from datetime import datetime
import cv2
import numpy as np
import time
from PySide6.QtCore import QThread, QObject, Signal, QMutex
import copy

import CONSTANTS
from PagesUI.mainPageUI import mainPageUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
from uiUtils import GUIComponents
from backend.Camera import dorsaPylon
from backend.Processing import particlesDetector
from backend.Processing.Report import Report


storage_path = 'data/'

class mainPageAPI:
    refresh_time = time.time()
    max_fps = 20
    max_thread = 3

    def __init__(self, ui:mainPageUI, cameras:dorsaPylon, database:mainDatabase, ):
        self.ui = ui
        self.database = database
        self.cameras = cameras

        self.t_frame = 0
        self.logined_username = ''
        self.external_report_event_func = None
        self.is_running = False
        self.during_processing = False
    
        self.warning_checker_timer = GUIComponents.timerBuilder(1000, self.check_warnings)
        self.warning_checker_timer.start()

        self.ui.player_buttons_connect('fast_start', self.fast_start)
        self.ui.player_buttons_connect('start', self.start)
        self.ui.player_buttons_connect('stop', self.stop)
        self.ui.run_button_connect(self.run_start)
        self.ui.report_button_connector(self.report_button_event)

        self.test_img_idx = 0
        self.report = Report()
        self.detector = None
    
    def startup(self,):
        if not self.is_running:
            self.ui.set_live_img(CONSTANTS.IMAGES.NO_IMAGE)
        #self.ui.startup()

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
        fps = 1/(time.time() - self.t_frame)
        self.t_frame = time.time()
        fps = np.round(fps, 1)
        return fps
    
        

    def check_warnings(self,):
        #print('camera Error')
        pass

    def process_image(self):
        if not self.during_processing:
            self.during_processing = True
            #calculate FPS-----------------------
            self.ui.set_information({"fps": self.calc_fps()})
            #________________________________ONLY FOR TEST________________________________________________
            fname = "{}.png".format(self.test_img_idx)
            img = cv2.imread(f"backend\Processing\\test_imgs\\{fname}", 0)
            #cv2.circle(img, (10,10), 10, (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255),), -1)
            self.test_img_idx+=1
            if self.test_img_idx>4:
                self.test_img_idx = 0
            #________________________________ONLY FOR TEST________________________________________________

            self.thread = QThread()
            self.worker = ProcessingWorker(img, self.detector, self.report, self.report_saver)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run_process)
            self.worker.finished_processing.connect(self.show_live_info)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.finished.connect(self.__set_processing_finish__)
            
            self.thread.start()

    

    def __set_processing_finish__(self,):
        self.during_processing = False



    def show_live_info(self):
        
        t = time.time()
        #update info in UI less than max_fps value
        #print(1/(t - self.refresh_time))
        if 1/(t - self.refresh_time) < self.max_fps:
            self.refresh_time = time.time()

            particle_buffer = self.worker.get_particles()
            img = self.worker.img
            self.worker.confirm_remove_permit()

            #calculate statistics information like std and avg
            infos = self.report.get_global_statistics()
            self.ui.set_information(infos)

            #calculate histogram and upadte chart
            grading_percents = self.report.Grading.get_hist()
            self.ui.set_grading_chart_values(grading_percents)

            #radiuses, cum_precents = self.report.get_accumulative_grading()
            radiuses, cum_precents = self.report.cumGrading.get_data()
            self.ui.set_cumulative_chart_value(radiuses, cum_precents)

            toolboxes_state = self.ui.get_toolboxes()
            if toolboxes_state['live']:
                if toolboxes_state['drawing']:
                    img = particlesDetector.draw_particles(img, particle_buffer.get_particels())
                self.ui.set_live_img(img)
            



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


    def start(self,):
        standards = self.database.grading_ranges_db.load_all()
        
        #error if no standards definded
        if len(standards) == 0:
            self.ui.write_error_msg("No standard defineded, Go to 'Settings >> Grading' and define new one")
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


    def fast_start(self,):
        return



    def stop(self,):
        flag = self.ui.show_dialog_box( 'Stop',
                                        'Are You shure you want to stop the measuring?',
                                        buttons=['yes', 'cancel']
                                        )
        if flag == 'cancel':
            return
        
        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()

        #disable stop button
        self.ui.set_player_buttons_status('stop')
        self.ui.enable_reports(True)
        self.report_saver.save_report(self.report)
        #-----------------------------------------------------------------------------------------
        db_data = self.report.get_database_record()
        self.database.reports_db.save(db_data)
        #-----------------------------------------------------------------------------------------
        self.is_running = False

        self.ui.set_live_img(CONSTANTS.IMAGES.STOP_SAMPLING)

    
    
    


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

        self.prepeard_measuring_system(sample_name=info['name'], standard_name=info['standard'])
        
        #disable start and fast_start buttons and enable stop button
        self.ui.set_player_buttons_status('start')
        #close sample info window
        self.ui.close_sample_info_window()
        self.ui.enable_reports(False)
        
        self.is_running = True
        
        for camera in self.cameras.values():
            camera.Operations.start_grabbing()



    
    def prepeard_measuring_system(self, sample_name = None, standard_name = None, username = ''):
        
        #-----------------------------------------------------------------------------------------
        #load algorithm parms from database
        algorithm_data = self.database.setting_db.algorithm_db.load()
        #build detector
        self.detector = particlesDetector.particlesDetector(algorithm_data['threshold'], 0.1, algorithm_data['border'])
        #-----------------------------------------------------------------------------------------
        #load selected standard from databasr
        standard = self.database.grading_ranges_db.load(standard_name)
        #set ranges to chart
        self.ui.set_grading_chart_bars_ranges(standard['ranges'])
        #-----------------------------------------------------------------------------------------
        main_path = self.database.setting_db.storage_db.load()['path']
        settings =  self.database.setting_db.sample_db.load()
        
        self.report = Report( sample_name, standard, self.logined_username, main_path, settings=settings )
        #self.report.set_operator_username(self.logined_username)
        self.report_saver = reportFileHandler(main_path, self.report.name, self.report.date_time)
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
            self.particles_buffer = self.detector.detect(self.img)
            #extend new particels into particles buffer
            self.report.append(self.particles_buffer)
            self.finished_processing.emit()
        
            if self.report.settings['save_image']:
                for particle in self.particles_buffer.get_particels():
                    p_img = particle.get_roi_image(self.img)
                    img_id = particle.get_id()
                    self.report_saver.save_image(p_img, img_id)

        while not self.remove_permit:
            time.sleep(0.05)


        self.finished.emit()

    def get_particles(self, ):
        return copy.copy(self.particles_buffer)
    

    def confirm_remove_permit(self,):
        self.remove_permit = True
    

