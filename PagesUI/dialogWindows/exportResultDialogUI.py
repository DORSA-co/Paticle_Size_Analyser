
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat


class exportResultDialogUI:
    ui_path = 'uiFiles\\export_result.ui'
    

    def __init__(self, parent=None) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path, parent=parent)

        self.massage_lbl = self.ui.message_lbl
        self.wrong_codes = self.ui.wrong_codes_text_edit
        self.n_wrong_codes = self.ui.wrong_count_lbl
        self.exception_error = self.ui.exception_error
        self.exception_frame = self.ui.exception_frame
        self.wrong_codes_frame = self.ui.wrong_codes_frame

        GUIBackend.set_win_frameless(self.ui)

    def set_massage(self, txt:str):
        GUIBackend.set_label_text(self.massage_lbl, txt)
    
    def set_wrong_codes(self, wrong_codes:list[str]):
        GUIBackend.set_label_text(self.n_wrong_codes, str(len(wrong_codes)))
        if len(wrong_codes):
            txt = ', '.join(wrong_codes)
            GUIBackend.set_wgt_visible(self.wrong_codes_frame, True)
            GUIBackend.set_textarea_text(self.wrong_codes, txt)
        else:
            GUIBackend.set_wgt_visible(self.wrong_codes_frame, False)
        
        #GUIBackend.adjustsize(self.wrong_codes_frame)
        GUIBackend.adjustsize(self.ui)

    def set_exception_msg(self, e):
        if e is None:
            GUIBackend.set_wgt_visible(self.exception_frame, False)
        else:
            e = str(e)
            GUIBackend.set_wgt_visible(self.exception_frame, True)
            GUIBackend.set_textarea_text(self.exception_error, e)

        #GUIBackend.adjustsize(self.exception_frame)
        GUIBackend.adjustsize(self.ui)

    def show(self,):
        GUIBackend.show_window(self.ui, True)
    
    def close(self):
        GUIBackend.close_window(self.ui)