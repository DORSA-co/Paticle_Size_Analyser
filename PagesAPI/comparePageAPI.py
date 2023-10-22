import cv2
import numpy as np
import os


from PagesUI.comparePageUI import comparePageUI
from backend.Processing.Report import Report
from Database.reportsDB import reportFileHandler
from Database.mainDatabase import mainDatabase
from backend.Processing.Compare import Compare


class comparePageAPI:
    
    def __init__(self, ui:comparePageUI, database:mainDatabase):
        self.ui = ui
        self.reports = []
        self.external_back_event_func = None
        self.attribute_dict = {
            'Grading percent': ('percent', '%'),
            'size': ('avrage', 'mm'),
            'std': ('std', 'mm')
        }
        self.compare = None
        
        self.ui.back_button_connector(self.back)
        self.ui.compare_attribute_combo_connector(self.change_attribute)
        self.ui.set_compare_attribute_items(list(self.attribute_dict.keys()))
        self.ui.set_default_compare_attribute('Grading percent')
        

    

    def set_back_event_func(self,func):
        "connect an external function to back button click event"
        self.external_back_event_func = func
    
    def change_attribute(self, atr:str):
        """this method called when compare combobox in ui changed

        Args:
            atr (str): selected attribue in comboboc
        """
        self.set_compare_data(self.compare)

    def set_compare_data(self, compare:Compare = None):
        
        #hide content and show progressbar
        self.ui.show_page_content(False)
        #progress bar 0
        self.ui.set_progressbar(0)
        atr = self.ui.get_compare_attribute()
        attribute_key, attribute_unit =  self.attribute_dict[atr]

        self.compare = compare
        if self.compare is None:
            return
        
        ranges = self.compare.standard['ranges']
        #set selected ranges into table header
        self.ui.set_compare_table_ranges_header(ranges)

        samples_count = len(self.compare.samples)
        data = []
        samples_ranges_data = []
        self.reports = []

        for i,sample in enumerate(self.compare.samples):
            sample_name = sample['name']
            rfh = reportFileHandler(sample)
            report = rfh.load_report()
            self.reports.append(report)

            #-------------------------------------------------------------------------
            if report is None:
                self.ui.show_confirm_box("Error", f"Report {sample_name} not exits. it's file maybe deleted", ['ignore'])
            
            #-------------------------------------------------------------------------
            else:
                report.change_standard(compare.standard)
                ranges_data = report.get_ranges_statistics()
                ranges_data = list(map( lambda x:x[attribute_key], ranges_data))
                samples_ranges_data.append(ranges_data)
                table_record = [sample_name, sample['date'], sample['time'] ] + ranges_data
                data.append( table_record )

            #--------------------------------------------------
            percent =  ( i + 1 )/samples_count * 100 
            self.ui.set_progressbar(percent)
            #--------------------------------------------------
        if len(samples_ranges_data)!=0:
            samples_ranges_data = np.array( samples_ranges_data )
            data_mean = np.round(np.mean( samples_ranges_data, axis=0), 0 )

            self.ui.set_compare_table(data, attribute_unit)
            self.ui.set_total_mean_table(data_mean)
            self.ui.show_page_content(True)
            self.ui.show_trends_chart(samples_ranges_data, compare.standard['ranges'])
            


    def back(self, ):
        """this function call when back button clicked
        """
        if self.external_back_event_func is not None:
            self.external_back_event_func('reports')


    