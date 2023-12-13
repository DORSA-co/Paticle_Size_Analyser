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
    REPORTS_PER_PAGE = 15

    def __init__(self, uiHandeler:reportsPageUI, database:mainDatabase):
        self.uiHandeler = uiHandeler
        self.database = database

        self.see_report_event_func = None
        self.compare_event_func = None
        self.in_rubuilding_flag = False
        self.logined_username = ''
        self.page_idx = 0
        self.selected_samples = []

        self.operations_condition = {
            '>': lambda real_value, condition_value : real_value > condition_value,
            '<': lambda real_value, condition_value : real_value < condition_value,
            '>=': lambda real_value, condition_value : real_value >= condition_value,
            '<=': lambda real_value, condition_value : real_value <= condition_value,
            '==': lambda real_value, condition_value : real_value == condition_value,
            'none': lambda real_value, condition_value :True
        }


        self.uiHandeler.apply_filter_button_connector(self.apply_filters)
        self.uiHandeler.compare_button_connector(self.compare)
        self.uiHandeler.select_all_checkbox_connector(self.select_all_sample)
        
        self.uiHandeler.delete_selections_button_connector(self.delete_selections)
        self.uiHandeler.set_checkbox_sample_event_func(self.checked_sample)
        self.uiHandeler.set_delete_sample_event_func(self.delete_sample)
        self.uiHandeler.set_see_report_event_func(self.see_report)
        self.uiHandeler.navigation_buttons_connector(self.navigation_pages)
        self.uiHandeler.autoRebuildDialog.button_connector('rebuild', self.rebuild_reports)
        self.uiHandeler.autoRebuildDialog.button_connector('close', self.close_rebild)
        self.uiHandeler.deleteSamplesDialog.cancel_button_connector(self.cancel_removing_samples)
        self.startup()


        
        
        
        

    
    def startup(self,):
        """this function called from main_API when corespond page loaded
        """
        self.page_idx = 0
        self.uiHandeler.popupFrame.show()
        #--------------------------
        t = time.time()
        self.all_samples = self.database.reports_db.load_all()
        print('load all samples: ',time.time() - t)
        #show rebuild if user login
        t = time.time()
        if self.logined_username != '':
            self.check_rebuild()

        print('check rebuild', time.time() - t)
        t = time.time()
        self.set_standards()
        print('set standard', time.time() - t)

        t = time.time()
        self.refresh_table()
        print('refresh table', time.time() - t)

        t = time.time()
        self.uiHandeler.startup()
        print('startup',time.time() - t)
        
        self.navigation_pages('none')
        #--------------------------
        self.uiHandeler.popupFrame.close()
        
    def navigation_pages(self, status):
        self.uiHandeler.popupFrame.show()
        max_page = int(len(self.all_samples) // self.REPORTS_PER_PAGE)
        
        if status == 'next':
            self.page_idx += 1 
            self.page_idx = min(self.page_idx, 
                                max_page)
        
        elif status == 'prev':
            self.page_idx -=1
            self.page_idx = max(0, self.page_idx)
        
        
        self.uiHandeler.set_navigation_enablity(self.page_idx, max_page )
        self.refresh_table()

        self.uiHandeler.popupFrame.close()


    def select_all_sample(self, state):
        if state:
            self.selected_samples = self.all_samples.copy()
        
        else:
            self.selected_samples = []

        self.uiHandeler.select_all_samples(state)



    def refresh_table(self,):
        page_samples = self.all_samples[self.page_idx*self.REPORTS_PER_PAGE:
                                        ( self.page_idx + 1 ) * self.REPORTS_PER_PAGE
                                        ]
        
        self.uiHandeler.set_samples_table(page_samples, self.selected_samples)

    

    
    def set_user_login(self, username):
        self.logined_username = username
    

    def check_rebuild(self,):
        history = self.database.standards_db.standardsHistoryTemp.get_history()
        self.rebuilder = autoRebuildReport(history.copy())
        
        if self.rebuilder.is_need(self.all_samples):
                self.uiHandeler.set_rebuild_status(True)
                self.uiHandeler.autoRebuildDialog.enable_buttons('rebuild', True)
                self.uiHandeler.autoRebuildDialog.enable_buttons('close', False)
                self.uiHandeler.autoRebuildDialog.show()
        else:
            self.uiHandeler.set_rebuild_status(False)
            self.database.standards_db.standardsHistoryTemp.remove_history()
    

    def rebuild_reports(self):
        self.in_rubuilding_flag = True
        self.uiHandeler.autoRebuildDialog.enable_buttons('rebuild', False)

        self.rebuild_worker = rebuildWorker(self.rebuilder, self.all_samples, self.database.reports_db)
        self.thread_rebuild = threading.Thread(target=self.rebuild_worker.rebuild)

        #self.rebuild_worker.moveToThread(self.thread_rebuild)
        #self.thread_rebuild.started.connect(self.rebuild_worker.rebuild)
        self.rebuild_worker.finished.connect(self.rebuild_complete)
        self.rebuild_worker.progressBar.connect(self.uiHandeler.autoRebuildDialog.set_progress_bar)
        #self.rebuild_worker.finished.connect(self.thread_rebuild.quit)
        #self.thread_rebuild.finished.connect(self.thread_rebuild.deleteLater)
        #self.rebuild_worker.finished.connect(self.rebuild_worker.deleteLater)

        self.thread_rebuild.start()
    

    def rebuild_complete(self,):
        self.in_rubuilding_flag = False
        if self.rebuild_worker.complete_success:
            self.database.standards_db.standardsHistoryTemp.remove_history()
            del(self.rebuilder)
            self.uiHandeler.set_rebuild_status(False)
            self.uiHandeler.autoRebuildDialog.set_massage('Rebuld success', is_error=False)
            self.uiHandeler.autoRebuildDialog.enable_buttons('close', True)
            self.uiHandeler.autoRebuildDialog.enable_buttons('rebuild', False)
        
        else:
            self.uiHandeler.autoRebuildDialog.set_massage('Some error happend', is_error=True)
            self.uiHandeler.autoRebuildDialog.enable_buttons('close', True)
            self.uiHandeler.autoRebuildDialog.enable_buttons('rebuild', True)
    
        
        self.refresh_table()

    
    def close_rebild(self,):
        if self.in_rubuilding_flag:
            self.uiHandeler.autoRebuildDialog.hide()
            btn = self.uiHandeler.show_confirm_box('Cancel','Are You Sure to stop rebuilding', ['yes','cancel'])
            if btn == 'cancel':
                self.uiHandeler.autoRebuildDialog.show()
                return 
            self.in_rubuilding_flag = False
            self.rebuild_worker.break_loop()
                
        self.uiHandeler.autoRebuildDialog.close()

    
    def set_standards(self,):
        standards = self.database.standards_db.load_all()
        standards_name = []
        
        if len(standards) > 0:
            standards_name = list(map( lambda x:x['name'], standards))

        self.uiHandeler.set_standards_filter_table_data(standards_name)
        self.uiHandeler.set_compare_standards_items(standards_name)
        self.uiHandeler.set_ranges_filter_standards(standards_name, standards)
        

    
    def apply_filters(self,):
        self.uiHandeler.set_select_all_samples(False)
        self.uiHandeler.get_standards_filter()
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

        
        self.uiHandeler.set_samples_table(self.filterd_samples, self.selected_samples)
        self.filterd_samples.clear()
    

    def __filter_loop__(self,batch_samples, filter_func):
        for sample in batch_samples:
            if filter_func(sample):
                self.filterd_samples.append(sample)
        
    
    def generate_filter(self, ):
        
        active_filters = self.uiHandeler.get_active_filters()
        name = self.uiHandeler.get_name_filter()
        username = self.uiHandeler.get_username_filter()
        start_date, end_date = self.uiHandeler.get_date_filter()
        standards_name = self.uiHandeler.get_standards_filter()
        ranges_conditions, range_filter_standard_name = self.uiHandeler.get_ranges_filter()
        
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
                    report.rebuild(range_filter_standard)
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
            self.uiHandeler.show_confirm_box('Error', "Report File dosen't exit. it may deleted", ['ok'])
        if self.see_report_event_func is not None:
            self.see_report_event_func( report, 'reports')
            
    
    def set_see_report_event_func(self, func):
        self.see_report_event_func = func
    

    def set_compare_event_func(self, func):
        self.compare_event_func = func


    def compare(self,):
        
        if len(self.selected_samples) == 0:
            self.uiHandeler.show_confirm_box("ERROR!", massage="No Sample Selected", buttons=['ok'])
            return
        
        if len(self.selected_samples) == 1:
            self.uiHandeler.show_confirm_box("ERROR!", massage="only one sample selected. Please select at least two samples", buttons=['ok'])
            return
        #get selected standard for compare
        standard_name = self.uiHandeler.get_selected_standard_for_campare()
        standard = self.database.standards_db.load(standard_name)

        compare = Compare(self.selected_samples, standard)

        
        self.compare_event_func(compare)

        
        
    def delete_sample(self, sample):

        state = self.uiHandeler.show_confirm_box(title='Delete Sample', 
                                 massage='Are you Sure delete sample?',
                                 buttons=['yes', 'cancel'])
        
        if state == 'cancel':
            return
        
        rfh = reportFileHandler(sample)
        rfh.remove()
        self.database.reports_db.remove(sample)
        self.all_samples.remove(sample)
        self.selected_samples.remove(sample)
        self.refresh_table()

    def checked_sample(self, sample):
        if sample in self.selected_samples:
            self.selected_samples.remove(sample)
        
        else:
            self.selected_samples.append(sample)


    def delete_selections(self,):
        """this functions calls when user want delete multi sample
           actuly calls when user clicked on delete button on top of table
        """


        if len(self.selected_samples) == 0:
            state = self.uiHandeler.show_confirm_box(title='Delete Sample', 
                                 massage=f'No Sample Selected',
                                 buttons=['ok'])
            return
        
        state = self.uiHandeler.show_confirm_box(title='Delete Sample', 
                                 massage=f'Are you Sure delete {len(self.selected_samples)} samples?',
                                 buttons=['yes', 'cancel'])
        
        if state == 'cancel':
            return
        
        self.uiHandeler.deleteSamplesDialog.show()


        self.remove_worker = removeSamplesWorkder(self.all_samples, 
                                                  self.selected_samples, 
                                                  self.database.reports_db)
        
        self.thread_remove = threading.Thread(target=self.remove_worker.run)

        self.remove_worker.finished.connect(self.uiHandeler.deleteSamplesDialog.close)
        self.remove_worker.finished.connect(self.refresh_table)
        self.remove_worker.progressBar.connect(self.uiHandeler.deleteSamplesDialog.set_delete_progress_value)
        self.thread_remove.start()

    def cancel_removing_samples(self,):
        self.remove_worker.pause(True)
        res = self.uiHandeler.deleteSamplesDialog.show_confirm_massage( title='Cancel Removing',
                                                                text= 'Are you sure cancel the progress?',
                                                                buttons=['yes','no']
        )
        if res == 'yes':
            self.remove_worker.stop()
        else:
            self.remove_worker.pause(False)





class removeSamplesWorkder(QObject):
    progressBar = Signal(int, int)
    finished = Signal()

    def __init__(self, all_samples:list[dict], selection_samples:list[dict], db:reportsDB ) -> None:
        super(removeSamplesWorkder, self).__init__()

        self.selection_samples = selection_samples
        #get all samples list to update it. after finish, remain samples set into table
        self.all_samples = all_samples
        self.db = db
        self.pause_flag = False
        self.stop_flag = False

    def pause(self, status):
        self.pause_flag = status

    def stop(self,):
        self.stop_flag = True

    def run(self,):
        total_count = len(self.selection_samples)
        #for i,sample in enumerate(self.selection_samples):
        i=0
        while self.selection_samples:
    
            if self.stop_flag:
                break

            if self.pause_flag:
                time.sleep(0.02)
                continue


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

            #delay for help to user to cancel soon
            time.sleep(0.3)

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


