from PagesUI.comparePageUI import comparePageUI
from backend.Processing.Report import Report
from Database.reportsDB import reportFileHandler
from Database.mainDatabase import mainDatabase
from backend.Processing.Compare import Compare
from backend.Utils.datetimeUtils import datetimeFormat

import cv2
import numpy as np
import os


class comparePageAPI:
    
    def __init__(self, ui:comparePageUI, database:mainDatabase):
        self.ui = ui

        self.external_back_event_func = None
        
        self.ui.back_button_connector(self.back)
    



    def set_back_event_func(self,func):
        "connect an external function to back button click event"
        self.external_back_event_func = func

    def set_compare_data(self, compare:Compare):
        
        #hide content and show progressbar
        self.ui.show_page_content(False)
        #progress bar 0
        self.ui.set_progressbar(0)

        self.compare = compare
        ranges = self.compare.standard['ranges']
        #set selected ranges into table header
        self.ui.set_compare_table_ranges_header(ranges)

        data = []
        samples_count = len(self.compare.samples)
        hists = []
        for i,sample in enumerate(self.compare.samples):
            sample_main_path = sample['path']
            sample_name = sample['name']
            
            sample_date = datetimeFormat.str_to_date( sample['date'])
            sample_time = datetimeFormat.str_to_time( sample['time'])
            sample_datetime = datetimeFormat.combine(sample_date, sample_time)
            rfh = reportFileHandler(main_path=sample_main_path, sample_name=sample_name, date_time=sample_datetime)
            report = rfh.load_report()

            #-------------------------------------------------------------------------
            if report is None:
                self.ui.show_confirm_box("Error", f"Report {sample_name} not exits. it's file maybe deleted", ['ignore'])
            
            #-------------------------------------------------------------------------
            else:
                report.change_standard(compare.standard)
            
                hist = list(report.Grading.get_hist())
                hists.append(hist)
                table_record = [sample_name, sample['date'], sample['time'] ] + hist
                data.append( table_record )

            #--------------------------------------------------
            percent =  ( i + 1 )/samples_count * 100 
            self.ui.set_progressbar(percent)
            #--------------------------------------------------
        if len(hists)!=0:
            hists = np.array( hists )
            hists_mean = np.round(np.mean( hists, axis=0), 0 )

            self.ui.set_compare_table(data)
            self.ui.set_total_mean_table(hists_mean)
            self.ui.show_page_content(True)
            


    def back(self, ):
        """this function call when back button clicked
        """
        if self.external_back_event_func is not None:
            self.external_back_event_func('reports')


    