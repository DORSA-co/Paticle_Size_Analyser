import threading
from datetime import datetime, date

import numpy as np
import cv2
from PySide6.QtCore import QThread, QObject, Signal

from PagesUI.reportsPageUI import reportsPageUI
from backend.Processing.Report import Report
from backend.Processing.Grading import Grading
from Database.mainDatabase  import mainDatabase
from Database.reportsDB import reportFileHandler, reportsDB
from backend.Processing.Compare import Compare
from backend.Rebuild.rebuidReport import autoRebuildReport


import time

class reportsPageAPI:   
    FILTER_THREAD_COUNT = 5 
    MIN_SAMPLE_COUNT_THREADING = 50
    def __init__(self, ui:reportsPageUI, database:mainDatabase):
        self.ui = ui
        self.database = database

        self.see_report_event_func = None
        self.compare_event_func = None
        self.in_rubuilding_flag = False
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
        self.ui.dialogbox_rebuild_btn_connector(self.rebuild_reports)
        self.ui.rebuid_close_button_connector(self.close_rebild)
        self.startup()


        
        
        
        

    
    def startup(self,):
        """this function called from main_API when corespond page loaded
        """
        self.ui.popupFrame.show()
        #--------------------------
        self.all_samples = self.database.reports_db.load_all()
        #show rebuild if user login
        if self.logined_username != '':
            self.check_rebuild()
        
        self.set_standards()
        self.refresh_table()
        self.ui.startup()
        #--------------------------
        self.ui.popupFrame.close()
        
        

    def refresh_table(self,):
        self.ui.set_samples_table(self.all_samples)
    
    def set_user_login(self, username):
        self.logined_username = username
    

    def check_rebuild(self,):
        history = self.database.standards_db.standardsHistoryTemp.get_history()
        self.rebuilder = autoRebuildReport(history.copy())
        
        if self.rebuilder.is_need(self.all_samples):
                self.ui.set_rebuild_status(True)
                self.ui.show_rebuild_win()
        else:
            self.ui.set_rebuild_status(False)
            self.database.standards_db.standardsHistoryTemp.remove_history()
    

    def rebuild_reports(self):
        self.in_rubuilding_flag = True
        self.ui.enable_rebuild_win_buttons('rebuild', False)

        self.rebuild_worker = rebuildWorker(self.rebuilder, self.all_samples, self.database.reports_db)
        self.thread_rebuild = threading.Thread(target=self.rebuild_worker.rebuild)

        #self.rebuild_worker.moveToThread(self.thread_rebuild)
        #self.thread_rebuild.started.connect(self.rebuild_worker.rebuild)
        self.rebuild_worker.finished.connect(self.rebuild_complete)
        self.rebuild_worker.progressBar.connect(self.ui.set_rebuild_progress_bar)
        #self.rebuild_worker.finished.connect(self.thread_rebuild.quit)
        #self.thread_rebuild.finished.connect(self.thread_rebuild.deleteLater)
        #self.rebuild_worker.finished.connect(self.rebuild_worker.deleteLater)

        self.thread_rebuild.start()
    

    def rebuild_complete(self,):
        self.in_rubuilding_flag = False
        if self.rebuild_worker.complete_success:
            self.database.standards_db.standardsHistoryTemp.remove_history()
            del(self.rebuilder)
            self.ui.set_rebuild_status(False)
    
        self.ui.enable_rebuild_win_buttons('rebuild', True)
        self.refresh_table()

    
    def close_rebild(self,):
        if self.in_rubuilding_flag:
            self.ui.hide_rebuild_win()
            btn = self.ui.show_confirm_box('Cancel','Are You Sure to stop rebuilding', ['yes','cancel'])
            if btn == 'cancel':
                self.ui.show_rebuild_win()
                return 
            self.in_rubuilding_flag = False
            self.rebuild_worker.break_loop()
                
        self.ui.close_rebuild_win()


    def load_all_samples(self,):
        all_records = self.database.reports_db.load_all()
        self.ui.set_samples_table(all_records)

    
    def set_standards(self,):
        standards = self.database.standards_db.load_all()
        standards_name = []
        
        if len(standards) > 0:
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
                sample_grading_result = None
                #-----------------------------------------------------------------------------
                if sample['standard'] == range_filter_standard_name:
                    sample_grading_result = sample['grading_result']
                    
                else:
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

    def see_report(self, sample_record:dict):
        
        rfh = reportFileHandler(sample_record)
        report = rfh.load_report()
        if report is None:
            self.ui.show_confirm_box('Error', "Report File dosen't exit. it may deleted", ['ok'])
        if self.see_report_event_func is not None:
            self.see_report_event_func( report, 'reports')
            
    
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
        samples = self.database.reports_db.load_by_name_ids(ids)
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
        self.all_samples.remove(sample)

        self.refresh_table()


    def delete_selections(self,):
        """this functions calls when user want delete multi sample
           actuly calls when user clicked on delete button on top of table
        """
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
        
        self.ui.progessBarDialog.setup('Remove samples','', operation_name='removed')
        self.ui.progessBarDialog.show()
        samples = self.database.reports_db.load_by_name_ids(ids)


        self.worker_remove = removeSamplesWorkder(self.all_samples, samples, self.database.reports_db)
        self.thread_remove = QThread()

        self.worker_remove.moveToThread(self.thread_remove)
        self.thread_remove.started.connect(self.worker_remove.run)
        self.worker_remove.finished.connect(self.ui.progessBarDialog.close)
        self.worker_remove.finished.connect(self.refresh_table)
        self.worker_remove.progressBar.connect(self.ui.progessBarDialog.set_value)
        self.worker_remove.finished.connect(self.thread_remove.quit)
        self.thread_remove.finished.connect(self.thread_remove.deleteLater)
        self.thread_remove.finished.connect(self.worker_remove.deleteLater)
        
        self.thread_remove.start()







class removeSamplesWorkder(QObject):
    progressBar = Signal(int, int)
    finished = Signal()

    def __init__(self, all_samples:list[dict], selection_samples:list[dict], db:reportsDB ) -> None:
        super(removeSamplesWorkder, self).__init__()

        self.selection_samples = selection_samples
        self.all_samples = all_samples
        self.db = db

    def run(self,):
        total_count = len(self.selection_samples)
        #for i,sample in enumerate(self.selection_samples):
        i=0
        while self.selection_samples:
            try:
                rfh = reportFileHandler(self.selection_samples[0])
                rfh.remove()
                self.db.remove(self.selection_samples[0])
                self.all_samples.remove(self.selection_samples[0])
                self.selection_samples.pop(0)
                i+=1
                self.progressBar.emit(i, total_count)
            except Exception as e:
                print(e)

        self.finished.emit()





class rebuildWorker(QObject):
    progressBar = Signal(int)
    finished = Signal()
    
    def __init__(self, rebuilder:autoRebuildReport, samples:list[dict], db:reportsDB) -> None:
        super(rebuildWorker,self).__init__()
        self.db = db
        self.samples = samples
        self.rebuilder = rebuilder
        self.break_flag = False
        self.complete_success = False

    def break_loop(self):
        self.break_flag = True

    def rebuild(self,):

        self.complete_success = False
        total_count = len(self.samples)

        for i in range(total_count):
            if self.break_flag:
                break
            rfh = reportFileHandler(self.samples[i])
            report = rfh.load_report()
            if report is not None:
                #rebuild sample and report base on standard changes
                new_sample_record, new_report = self.rebuilder.rebuild(self.samples[i], report)
                #if new_sample_record be None, no rebuid done
                if new_sample_record is not None:
                    self.samples[i] = new_sample_record
                    self.db.update(new_sample_record)
                    rfh.save_report(new_report)

            percent = int( (i+1) / total_count * 100)
            self.progressBar.emit(percent)
        else:
            self.complete_success = True
            

        self.finished.emit()


