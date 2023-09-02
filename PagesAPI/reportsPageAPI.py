from PagesUI.reportsPageUI import reportsPageUI
from backend.Processing.Report import Report
from Database.mainDatabase  import mainDatabase
from Database.reportsDB import reportFileHandler
from backend.Processing.Compare import Compare
import cv2
from datetime import datetime, date

class reportsPageAPI:    
    def __init__(self, ui:reportsPageUI, database:mainDatabase):
        self.ui = ui
        self.database = database

        self.see_report_event_func = None
        self.compare_event_func = None

        self.ui.apply_filter_button_connector(self.apply_filters)
        self.ui.external_see_report_button_connector(self.see_report)
        self.ui.compare_button_connector(self.compare)
        self.ui.set_delete_sample_event_func(self.delete_sample)
        self.startup()
        
        
        

    
    def startup(self,):
        """this function called from main_API when corespond page loaded
        """
        self.set_standards()
        self.load_all_samples()



    def load_all_samples(self,):
        all_records = self.database.reports_db.load_all()
        self.ui.set_samples_table(all_records)

    
    def set_standards(self,):
        standards = self.database.grading_ranges_db.load_all()
        standards_name = list(map( lambda x:x['name'], standards))

        self.ui.set_standards_filter_table_data(standards_name)
        self.ui.set_compare_standards_items(standards_name)
        

    
    def apply_filters(self,):
        self.ui.set_select_all_samples(False)
        self.ui.get_standards_filter()
        all_samples = self.database.reports_db.load_all()
        filter_func = self.generate_filter()
        filterd_samples = []
        for sample in all_samples:
            if filter_func(sample):
                filterd_samples.append(sample)
        
        self.ui.set_samples_table(filterd_samples)
                
    
    def generate_filter(self, ):
        
        active_filters = self.ui.get_active_filters()
        name = self.ui.get_name_filter()
        username = self.ui.get_username_filter()
        start_date, end_date = self.ui.get_date_filter()
        standards_name = self.ui.get_standards_filter()

        def func(sample):
            flag = True
            if 'name' in active_filters:
                if name.lower() not in sample['name'].lower():
                    return False
            
            if 'standards' in active_filters:
                if sample['standard'] not in standards_name and len(standards_name) != 0 :
                    return False
            
            if 'username' in active_filters:
                if sample['username'] is None:
                    return False
                if username.lower() not in sample['username']:
                    return False
                
            if 'date' in active_filters:
                if sample['date'] < start_date or sample['date'] > end_date:
                    return False
            
            return flag
        return func
    

    def see_report(self, sample):
        date_time = datetime.combine(sample['date'], sample['time'])
        rfh = reportFileHandler(main_path=sample['path'], sample_name=sample['name'], date_time=date_time)
        report = rfh.load_report()
        if report is None:
            self.ui.show_confirm_box('Error', "Report File dosen't exit. it may deleted", ['ok'])
        if self.see_report_event_func is not None:
            self.see_report_event_func(report, 'reports')



    
    def set_see_report_event_func(self, func):
        self.see_report_event_func = func
    

    def set_compare_event_func(self, func):
        self.compare_event_func = func


    def compare(self,):
        ids  = self.ui.get_selected_samples()
        if len(ids) == 0:
            self.ui.show_confirm_box("ERROR!", massage="No Sample Selected", buttons=['ok'])
            return
        #load selected sample for compare from database
        samples = self.database.reports_db.load_by_ids(ids)
        #get selected standard for compare
        standard_name = self.ui.get_selected_standard_for_campare()
        standard = self.database.grading_ranges_db.load(standard_name)

        compare = Compare(samples, standard)

        self.compare_event_func(compare)

        
        
    def delete_sample(self, sample):

        state = self.ui.show_confirm_box(title='Delete Sample', 
                                 massage='Are you Sure delete sample?',
                                 buttons=['yes', 'cancel'])
        
        if state == 'cancel':
            return
        date_time = datetime.combine(sample['date'], sample['time'])
        rfh = reportFileHandler(main_path=sample['path'], sample_name=sample['name'], date_time=date_time)
        rfh.remove()
        self.database.reports_db.remove(sample)

        self.load_all_samples()

        