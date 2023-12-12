import copy
import time
import threading

import numpy as np
import cv2
from PySide6.QtCore import QThread, QObject, Signal, QMutex

from backend.Processing import particlesDetector
import Constants.CONSTANTS as CONSTANTS
from PagesUI.validationPageUI import validationPageUI, statisticalHypothesisTab, calibrationTabUI, testSectionUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
from backend.Processing.Report import Report
from backend.Calibration.testsValidation import weightDifferenceValidation, tTestValidation
from backend.Camera.dorsaPylon import Collector, Camera
from uiUtils.IO.Mouse import MouseEvent
from backend.Processing.Calibration import Calibration



class validationPageAPI:

    def __init__(self, ui:validationPageUI, database:mainDatabase, cameras: dict[str, Camera]):
        self.statisticalHypothesisTab = statisticalHypothesisTabAPI(ui.statisticalHypothesisTab, database)
        self.calibrationTab = calibrationTab(ui.calibrationTab, database=database, cameras=cameras)
    
    def startup(self,):
        self.statisticalHypothesisTab.startup()
        self.calibrationTab.startup()


class calibrationTab:
    DEBUG_PROCESS_THREAD = False

    def __init__(self, ui:calibrationTabUI, database: mainDatabase, cameras: dict[str, Camera]) -> None:
        self.ui = ui
        self.database = database
        self.cameras = cameras
        
        self.during_processing = False
        self.particles = []
        self.calib_image = None
        self.calibration_step = 'none'
        self.iteration = 0 
        self.total_iteration = CONSTANTS.Calibration.ITERATIONS
        #self.detector: particlesDetector.particlesDetector = None

        algorithm_data = self.database.setting_db.algorithm_db.load()
        self.calibration = Calibration(thresh=CONSTANTS.Calibration.THRESH,
                                       border=algorithm_data['border'],
                                       circularity=0.7,
                                       min_diameter_mm=0.8)
        
        
        self.ui.check_button_connector(self.set_step('check'))
        self.ui.start_button_connector(self.set_step('start'))
        self.ui.connect_image_mouse_event(self.image_mouse_event)

    def startup(self,):
        self.ui.startup()



    def image_mouse_event(self, event:MouseEvent):
        if event.is_click() and event.is_left_btn():
            pos = event.get_relative_postion()
   
            pos = self.calib_image.shape[::-1] * pos
            pos = pos.astype(np.int32)

            for particle in self.particles:
                cnt = particle.cnt
                dist = cv2.pointPolygonTest(cnt,pos.tolist(), False)
                if dist > 0:
                    img = self.calib_image.copy()
                    img = particlesDetector.draw_particles(img, self.particles, (255,0,0), 5 )
                    img = particlesDetector.draw_particles(img, [particle], (0,255,0), 5 )
                    img = particlesDetector.draw_particles_size(img, [particle], color=(0,0,255))
                    self.ui.show_live(img)
                    
        

    def set_step(self, step):

        def func():
            self.calibration_step = step
            if step == 'check':
                self.ui.write_check_massage(None)

            elif step == 'start':
                self.calibration.reset()
                self.iteration = 0
                self.ui.set_progress_bar(0)

            for camera in self.cameras.values():
                camera.Operations.start_grabbing()

        return func
    

    def camera_image_event(self,):
        cam_application = 'standard'
        image = self.cameras[cam_application].image

        if image is not None:

            if self.calibration_step == 'check':
                self.check_calibration_placement(image)
                
            
            elif self.calibration_step == 'start':
                self.calibration_proccess(image)
        else:
            return
    
    

    def check_calibration_placement(self, image):
        status, founded_count, real_count, particles = self.calibration.check(image)
        image = particlesDetector.draw_particles(image, particles, color=(255,0,0))
        # for part in particles:
        #     print(part.avg_diameter)
        self.ui.show_live(image)
        if status:
            self.ui.write_check_massage('Ok', status=status)
        else:
            self.ui.write_check_massage(
                massage=f""" found {founded_count} but should be {real_count} please sure calibrator placement is true and all glasses are clean""",
                status= status
            )

        self.calibration_step = 'none'
        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()

    def calibration_proccess(self, image):
        if not self.during_processing:
            self.during_processing = True
            if image is None:
                self.during_processing = False
                return
            #________________________________ONLY FOR TEST________________________________________________
            self.processing_time = time.time()
            self.calibration_worker = calibrationWorker(image,
                                            calibration=self.calibration,
                                            total_steps= self.total_iteration
                                            )
            
            self.thread = threading.Thread(target=self.calibration_worker.run_process)
            self.calibration_worker.finished_processing.connect(self.update_calibration)
            self.calibration_worker.finished.connect(self.__set_processing_finish__)
            
            if self.DEBUG_PROCESS_THREAD:
                self.calibration_worker.run_process()
            else:
                self.thread.start()

        else:
            if ( time.time() - self.processing_time ) >=1:
                print('TimeOut')
                self.during_processing = False
                self.processing_time = time.time()

    

    
    
    def stop_calibration(self, ):
        self.calibration_step = 'none'
        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()
        
        self.calibration.reset()


    

    def __set_processing_finish__(self,):
        self.during_processing = False
        self.processing_time = time.time() - self.processing_time

    
    def update_calibration(self,):
        self.iteration+=1
        percent = int((self.iteration / self.total_iteration) * 100)
        particles = self.calibration_worker.get_particles()
        self.ui.set_progress_bar(percent)
        
        if particles is not None:
            self.particles = particles
            self.calib_image = self.calibration_worker.img.copy()
            image = particlesDetector.draw_particles(self.calibration_worker.img, self.particles )
            self.ui.show_live(image)
        
        else:
            self.calibration_step = 'none'
            self.stop_calibration()
            self.ui.show_confirm_box('Warnings',
                                     massage='Please check calibration placement',
                                     buttons=['ok'])

            self.ui.set_progress_bar(0)
            
        
        if self.iteration == self.total_iteration:
            result = self.calibration.get_result()
            self.ui.show_calib_result(result)
            self.stop_calibration()
            
       




class statisticalHypothesisTabAPI:
    
    VERFICATION_TYPES = ['WSTD', 'T-Test']

    def __init__(self, ui:statisticalHypothesisTab, database:mainDatabase, ):
        self.ui = ui
        self.database = database
        self.test_section_idx = 0
        self.test_system_samples = [None] * self.ui.MAX_TEST_COUNT
        
        
        for i in range(self.ui.MAX_TEST_COUNT):
            test_section = self.ui.get_test_section(i)
            test_section.load_button_connector(self.test_section_load_sample)
        
        self.ui.sampleLoader.sample_button_connector(self.load_selected_sample)
        self.ui.calculate_button_connector(self.calculation)
        self.ui.set_verification_type_items(self.VERFICATION_TYPES)
        


    def test_section_load_sample(self, test_idx:int):
        """this function calls when user click on load sample button of any test section in validation Tab

        Args:
            test_idx (int): index of the test section that it's button clicked
        """
        self.test_section_idx = test_idx
        self.ui.sampleLoader.show_samples(self.database.reports_db.load_all())
        self.ui.sampleLoader.show()
        

    def load_selected_sample(self, sample):
        selcted_standard = self.ui.get_selected_standard()

        if sample['standard'] != selcted_standard:
            self.ui.sampleLoader.close()

            self.ui.show_confirm_box(
                        'Error', 
                        f'Selected sample is not in {selcted_standard} standard.choose another sample or rebuild it',
                        ['ok']
                        )
            return
        
        self.test_system_samples[self.test_section_idx] = sample
        standard = self.database.standards_db.load(sample['standard'])

        test_section = self.ui.get_test_section(self.test_section_idx)
        test_section.set_sample(sample, standard['ranges'])
        
        self.ui.sampleLoader.close()
            
        
        


    def startup(self,):
        self.load_standards()


    def load_standards(self,):
        standards_name = self.database.standards_db.load_standards_name()
        self.ui.set_standards_list(standards_name)


    def verfiy_siev_numbers(self, test_percents: list[np.ndarray]):
        """check sum of sive numbers be equal 100
        """
        flag = True
        for i , percents in enumerate(test_percents):
            sum_p = np.round(percents.sum(),3)
            if sum_p != 100:
                self.ui.get_test_section(i).write_error(f'sum of percents should be 100% but is {sum_p}%')
                flag = False
            else:
                self.ui.get_test_section(i).write_error(None)
        return flag
    
    
    
    def calculation(self,):
        n_test = self.ui.get_test_count()

        #fetch input percents of all tests
        sieve_percents = self.ui.get_sieve_inputs()

        #check sum of percents of each test is 100%
        if not self.verfiy_siev_numbers(sieve_percents):
            self.ui.show_confirm_box('Error',"Sum of some sieve percents aren't 100%", ['ok'])
            return
        
        system_percents = self.test_system_samples[:n_test].copy()
        system_percents = list(map(lambda x:x['grading_result'], system_percents))
        
        verfication_type = self.ui.get_verfication_type()
        
        text = ""
        status = False
        infoes = {}
        
        if verfication_type == 'wstd':
            wdv = weightDifferenceValidation()
            wdv.set_test(system_percents, sieve_percents)
            
            status, infoes = wdv.calculate()
            if status:
                text = "the Error between system and sieve is less than sieve STD and test passed."
            else:
                text = "the Error between system and sieve is more than sieve STD and test not passed."

            self.ui.resultDialog.set_page(0)

        
        else:
            t_test = tTestValidation()
            standatd_name = self.test_system_samples[0]['standard']
            standard = self.database.standards_db.load(standatd_name)
            
            t_test.set_ranges(standard['ranges'])
            t_test.set_test(system_percents, sieve_percents)
            status, infoes = t_test.calculate() 
            best = infoes['best_confidence']
            if status:
                text = f"T test passed in T95 condfidence (on-tail). the best confidence is {best}"
            else:
                text = f"T test didn't passed in T95 condfidence (on-tail). the best confidence is {best}"

            self.ui.resultDialog.set_page(1)

            
        self.ui.resultDialog.set_result_status(status)
        self.ui.resultDialog.set_info(infoes)
        self.ui.resultDialog.set_description(text)
        self.ui.resultDialog.show()
        
        
        



class calibrationWorker(QObject):
    finished = Signal()
    finished_processing = Signal()
    def __init__(self, 
                 img:np.ndarray,
                 calibration:Calibration,
                 total_steps = 10
                 ) -> None:
        super(calibrationWorker,self).__init__()
        self.img = img
        self.calibration = calibration
        self.total_steps = total_steps


    
    def run_process(self,):

        for i in range(1):
            try:
                self.particles = self.calibration.calibration(self.img)
                self.finished_processing.emit()
       
            except Exception as e:
                print(e)

        self.finished.emit()

    def get_particles(self, ):
        return copy.copy(self.particles)