import CONSTANTS
from PagesUI.validationPageUI import validationPageUI, statisticalHypothesisTab, calibrationTabUI, testSectionUI
from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler
from backend.Processing.Report import Report


storage_path = 'data/'

class validationPageAPI:

    def __init__(self, ui:validationPageUI, database:mainDatabase, ):
        self.statisticalHypothesisTab = statisticalHypothesisTabAPI(ui.statisticalHypothesisTab, database)
    
    def startup(self,):
        self.statisticalHypothesisTab.startup()






class statisticalHypothesisTabAPI:

    def __init__(self, ui:statisticalHypothesisTab, database:mainDatabase, ):
        self.ui = ui
        self.database = database

        self.test_section_idx = 0
        
        
        for i in range(self.ui.MAX_TEST_COUNT):
            test_section = self.ui.get_test_section(i)
            test_section.load_button_connector(self.test_section_load_sample)
        
        self.ui.sampleLoader.sample_button_connector(self.load_selected_sample)
        


    def test_section_load_sample(self, test_idx:int):
        """this function calls when user click on load sample button of any test section in validation Tab

        Args:
            test_idx (int): index of the test section that it's button clicked
        """
        self.test_section_idx = test_idx
        self.ui.sampleLoader.show_samples(self.database.reports_db.load_all())
        self.ui.sampleLoader.show()
        

    def load_selected_sample(self, sample):
        standard = self.database.standards_db.load(sample['standard'])

        test_section = self.ui.get_test_section(self.test_section_idx)
        test_section.set_sample(sample, standard['ranges'])
        self.ui.sampleLoader.close()
        


    def startup(self,):
        self.load_standards()


    def load_standards(self,):
        standards_name = self.database.standards_db.load_standards_name()
        self.ui.set_standards_list(standards_name)


    





