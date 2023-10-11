
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat


class verficationResultDialogUI:
    ui_path = 'uiFiles\\verfication_result.ui'

    def __init__(self) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path)

        self.test_result = {
            True: self.ui.passed,
            False: self.ui.not_passed,
        }

        self.pages = self.ui.pages
        self.description_lbl = self.ui.description_lbl

        self.info = [
            {
                'sieve_std' : self.ui.sieve_std_lbl,
                'error' : self.ui.error_lbl,
            },
            {

            }
        ]

        
        

    def set_result_status(self, flag:bool):
        if flag:
            GUIBackend.set_wgt_visible(self.test_result[True], True)
            GUIBackend.set_wgt_visible(self.test_result[False], False)
        else:
            GUIBackend.set_wgt_visible(self.test_result[True], False)
            GUIBackend.set_wgt_visible(self.test_result[False], True)

    
    def set_info(self, infos : dict):
        page_idx = GUIBackend.get_stack_widget_idx(self.pages)

        for name , value in infos.items():
            GUIBackend.set_label_text( self.info[page_idx][name], str(value))
    
    def set_page(self, idx):
        GUIBackend.set_stack_widget_idx(self.pages, idx)

    def set_description(self, text:str):
        GUIBackend.set_label_text(self.description_lbl, text)

    def show(self,):
        GUIBackend.show_window(self.ui, True)
    
    def close(self):
        GUIBackend.close_window(self.ui)