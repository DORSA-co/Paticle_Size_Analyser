from dorsaPylon import Collector

from PagesUI.mainPageUI import mainPageUI
from Database.mainDatabase import mainDatabase
import CONSTANTS
#from main_UI import routerUI
from uiUtils import GUIComponents
from backend.Camera import dorsaPylon
from backend.Processing import particlesDetector, Grading

import cv2
import numpy as np
import time

class mainPageAPI:

    def __init__(self, ui:mainPageUI, cameras:dorsaPylon, database:mainDatabase, ):
        self.ui = ui
        self.database = database
        self.cameras = cameras

        self.t_frame = 0
    
        self.warning_checker_timer = GUIComponents.timerBuilder(1000, self.check_warnings)
        self.warning_checker_timer.start()

        self.ui.player_buttons_connect('fast_start', self.fast_start)
        self.ui.player_buttons_connect('start', self.start)
        self.ui.player_buttons_connect('stop', self.stop)
        self.ui.run_button_connect(self.run_start)

        self.test_img_idx = 0

        self.detector = particlesDetector.particlesDetector(50, 0.1, 10)
        self.gradind_calculator = Grading.Grading([])

    def check_warnings(self,):
        #print('checkwarning')
        pass

    def process_image(self):
        #calculate FPS-----------------------
        self.ui.set_information({"fps": self.calc_fps()})

        #-----------------------------------

        #________________________________ONLY FOR TEST________________________________________________
        fname = "{}.png".format(self.test_img_idx)
        img = cv2.imread(f"backend\Processing\\test_imgs\\{fname}", 0)
        self.test_img_idx+=1
        if self.test_img_idx>3:
            self.test_img_idx = 0
        #________________________________ONLY FOR TEST________________________________________________
        
        #----------------------------------------------------
        #detect particles
        particles = self.detector.detect(img, return_dataframe=False)

        max_rs = np.array( list( map( lambda x:(x.max_radius), particles)))
        avg_vs = np.array( list( map( lambda x:(x.avg_volume), particles)))

        self.gradind_calculator.append(max_rs, avg_vs)        

        #calculate histogram and upadte chart
        grading_percents = self.gradind_calculator.get_hist()
        self.ui.set_grading_chart_values(grading_percents)

        #calculate statistics information like std and avg
        infos = self.gradind_calculator.get_statistics()
        self.ui.set_information(infos)

        #----------------------------------------------------
        #get toolboxes value
        toolboxes_state = self.ui.get_toolboxes()
        if toolboxes_state['live']:
            if toolboxes_state['drawing']:
                img = particlesDetector.draw_particles(img, particles)
            self.ui.set_live_img(img)
        #----------------------------------------------------
        

    def start(self,):
            
        standards = self.database.setting_db.grading_db.load_all()
        
        #error if no standards definded
        if len(standards) == 0:
            self.ui.write_error_msg("No standard defineded, Go to 'Settings >> Grading' and define new one")
            return
        
        #---------------------------------------------------------------------------
        #extract name of standards from standards list
        standards_name = list(map( lambda x:x['name'], standards))
        #set standards into combobox
        self.ui.set_sample_info_standards_items(standards_name)

        self.ui.show_sample_info_window()

    

    def run_start(self,):
        #get inputs
        info = self.ui.get_sample_info()

        if info['name'] == "":
            self.ui.write_sample_info_error_msg("Name field cann't be empty")
            return
        #clear error from sample info window box
        self.ui.write_sample_info_error_msg(None)

        #load selected standard from database
        standard = self.database.setting_db.grading_db.load(info['standard'])
        #build a grading object base on selected standard's ranges
        self.gradind_calculator = Grading.Grading(standard['ranges'])
        #set chart bars
        self.ui.set_grading_chart_ranges(standard['ranges'])
        #disable start and fast_start button and enable stop button
        self.ui.set_player_buttons_status('start')
        #close sample info window
        self.ui.close_sample_info_window()

        self.t_frame = time.time()
        for camera in self.cameras.values():
            camera.Operations.start_grabbing()

        


    def fast_start(self,):
        return
        for camera in self.cameras.values():
            camera.Operations.start_grabbing()

        self.ui.set_player_buttons_status('start')


    def stop(self,):
        flag = self.ui.show_dialog_box('Stop',
                                        'Are You shure you want to stop the measuring?',
                                        buttons=['yes', 'cancel'])
        if flag == 'cancel':
            return
        
        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()

        #disable stop button
        self.ui.set_player_buttons_status('stop')
        self.ui.enable_reports(True)



    
    def calc_fps(self):
        fps = 1/(time.time() - self.t_frame)
        self.t_frame = time.time()
        fps = np.round(fps, 1)
        return fps

    