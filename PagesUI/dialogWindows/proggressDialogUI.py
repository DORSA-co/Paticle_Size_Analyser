
from typing import Any
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat


class proggressDialogUI:
    ui_path = 'uiFiles\\progress.ui'

    def __init__(self, title='',
                       description='',
                       show_info = True,
                       operation_name='') -> None:

        self.ui = GUIBackend.load_ui(self.ui_path)

        self.progressbar = self.ui.progressbar
        self.title_lbl = self.ui.title_lbl
        self.description_lbl = self.ui.description_lbl
        self.progress_operetion_lbl = self.ui.progress_operetion_lbl
        self.progress_frame = self.ui.progress_frame
        self.complete_count_lbl = self.ui.complete_count_lbl
        self.total_count_lbl = self.ui.total_count_lbl

        self.setup(title, description, show_info, operation_name)




    def setup(self, title='',
                       description='',
                       show_info = True,
                       operation_name=''):
        
        
        
        GUIBackend.set_wgt_visible(self.progress_frame, show_info)
        GUIBackend.set_label_text(self.title_lbl, title)
        GUIBackend.set_label_text(self.description_lbl, description)
        GUIBackend.set_label_text(self.title_lbl, title)
        GUIBackend.set_label_text(self.progress_operetion_lbl, operation_name)

    
    

    def set_value(self, n, total=100):
        GUIBackend.set_label_text(self.complete_count_lbl, str(int(n)))
        GUIBackend.set_label_text(self.total_count_lbl, str(total))

        percent = n / total * 100
        GUIBackend.set_progressbar_value(self.progressbar, percent)


    def show(self,):
        GUIBackend.show_window(self.ui, True)
    
    def close(self):
        GUIBackend.close_window(self.ui)

    def hide(self,):
        GUIBackend.hide_window(self.ui)