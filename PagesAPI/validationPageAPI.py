import numpy as np
import cv2

from backend.Processing import particlesDetector
import Constants.CONSTANTS as CONSTANTS
from PagesUI.validationPageUI import validationPageUI, statisticalHypothesisTab, calibrationTabUI, testSectionUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
from backend.Processing.Report import Report
from backend.Calibration.testsValidation import weightDifferenceValidation, tTestValidation
from backend.Camera.dorsaPylon import Collector, Camera
from uiUtils.IO.Mouse import MouseEvent

storage_path = 'data/'

class validationPageAPI:

    def __init__(self, ui:validationPageUI, database:mainDatabase, cameras: dict[str, Camera]):
        self.statisticalHypothesisTab = statisticalHypothesisTabAPI(ui.statisticalHypothesisTab, database)
        self.calibrationTab = calibrationTab(ui.calibrationTab, database=database, cameras=cameras)
    
    def startup(self,):
        self.statisticalHypothesisTab.startup()


class calibrationTab:

    def __init__(self, ui:calibrationTabUI, database: mainDatabase, cameras: dict[str, Camera]) -> None:
        self.ui = ui
        self.database = database
        self.cameras = cameras
        
        self.calibration_flag = False
        self.particles = []
        self.calib_image = None
        self.detector: particlesDetector.particlesDetector = None
        
        

        self.ui.check_button_connector(self.check_calibration_placement)
        self.ui.start_button_connector(self.start_calibration)
        self.ui.connect_image_mouse_event(self.image_mouse_event)

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
                    
        

    def check_calibration_placement(self,):
        return True
    

    def start_calibration(self,):
        self.calibration_flag = True

        #build detector ----------------------------------------------
        algorithm_data = self.database.setting_db.algorithm_db.load()
        self.detector = particlesDetector.particlesDetector(algorithm_data['threshold'], 0.1, algorithm_data['border'])
        #-------------------------------------------------------------

        for camera in self.cameras.values():
            camera.Operations.start_grabbing()
        

    
    def camera_image_event(self,):
        cam_application = 'standard'
        if self.calibration_flag:
            image = self.cameras[cam_application].image
            image = cv2.imread('backend/Processing/test_imgs/0.png',0)
            
            self.calib_image = image.copy()
            self.particles = self.detector.detect(image, None)

            image = particlesDetector.draw_particles(image, self.particles )
            self.ui.show_live(image)
            self.calibration_flag = False

    

    



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
            sum_p = percents.sum()
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
        
        
        




