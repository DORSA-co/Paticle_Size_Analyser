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

        self.operations_condition = {
            '>': lambda real_value, condition_value : real_value > condition_value,
            '<': lambda real_value, condition_value : real_value < condition_value,
            '>=': lambda real_value, condition_value : real_value >= condition_value,
            '<=': lambda real_value, condition_value : real_value <= condition_value,
            '==': lambda real_value, condition_value : real_value == condition_value,
            'none': lambda real_value, condition_value :True
        }


        self.ui.apply_filter_button_connector(self.apply_filters)
        self.ui.external_see_report_button_connector(self.see_report)
        self.ui.compare_button_connector(self.compare)
        self.ui.set_delete_sample_event_func(self.delete_sample)
        self.ui.delete_selections_button_connector(self.delete_selections)
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
        self.ui.set_ranges_filter_standards(standards_name, standards)
        

    
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
        ranges_conditions, range_filter_standard_name = self.ui.get_ranges_filter()

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
            
            if 'ranges' in active_filters:
                if sample['standard'] != range_filter_standard_name:
                    return False
                
                sample_grading_result = sample['grading_result']
                for i in range(len(ranges_conditions)):
                    operator = ranges_conditions[i]['operator']
                    value = ranges_conditions[i]['input']
                    real_value = sample_grading_result[i]

                    if not self.operations_condition[operator](real_value, value):
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
        
        if len(ids) == 1:
            self.ui.show_confirm_box("ERROR!", massage="only one sample selected. Please select at least two samples", buttons=['ok'])
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


    def delete_selections(self,):
        ids  = self.ui.get_selected_samples()

        if len(ids) == 0:
            state = self.ui.show_confirm_box(title='Delete Sample', 
                                 massage=f'No Sample Selected',
                                 buttons=['ok'])
            return
        
        state = self.ui.show_confirm_box(title='Delete Sample', 
                                 massage=f'Are you Sure delete {len(ids)} samples?',
                                 buttons=['yes', 'cancel'])
        
        if state == 'cancel':
            return
        samples = self.database.reports_db.load_by_ids(ids)
        for sample in samples:
            date_time = datetime.combine(sample['date'], sample['time'])
            rfh = reportFileHandler(main_path=sample['path'], sample_name=sample['name'], date_time=date_time)
            rfh.remove()
            self.database.reports_db.remove(sample)

        self.load_all_samples()
        