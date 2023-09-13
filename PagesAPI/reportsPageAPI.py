from PagesUI.reportsPageUI import reportsPageUI
from backend.Processing.Report import Report
from backend.Processing.Grading import Grading
from Database.mainDatabase  import mainDatabase
from Database.reportsDB import reportFileHandler
from backend.Processing.Compare import Compare
from backend.Rebuild.rebuidReport import rebuildReport
import cv2
from datetime import datetime, date
import threading
import numpy as np

class reportsPageAPI:   
    FILTER_THREAD_COUNT = 5 
    MIN_SAMPLE_COUNT_THREADING = 50
    def __init__(self, ui:reportsPageUI, database:mainDatabase):
        self.ui = ui
        self.database = database

        self.see_report_event_func = None
        self.compare_event_func = None
        self.logined_username = ''

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
        self.ui.rebuild_btn_connector(self.rebuild_reports)
        self.startup()


        
        
        
        

    
    def startup(self,):
        """this function called from main_API when corespond page loaded
        """
        #show rebuild if user login
        if self.logined_username != '':
            self.check_rebuild()
        
        self.set_standards()
        self.load_all_samples()

    
    def set_user_login(self, username):
        self.logined_username = username
    

    def check_rebuild(self,):
        history = self.database.standards_db.standardsHistoryTemp.get_history()
        self.rebuilder = rebuildReport(history.copy())
        all_samples = self.database.reports_db.load_all()
        if self.rebuilder.is_need(all_samples):
                self.ui.show_rebuild_win()
        else:
            self.database.standards_db.standardsHistoryTemp.remove_history()
    

    def rebuild_reports(self):
        all_samples = self.database.reports_db.load_all()
        total_count = len(all_samples)

        for i in range(total_count):
            rfh = reportFileHandler(all_samples[i])
            report = rfh.load_report()
            #rebuild sample and report base on standard changes
            new_sample_record, new_report = self.rebuilder.rebuild(all_samples[i], report)
            #if new_sample_record be None, no rebuid done
            if new_sample_record is not None:
                self.database.reports_db.update(new_sample_record)
                rfh.save_report(new_report)

            percent = (i+1) / total_count * 100
            self.ui.set_rebuild_progress_bar( percent )

        self.database.standards_db.standardsHistoryTemp.remove_history()
        del(self.rebuilder)
        self.load_all_samples()
        self.ui.enable_rebuild_win_close()
        


    def load_all_samples(self,):
        all_records = self.database.reports_db.load_all()
        self.ui.set_samples_table(all_records)

    
    def set_standards(self,):
        standards = self.database.standards_db.load_all()
        standards_name = list(map( lambda x:x['name'], standards))

        self.ui.set_standards_filter_table_data(standards_name)
        self.ui.set_compare_standards_items(standards_name)
        self.ui.set_ranges_filter_standards(standards_name, standards)
        

    
    def apply_filters(self,):
        self.ui.set_select_all_samples(False)
        self.ui.get_standards_filter()
        all_samples = self.database.reports_db.load_all()
        filter_func = self.generate_filter()
        self.filterd_samples = []
        
        samples_count = len(all_samples)
        batch_size = int( np.ceil(samples_count / self.FILTER_THREAD_COUNT))
        

        #start by threading
        if samples_count > self.MIN_SAMPLE_COUNT_THREADING:
            threads = []
            for i in range(self.FILTER_THREAD_COUNT):
                threads.append(
                    threading.Thread( 
                        target=self.__filter_loop__, args=(all_samples[i*batch_size:(i+1)*batch_size], filter_func)
                    )
                )

                threads[-1].start()

            for i in range(self.FILTER_THREAD_COUNT):
                threads[i].join()
        #start without threading  
        else:
            self.__filter_loop__(all_samples, filter_func)

        
        self.ui.set_samples_table(self.filterd_samples)
        self.filterd_samples.clear()
    

    def __filter_loop__(self,batch_samples, filter_func):
        for sample in batch_samples:
            if filter_func(sample):
                self.filterd_samples.append(sample)
        
        
        #
    
    def generate_filter(self, ):
        
        active_filters = self.ui.get_active_filters()
        name = self.ui.get_name_filter()
        username = self.ui.get_username_filter()
        start_date, end_date = self.ui.get_date_filter()
        standards_name = self.ui.get_standards_filter()
        ranges_conditions, range_filter_standard_name = self.ui.get_ranges_filter()
        
        if 'ranges' in active_filters:
            range_filter_standard = self.database.standards_db.load(range_filter_standard_name)
            
            
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
                #-----------------------------------------------------------------------------
                # if sample['standard'] != range_filter_standard_name:
                #     return False
                
                # sample_grading_result = sample['grading_result']
                
                #-----------------------------------------------------------------------------
                #WHIT CALCULATION
                #-----------------------------------------------------------------------------
                # grading.clear()
                # grading.append(sample['max_radiuses'])
                # sample_grading_result = grading.get_hist()
                rfh = reportFileHandler(sample)
                report = rfh.load_report()
                report.change_standard(range_filter_standard)
                sample_grading_result = report.Grading.get_hist()
                #-----------------------------------------------------------------------------

                for i in range(len(ranges_conditions)):
                    operator = ranges_conditions[i]['operator']
                    value = ranges_conditions[i]['input']
                    real_value = sample_grading_result[i]

                    if not self.operations_condition[operator](real_value, value):
                        return False

            
            return flag
        return func

    def see_report(self, sample:dict):
        
        rfh = reportFileHandler(sample)
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
        standard = self.database.standards_db.load(standard_name)

        compare = Compare(samples, standard)

        self.compare_event_func(compare)

        
        
    def delete_sample(self, sample):

        state = self.ui.show_confirm_box(title='Delete Sample', 
                                 massage='Are you Sure delete sample?',
                                 buttons=['yes', 'cancel'])
        
        if state == 'cancel':
            return
        
        rfh = reportFileHandler(sample)
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
            rfh = reportFileHandler(sample)
            rfh.remove()
            self.database.reports_db.remove(sample)

        self.load_all_samples()

