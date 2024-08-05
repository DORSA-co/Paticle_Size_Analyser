from datetime import datetime
import copy
import time
import threading

import numpy as np

from PySide6.QtCore import QObject, Signal


import Constants.CONSTANTS as CONSTANTS
from PagesUI.mainPageUI import mainPageUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
from uiUtils import GUIComponents
from backend.Camera import dorsaPylon
from backend.Processing import particlesDetector
from backend.Processing.Report import Report
from backend.Utils.datetimeUtils import timerCounter
from Mediator.mainMediator import Mediator
from backend.Processing.Particel import Particle


# class myThread(QThread):
#     def quit(self) -> None:
#         print('Quit thread')
#         return super().quit()


class mainPageAPI:
    refresh_time = time.time()
    max_fps = 20
    DEBUG_PROCESS_THREAD = False

    def __init__(self, uiHandeler:mainPageUI, cameras:dict[str,dorsaPylon.Camera], database:mainDatabase, ):
        self.uiHandeler = uiHandeler
        self.database = database
        self.cameras = cameras
        self.Mediator = Mediator()
        self.default_camera_status = False

        self.t_frame = 0
        self.permissible_fps = self.max_fps
        self.fps = 0
        self.logined_username = ''
        self.external_report_event_func = None
        self.is_running = False
        self.during_processing = False
        self.processing_time = 0
        self.auto_run_flag = False

        self.warnings_and_status = {
            'camera_connection': False,
            'camera_grabbing': False,
            'illumination': True,
            'tempreture': False,
            'plc': False

        }
        
    
        self.warning_checker_timer = GUIComponents.timerBuilder(1000, self.check_warnings)
        self.warning_checker_timer.start()

        self.system_timer_thread = GUIComponents.timerBuilder(1000, self.running_one_second_event)
        self.system_timer_thread.start()
        self.running_timer = timerCounter()

        self.uiHandeler.run_auto_button_connector(self.run_auto)
        self.uiHandeler.player_buttons_connect('fast_start', self.fast_start)
        self.uiHandeler.player_buttons_connect('start', self.start)
        self.uiHandeler.player_buttons_connect('stop', self.stop)
        self.uiHandeler.sampleInfoDialog.button_connector('run', self.run_start)
        self.uiHandeler.report_button_connector(self.report_button_event)
        self.uiHandeler.sampleInfoDialog.set_grading_parm_items(list(CONSTANTS.Sample.GRADING_PARMS.keys()))

        self.test_img_idx = 0
        self.report:Report = None
        self.detector = None
        self.Mediator = Mediator()
        self.startup()
    
    def startup(self,):
        for name, status in self.warnings_and_status.items():
            self.uiHandeler.set_warning_buttons_status(name, status)
        if not self.is_running:
            self.uiHandeler.set_live_img(CONSTANTS.IMAGES.NO_IMAGE)
        self.uiHandeler.startup()

    def run_auto(self,):
        self.auto_run_flag = not(self.auto_run_flag)
        self.uiHandeler.set_auto_run_status(self.auto_run_flag)
        self.Mediator.send('auto_run_changed', self.auto_run_flag)

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
                    self.uiHandeler.set_information({'tempreture':'not avaiable'})
                else:
                    self.uiHandeler.set_information({'tempreture':temp})
                    if temp > CONSTANTS.MAX_CAMERA_TEMP:
                        warning_flag_temp = False
                        break
                    

        self.set_system_status('tempreture', warning_flag_temp)
        



    def process_image(self, img:np.ndarray):

        if self.is_running:
            if not self.during_processing:
                
                self.during_processing = True
                self.calc_fps()
              
                
                if img is None:
                    self.during_processing = False
                    return
                #________________________________ONLY FOR TEST________________________________________________
                self.processing_time = time.time()

                
                self.worker = ProcessingWorker(img, self.detector, self.report, self.report_saver)
                self.thread = threading.Thread(target=self.worker.run_process)
                self.worker.founded_particels.connect(self.particales_found_evet)
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

    def particales_found_evet(self, particels:list[Particle]):
        self.Mediator.send('particels_founded', particels)

    def __set_processing_finish__(self,):
        #print('__set_processing_finish__')
        self.during_processing = False
        self.processing_time = time.time() - self.processing_time
        #print('processing_time = ', self.processing_time)



    def show_live_info(self):
        t = time.time()
        
        if 1/((t - self.refresh_time) + 1e-5) < self.max_fps and self.is_running:
            self.refresh_time = time.time()

            particles = self.worker.get_particles()
            img = self.worker.img

            infos = self.report.get_global_statistics()
            self.uiHandeler.set_information(infos)

            grading_percents = self.report.Grading.get_hist()
            self.uiHandeler.set_grading_chart_values(grading_percents)

            radiuses, cum_precents = self.report.cumGrading.get_data()
            self.uiHandeler.set_cumulative_chart_value(radiuses, cum_precents)

            toolboxes_state = self.uiHandeler.get_toolboxes()
            if toolboxes_state['live']:
                if toolboxes_state['drawing']:
                    img = particlesDetector.draw_particles(img, particles)

                self.uiHandeler.set_live_img(img)

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
            if name_struct[idx] in [CONSTANTS.NAME_CODES['dash'],
                                    CONSTANTS.NAME_CODES['spacer'],]:
                name += name_struct[idx]
            
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
            self.uiHandeler.write_error_msg("No standard defineded, Go to 'Standards >> New Standard' and define new one")
            return False
        return True
    

    def start(self,):
        standards = self.database.standards_db.load_all()

        ######## check camera status
        if not self.warnings_and_status['camera_connection']:
            self.uiHandeler.write_error_msg("chosen camera in settings is not connected")
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
        self.uiHandeler.sampleInfoDialog.set_standards_items(standards_name)
        self.uiHandeler.sampleInfoDialog.set_current_standard( sample_setting['default_standard'])
        #---------------------------------------------------------------------------
        self.uiHandeler.sampleInfoDialog.set_current_grading_parm(sample_setting['default_grading_parm'])
        #---------------------------------------------------------------------------
        
        if sample_setting['autoname_enable']:
            name = self.build_autoname_sample(sample_setting)
            self.uiHandeler.sampleInfoDialog.set_sample_name(name)
            self.uiHandeler.sampleInfoDialog.disable_sample_name(False)
        else:
            self.uiHandeler.sampleInfoDialog.disable_sample_name(True)

        #---------------------------------------------------------------------------
        #show sample information box
        self.uiHandeler.sampleInfoDialog.show()

    ############################## event default camera status ###############################

    def set_system_status(self, name,  status: bool):
        if self.warnings_and_status[name] != status:
            self.warnings_and_status[name] = status
            self.uiHandeler.set_warning_buttons_status(name, status)
        
        if name in ['camera_connection', 'camera_grabbing'] and status == False:
            if self.is_running:
                self.stop(False)



    def fast_start(self,):
        standards = self.database.standards_db.load_all()


        ######## check camera status
        if not self.warnings_and_status['camera_connection']:
            self.uiHandeler.write_error_msg("chosen camera in settings is not connected")
            self.Mediator.send_start_processing_status(False)
            return
        
        if not self.handle_standard_error(standards):
            self.Mediator.send_start_processing_status(False)
            return

           
        #---------------------------------------------------------------------------
        sample_setting = self.database.setting_db.sample_db.load()
        #---------------------------------------------------------------------------
        #extract name of standards from standards list
        standards_name = list(map( lambda x:x['name'], standards))
        #set standards into combobox
        self.uiHandeler.sampleInfoDialog.set_standards_items(standards_name)

        default_standard = sample_setting.get('default_standard')
        if default_standard == None or default_standard == '-':
            self.uiHandeler.write_error_msg("No default standard selected. go to 'Settings >> sample Setting' and choose a default standard")
            self.Mediator.send_start_processing_status(False)
            return
        
        if default_standard not in standards_name:
            self.uiHandeler.write_error_msg("Couldn't find default standard. go to 'Settings >> sample Setting' and choose a default standard")
            self.Mediator.send_start_processing_status(False)
            return

        self.uiHandeler.sampleInfoDialog.set_current_standard( sample_setting['default_standard'])
        self.uiHandeler.sampleInfoDialog.set_current_grading_parm( sample_setting['default_grading_parm'])
        #---------------------------------------------------------------------------

        if not sample_setting['autoname_enable']:
            self.uiHandeler.write_error_msg("You Should enable 'Auto name' to use fast start. go to Settings >> sample Setting and setup 'Auto Sample Name'")
            self.Mediator.send_start_processing_status(False)
            return
        
            
        name = self.build_autoname_sample(sample_setting)
        self.uiHandeler.sampleInfoDialog.set_sample_name(name)
        self.uiHandeler.sampleInfoDialog.disable_sample_name(False)

        res = self.run_start()
        self.Mediator.send_start_processing_status(res)



    def stop(self,ask=True):
        if not self.is_running:
            return

        if ask:
            flag = self.uiHandeler.show_dialog_box( 'Stop',
                                            'Are You shure you want to stop the measuring?',
                                            buttons=['yes', 'cancel']
                                            )
            if flag == 'cancel':
                return

        self.is_running = False
        self.during_processing = False
        

        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()     
        
        if len(self.report.Buffer.total_buffer.particels):
            self.report_saver.save_report(self.report)
            #-----------------------------------------------------------------------------------------
            db_data = self.report.get_database_record()
            self.database.reports_db.save(db_data)
            #-----------------------------------------------------------------------------------------
            self.uiHandeler.enable_report(True)

        else:
            self.uiHandeler.enable_report(False)

            self.uiHandeler.show_dialog_box( 'Warning',
                                            'No Particle Founded.',
                                            buttons=['ok']
                                            )
            

        
        self.uiHandeler.set_live_img(CONSTANTS.IMAGES.STOP_SAMPLING)
        self.uiHandeler.set_player_buttons_status('stop')
        #print('stop FINISH')

    
    
    


    def run_start(self,):
        """this function called when run button in sample_info dialog box clicked
        """
        #get inputs
        info = self.uiHandeler.sampleInfoDialog.get_info()

        if info['name'] == "":
            self.uiHandeler.sampleInfoDialog.write_error_massage("Name field cann't be empty")
            return False
        #clear error from sample info window box
        self.uiHandeler.sampleInfoDialog.write_error_massage(None)

        self.prepeard_measuring_system(info)
        
        #disable start and fast_start buttons and enable stop button
        self.uiHandeler.set_player_buttons_status('start')
        #close sample info window
        self.uiHandeler.sampleInfoDialog.close()
        self.uiHandeler.enable_report(False)
        
        self.is_running = True
        
        for camera in self.cameras.values():
            camera.Operations.start_grabbing()
        
        self.running_timer = timerCounter()
        return True
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
        self.uiHandeler.set_grading_chart_bars_ranges(standard['ranges'])
        #-----------------------------------------------------------------------------------------
        main_path = self.database.setting_db.storage_db.load()['path']
        settings =  self.database.setting_db.sample_db.load()
        #-----------------------------------------------------------------------------------------
        self.report = Report( info['name'],
                              standard,
                              self.logined_username,
                              main_path,
                              settings=settings,
                              description = info['description'] ,
                              grading_parm = info['grading_parm']
                              )
        args = {'path':main_path, 'name':self.report.name, 'date':self.report.date, 'time':self.report.time}
        self.report_saver = reportFileHandler(args)
        #-----------------------------------------------------------------------------------------
        min_v, max_v = self.report.get_full_range()
        self.uiHandeler.set_cumulative_chart_range(min_v, max_v)
        
        self.t_frame = time.time()
        

    
    def endup(self):
        if self.is_running:
            self.uiHandeler.show_dialog_box("Warning", 
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
            self.uiHandeler.set_information(info)







class ProcessingWorker(QObject):
    finished = Signal()
    founded_particels = Signal(list)
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
        self.current_particles = []


    
    def run_process(self,):

        for i in range(1):
            try:
                self.current_particles = self.detector.detect(self.img, self.report)
                if len(self.current_particles):
                    self.founded_particels.emit(self.current_particles)

                self.finished_processing.emit()
            
                if self.report.settings['save_image']:
                    for particle in self.current_particles:
                        p_img = particle.get_roi_image(self.img)
                        img_id = particle.get_id()
                        self.report_saver.save_image(p_img, img_id)
            except Exception as e:
                print('ERROR in ProcessingWorker', e)

        #print('FINISH signal--')
        self.finished.emit()
        #print('FINISH signal**')

    def get_particles(self, ):
        return copy.copy(self.current_particles)
    

