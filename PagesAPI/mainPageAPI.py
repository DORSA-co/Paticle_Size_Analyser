from datetime import datetime
import copy
import time
import os

import cv2
import numpy as np

from PySide6.QtCore import QThread, QObject, Signal, QMutex


import Constants.CONSTANTS as CONSTANTS
from PagesUI.mainPageUI import mainPageUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
from uiUtils import GUIComponents
from backend.Camera import dorsaPylon
from backend.Processing import particlesDetector
from backend.Processing.Report import Report
from backend.Utils.datetimeUtils import timerCounter
import threading

# class myThread(QThread):
#     def quit(self) -> None:
#         print('Quit thread')
#         return super().quit()


class mainPageAPI:
    refresh_time = time.time()
    max_fps = 20
    DEBUG_PROCESS_THREAD = False
    #max_thread = 3

    def __init__(self, ui:mainPageUI, cameras:dict[str,dorsaPylon.Camera], database:mainDatabase, ):
        self.ui = ui
        self.database = database
        self.cameras = cameras
        self.default_camera_status = False

        self.t_frame = 0
        self.permissible_fps = self.max_fps
        self.fps = 0
        self.logined_username = ''
        self.external_report_event_func = None
        self.is_running = False
        self.during_processing = False
        self.processing_time = 0
        
    
        self.warning_checker_timer = GUIComponents.timerBuilder(1000, self.check_warnings)
        self.warning_checker_timer.start()

        self.system_timer_thread = GUIComponents.timerBuilder(1000, self.running_one_second_event)
        self.system_timer_thread.start()
        self.running_timer = timerCounter()


        self.ui.player_buttons_connect('fast_start', self.fast_start)
        self.ui.player_buttons_connect('start', self.start)
        self.ui.player_buttons_connect('stop', self.stop)
        self.ui.run_button_connect(self.run_start)
        self.ui.report_button_connector(self.report_button_event)

        self.test_img_idx = 0
        self.report:Report = None
        self.detector = None
        self.startup()
    
    def startup(self,):
        if not self.is_running:
            self.ui.set_live_img(CONSTANTS.IMAGES.NO_IMAGE)
        self.ui.startup()

    def set_logined_user(self, username:str):
        """this function calls from main_API when a login or logout event happend and gets logined username

        Args:
            username (str): logined username
        """
        self.logined_username = username

    def set_report_button_event_func(self, func):
        self.external_report_event_func = func

    def report_button_event(self,):
        if self.external_report_event_func is not None:
            self.external_report_event_func(self.report, 'main')


    def calc_fps(self):
        fps = 1/(abs((time.time() - self.t_frame )) + 1e-5)
        #fps = self.fps * 0.8 + fps*0.2 #movig avrage 
        self.t_frame = time.time()
        self.fps = np.round(fps, 1)
        return self.fps
    
        

    def check_warnings(self,):
        warning_flag_temp = True
        for cam in self.cameras.values():
            if cam.Status.is_open():
                temp = cam.Status.get_tempreture()

                if temp is None:
                    self.ui.set_information({'tempreture':'not avaiable'})
                else:
                    self.ui.set_information({'tempreture':temp})
                    if temp > CONSTANTS.MAX_CAMERA_TEMP:
                        warning_flag_temp = False
                        break
                    

        self.ui.set_warning_buttons_status('tempreture', warning_flag_temp)
        



    def process_image(self):
        #print('process_image')
        if self.is_running:
            if not self.during_processing:
                
                self.during_processing = True
                self.calc_fps()
                #self.ui.set_information({"fps": self.calc_fps()})
                #________________________________ONLY FOR TEST________________________________________________
                img = None
                if self.cameras['standard'].Infos.is_Simulation():
                    fname = "{}.jpg".format(self.test_img_idx)
                    path = os.path.join(CONSTANTS.Files.DEMO_IMGS_DIR, fname)
                    img = cv2.imread(path, 0)

                
                    self.test_img_idx+=1
                    if self.test_img_idx>=len(os.listdir(CONSTANTS.Files.DEMO_IMGS_DIR)):
                        self.test_img_idx = 0
                else:
                    img = self.cameras['standard'].image
                
                if img is None:
                    self.during_processing = False
                    return
                #________________________________ONLY FOR TEST________________________________________________
                self.processing_time = time.time()

                
                self.worker = ProcessingWorker(img, self.detector, self.report, self.report_saver)
                self.thread = threading.Thread(target=self.worker.run_process)

                self.worker.finished_processing.connect(self.show_live_info)
                self.worker.finished.connect(self.__set_processing_finish__)
                
                if self.DEBUG_PROCESS_THREAD:
                    self.worker.run_process()
                else:
                    self.thread.start()

            else:
                if ( time.time() - self.refresh_time ) >=1:
                    print('TimeOut')
                    #self.thread.quit()
                    self.during_processing = False
                    self.refresh_time = time.time()

    

    def __set_processing_finish__(self,):
        #print('__set_processing_finish__')
        self.during_processing = False
        self.processing_time = time.time() - self.processing_time
        #print('processing_time = ', self.processing_time)



    def show_live_info(self):
        t = time.time()
        
        if 1/(t - self.refresh_time) < self.max_fps and self.is_running:
            self.refresh_time = time.time()

            t1= time.time()
            particles = self.worker.get_particles()
            img = self.worker.img

            infos = self.report.get_global_statistics()
            self.ui.set_information(infos)

            grading_percents = self.report.Grading.get_hist()
            self.ui.set_grading_chart_values(grading_percents)

            radiuses, cum_precents = self.report.cumGrading.get_data()
            self.ui.set_cumulative_chart_value(radiuses, cum_precents)

            toolboxes_state = self.ui.get_toolboxes()
            if toolboxes_state['live']:
                if toolboxes_state['drawing']:
                    img = particlesDetector.draw_particles(img, particles)

                self.ui.set_live_img(img)

            delay_time = time.time() - self.refresh_time
            real_fps = 1 / (delay_time + 1e-3)
            real_fps *= 0.1 #for safity
            #print('real_fps', real_fps)
            self.permissible_fps = min(self.max_fps, real_fps)
                    
        
            



    def build_autoname_sample(self, sample_setting):
        name_struct = str(sample_setting['autoname_struct'])
        _datetime = datetime.now()
        idx = 0
        name = ''
        while idx < len(name_struct):
            if name_struct[idx] == CONSTANTS.NAME_CODE_SPACER:
                name += CONSTANTS.NAME_CODE_SPACER
            
            elif name_struct[idx] == CONSTANTS.NAME_CODE_CHAR:
                code_end_idx = name_struct.find(CONSTANTS.NAME_CODE_CHAR, idx+1)
                code_name = name_struct[idx+1 : code_end_idx]
                idx = code_end_idx

                if code_name.lower() == 'year':
                    name += _datetime.strftime("%Y")

                elif code_name.lower() == 'month':
                    name += _datetime.strftime("%m")

                elif code_name.lower() == 'day':
                    name += _datetime.strftime("%d")

                elif code_name.lower() == 'hour':
                    name += _datetime.strftime("%H")

                elif code_name.lower() == 'minute':
                    name += _datetime.strftime("%M")
                
                elif code_name.lower() == 'username':
                    name += self.logined_username

                elif code_name.lower() == 'text1':
                    name += sample_setting['text1']
            idx+=1
        return name

    def handle_standard_error(self, standards):
        #error if no standards definded
        if len(standards) == 0:
            self.ui.write_error_msg("No standard defineded, Go to 'Standards >> New Standard' and define new one")
            return False
        return True
    

    def start(self,):
        standards = self.database.standards_db.load_all()

        ######## check camera status
        if not self.default_camera_status:
            self.ui.write_error_msg("chosen camera in settings is not connected")
            return
        
        #error if no standards definded
        if not self.handle_standard_error(standards):
            return
        
        #---------------------------------------------------------------------------
        sample_setting = self.database.setting_db.sample_db.load()
        #---------------------------------------------------------------------------
        #extract name of standards from standards list
        standards_name = list(map( lambda x:x['name'], standards))
        #set standards into combobox
        self.ui.set_sample_info_standards_items(standards_name)
        self.ui.set_sample_info_selected_standard( sample_setting['default_standard'])
        #---------------------------------------------------------------------------
        
        if sample_setting['autoname_enable']:
            name = self.build_autoname_sample(sample_setting)
            self.ui.set_sample_info_sample_name(name)
            self.ui.disable_sample_info_sample_name(False)
        else:
            self.ui.disable_sample_info_sample_name(True)

        #---------------------------------------------------------------------------
        #show sample information box
        self.ui.show_sample_info_window()

    ############################## event default camera status ###############################

    def default_camera_status_event(self, status: bool):
        self.default_camera_status = status
        self.ui.set_warning_buttons_status('camera_connection', status)


    def fast_start(self,):
        standards = self.database.standards_db.load_all()


        ######## check camera status
        if not self.default_camera_status:
            self.ui.write_error_msg("chosen camera in settings is not connected")
            return
        
        if not self.handle_standard_error(standards):
            return
           
        #---------------------------------------------------------------------------
        sample_setting = self.database.setting_db.sample_db.load()
        #---------------------------------------------------------------------------
        #extract name of standards from standards list
        standards_name = list(map( lambda x:x['name'], standards))
        #set standards into combobox
        self.ui.set_sample_info_standards_items(standards_name)

        default_standard = sample_setting.get('default_standard')
        if default_standard == None or default_standard == '-':
            self.ui.write_error_msg("No default standard selected. go to 'Settings >> sample Setting' and choose a default standard")
            return
        
        if default_standard not in standards_name:
            self.ui.write_error_msg("Couldn't find default standard. go to 'Settings >> sample Setting' and choose a default standard")
            return

        self.ui.set_sample_info_selected_standard( sample_setting['default_standard'])
        #---------------------------------------------------------------------------

        if not sample_setting['autoname_enable']:
            self.ui.write_error_msg("You Should enable 'Auto name' to use fast start. go to Settings >> sample Setting and setup 'Auto Sample Name'")
            return
        
            
        name = self.build_autoname_sample(sample_setting)
        self.ui.set_sample_info_sample_name(name)
        self.ui.disable_sample_info_sample_name(False)

        self.run_start()


    def stop(self,ask=True):
        if not self.is_running:
            return

        if ask:
            flag = self.ui.show_dialog_box( 'Stop',
                                            'Are You shure you want to stop the measuring?',
                                            buttons=['yes', 'cancel']
                                            )
            if flag == 'cancel':
                return

        self.is_running = False
        self.during_processing = False
        

        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()     
        
        
        self.report_saver.save_report(self.report)
        #-----------------------------------------------------------------------------------------
        db_data = self.report.get_database_record()
        self.database.reports_db.save(db_data)
        #-----------------------------------------------------------------------------------------
        
        self.ui.set_live_img(CONSTANTS.IMAGES.STOP_SAMPLING)

        self.ui.enable_report(True)
        self.ui.set_player_buttons_status('stop')
        #print('stop FINISH')

    
    
    


    def run_start(self,):
        """this function called when run button in sample_info dialog box clicked
        """
        #get inputs
        info = self.ui.get_sample_info()

        if info['name'] == "":
            self.ui.write_sample_info_error_msg("Name field cann't be empty")
            return
        #clear error from sample info window box
        self.ui.write_sample_info_error_msg(None)

        self.prepeard_measuring_system(info)
        
        #disable start and fast_start buttons and enable stop button
        self.ui.set_player_buttons_status('start')
        #close sample info window
        self.ui.close_sample_info_window()
        self.ui.enable_report(False)
        
        self.is_running = True
        
        for camera in self.cameras.values():
            camera.Operations.start_grabbing()
        
        self.running_timer = timerCounter()
        #self.running_timer.set_external_event(self.running_one_second_event)
        #self.running_timer.run()

        



    
    def prepeard_measuring_system(self, info = {}):
        
        #-----------------------------------------------------------------------------------------
        #load algorithm parms from database
        algorithm_data = self.database.setting_db.algorithm_db.load()
        #build detector
        self.detector = particlesDetector.particlesDetector(algorithm_data['threshold'], 
                                                            CONSTANTS.Calibration.PX2MM, 
                                                            algorithm_data['border'])
        #-----------------------------------------------------------------------------------------
        #load selected standard from databasr
        standard = self.database.standards_db.load(info['standard'])
        #set ranges to chart
        self.ui.set_grading_chart_bars_ranges(standard['ranges'])
        #-----------------------------------------------------------------------------------------
        main_path = self.database.setting_db.storage_db.load()['path']
        settings =  self.database.setting_db.sample_db.load()
        #-----------------------------------------------------------------------------------------
        self.report = Report( info['name'],
                              standard,
                              self.logined_username,
                              main_path,
                              settings=settings,
                              description = info['description'] 
                              )
        args = {'path':main_path, 'name':self.report.name, 'date':self.report.date, 'time':self.report.time}
        self.report_saver = reportFileHandler(args)
        #-----------------------------------------------------------------------------------------
        min_v, max_v = self.report.get_full_range()
        self.ui.set_cumulative_chart_range(min_v, max_v)
        
        self.t_frame = time.time()
        

    
    def endup(self):
        if self.is_running:
            self.ui.show_dialog_box("Warning", 
                                    "You can't leave this page when system is Running, Please stop it first",
                                    buttons=['ok'])
            return False
        return True
    

    def running_one_second_event(self,):
        self.running_timer.count(second=1)
        if self.is_running:
            info = {'timer' : self.running_timer.get_fstr('%M:%S'),
                    'fps': self.fps,
                    }
            self.ui.set_information(info)







class ProcessingWorker(QObject):
    finished = Signal()
    finished_processing = Signal()
    def __init__(self, 
                 img:np.ndarray,
                 detector:particlesDetector.particlesDetector,
                 report: Report,
                 report_saver: reportFileHandler
                 
                 
                 ) -> None:
        super(ProcessingWorker,self).__init__()
        self.img = img
        self.detector = detector
        self.report = report
        self.report_saver = report_saver
        self.remove_permit = False


    
    def run_process(self,):

        for i in range(1):
            try:
                self.current_particles = self.detector.detect(self.img, self.report)

                self.finished_processing.emit()
            
                if self.report.settings['save_image']:
                    for particle in self.current_particles:
                        p_img = particle.get_roi_image(self.img)
                        img_id = particle.get_id()
                        self.report_saver.save_image(p_img, img_id)
            except Exception as e:
                print(e)

        #print('FINISH signal--')
        self.finished.emit()
        #print('FINISH signal**')

    def get_particles(self, ):
        return copy.copy(self.current_particles)
    

