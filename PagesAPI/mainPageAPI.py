from dorsaPylon import Collector

from PagesUI.mainPageUI import mainPageUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
import CONSTANTS
#from main_UI import routerUI
from uiUtils import GUIComponents
from backend.Camera import dorsaPylon
from backend.Processing import particlesDetector, Grading
from backend.Processing.Report import Report
from datetime import datetime
import cv2
import numpy as np
import time

storage_path = 'data/'

class mainPageAPI:

    def __init__(self, ui:mainPageUI, cameras:dorsaPylon, database:mainDatabase, ):
        self.ui = ui
        self.database = database
        self.cameras = cameras

        self.t_frame = 0
        self.frame_idx = 0
        self.logined_username = ''
        self.external_report_event_func = None
    
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
        #calculate FPS-----------------------
        self.ui.set_information({"fps": self.calc_fps()})
        #________________________________ONLY FOR TEST________________________________________________
        fname = "{}.png".format(self.test_img_idx)
        img = cv2.imread(f"backend\Processing\\test_imgs\\{fname}", 0)
        self.test_img_idx+=1
        if self.test_img_idx>3:
            self.test_img_idx = 0
        #________________________________ONLY FOR TEST________________________________________________
        t = time.time()
        #----------------------------------------------------
        #detect particles
        particles = self.detector.detect(img, img_id=self.frame_idx)
        #extend new particels into particles buffer
        self.report.append(particles)

        #calculate histogram and upadte chart
        grading_percents = self.report.Grading.get_hist()
        self.ui.set_grading_chart_values(grading_percents)
        
        #calculate statistics information like std and avg
        infos = self.report.get_global_statistics()
        self.ui.set_information(infos)
        
        #----------------------------------------------------
        self.report_saver.save_image(img, self.frame_idx)
        #----------------------------------------------------
        #get toolboxes value
        toolboxes_state = self.ui.get_toolboxes()
        if toolboxes_state['live']:
            if toolboxes_state['drawing']:
                img = particlesDetector.draw_particles(img, particles.particels)
            self.ui.set_live_img(img)
        #----------------------------------------------------
        
        self.frame_idx +=1
        t = time.time() - t
        print(t)

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

        #---------------------------------------------------------------------------
        #show sample information box
        self.ui.show_sample_info_window()


    def fast_start(self,):
        return
        for camera in self.cameras.values():
            camera.Operations.start_grabbing()

        self.ui.set_player_buttons_status('start')


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
        self.ui.set_grading_chart_ranges(standard['ranges'])
        #-----------------------------------------------------------------------------------------
        main_path = self.database.setting_db.storage_db.load()['path']
        
        self.report = Report( sample_name, standard, self.logined_username, main_path )
        #self.report.set_operator_username(self.logined_username)
        self.report_saver = reportFileHandler(main_path, self.report.name, self.report.date_time)
        #-----------------------------------------------------------------------------------------
        db_data = self.report.get_database_record()
        self.database.reports_db.save(db_data)
        #-----------------------------------------------------------------------------------------
        self.t_frame = time.time()
        self.frame_idx = 0
        #set chart bars
        
        #disable start and fast_start button and enable stop button