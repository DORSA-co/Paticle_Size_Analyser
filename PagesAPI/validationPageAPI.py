import numpy as np

import Constants.CONSTANTS as CONSTANTS
from PagesUI.validationPageUI import validationPageUI, statisticalHypothesisTab, calibrationTabUI, testSectionUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
from backend.Processing.Report import Report
from backend.Calibration.testsValidation import weightDifferenceValidation, tTestValidation

storage_path = 'data/'

class validationPageAPI:

    def __init__(self, ui:validationPageUI, database:mainDatabase, ):
        self.statisticalHypothesisTab = statisticalHypothesisTabAPI(ui.statisticalHypothesisTab, database)
    
    def startup(self,):
        self.statisticalHypothesisTab.startup()






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
        
        
        




