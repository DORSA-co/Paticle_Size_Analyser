
from uiUtils.guiBackend import GUIBackend
from uiUtils import Charts
import cv2


class comparePageUI:
    
    def __init__(self, ui,):
        self.ui = ui
        self.back_btn = self.ui.comparepage_back_btn
        self.compare_table = self.ui.comparepage_compare_table
        self.progressbar = self.ui.comparepage_progressbar
        

        self.compare_table_headrs = ['name', 'date', 'time']
        

    def back_button_connector(self, func):
        GUIBackend.button_connector(self.back_btn, func)

    def set_compare_table_ranges_header(self, ranges):

        ranges_str = list(map( lambda x:f"{x[0]}mm - {x[1]}mm", ranges))
        headers = self.compare_table_headrs + ranges_str
        GUIBackend.set_table_dim(self.compare_table,
                                 row=None,
                                 col=len(headers))
        
        GUIBackend.set_table_cheaders( self.compare_table,
                                       headers
                                      )
        

    def set_compare_table(self, data: list[list]):

        GUIBackend.set_table_dim(self.compare_table, row=len(data), col=None)

        for row_idx, row in enumerate(data):
            GUIBackend.set_table_row(self.compare_table, row_idx, row)
            

    def set_progressbar(self, value:int):
        GUIBackend.set_progressbar_value(self.progressbar, value)

    
    def show_page_content(self, show:bool):
        if show:
            GUIBackend.set_max_size(self.ui.compareScrollAreaWidget, h=16777215)
            GUIBackend.set_max_size(self.progressbar, h=0)
        
        else:
            GUIBackend.set_max_size(self.ui.compareScrollAreaWidget, h=0)
            GUIBackend.set_max_size(self.progressbar, h=100)
