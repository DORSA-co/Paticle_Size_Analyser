
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from uiUtils import Charts
import cv2


class comparePageUI:
    
    def __init__(self, ui,):
        self.ui = ui
        self.back_btn = self.ui.comparepage_back_btn
        self.compare_table = self.ui.comparepage_compare_table
        self.total_mean_table = self.ui.comparepage_compare_mean_table
        self.progressbar = self.ui.comparepage_progressbar
        

        self.compare_table_headrs = ['name', 'date', 'time']
        GUIBackend.set_table_dim(self.total_mean_table,row=1, col=None)




    def back_button_connector(self, func):
        GUIBackend.button_connector(self.back_btn, func)

    def set_compare_table_ranges_header(self, ranges):

        ranges_str = list(map( lambda x:f"{x[0]}mm - {x[1]}mm", ranges))
        self.ranges_str = ranges_str
        headers = self.compare_table_headrs + ranges_str
        GUIBackend.set_table_dim(self.compare_table,
                                 row=None,
                                 col=len(headers))
        
        GUIBackend.set_table_dim(self.total_mean_table,
                                 row=None,
                                 col=len(ranges_str))
        
        GUIBackend.set_table_cheaders( self.compare_table,
                                       headers
                                      )
        
        GUIBackend.set_table_cheaders( self.total_mean_table,
                                       ranges_str
                                      )


    def set_compare_table(self, data: list[list]):

        GUIBackend.set_table_dim(self.compare_table, row=len(data), col=None)
        start_ranges_idx = len(self.compare_table_headrs) 
        end_ranges_idx = len(self.compare_table_headrs + self.ranges_str)
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                if start_ranges_idx<=col_idx< end_ranges_idx:
                    value = str(value) + ' %'
                
                GUIBackend.set_table_cell_value(self.compare_table, (row_idx, col_idx), value)


    
    def set_total_mean_table(self, data: list[list]):

        for col_idx, value in enumerate(data):
                value = str(value) + ' %'
                GUIBackend.set_table_cell_value(self.total_mean_table, (0, col_idx), value)
            

    def set_progressbar(self, value:int):
        GUIBackend.set_progressbar_value(self.progressbar, value)

    
    def show_page_content(self, show:bool):
        if show:
            GUIBackend.set_max_size(self.ui.compareScrollAreaWidget, h=16777215)
            GUIBackend.set_max_size(self.progressbar, h=0)
        
        else:
            GUIBackend.set_max_size(self.ui.compareScrollAreaWidget, h=0)
            GUIBackend.set_max_size(self.progressbar, h=100)



    def show_confirm_box(Self, title, massage, buttons):
        cmb = GUIComponents.confirmMessageBox(title, massage, buttons = buttons)
        return cmb.render()