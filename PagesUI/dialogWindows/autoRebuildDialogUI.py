
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat


class autoRebuildDialogUI:
    ui_path = 'uiFiles\\rebuild.ui'
    

    def __init__(self) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path)
        self.buttons = {
            'rebuild': self.ui.rebuild_btn,
            'close': self.ui.close_btn,
        }


        GUIBackend.set_win_frameless(self.ui)



    def set_massage(self, txt:str, is_error=False ):
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.massage_lbl, False)
            
            
        else:
            GUIBackend.set_wgt_visible(self.ui.massage_lbl, True)
            if is_error:
                GUIBackend.set_style(self.ui.massage_lbl, "color:rgb(197, 63, 59);")
            else:
                GUIBackend.set_style(self.ui.massage_lbl, "color:rgb(41, 147, 108);")

            GUIBackend.set_label_text(self.ui.massage_lbl, txt)
    

    def show(self,):
        self.set_progress_bar(0)
        self.set_massage(None)
        GUIBackend.show_window(self.ui, True)

    
    def button_connector(self, btn_name, func):
        GUIBackend.button_connector(self.buttons[btn_name], func)

    def set_progress_bar(self, value):
        value = int(value)
        GUIBackend.set_progressbar_value(self.ui.converting_progressbar, value)

    def enable_buttons(self,btn_name, status):
        GUIBackend.set_disable_enable(self.buttons[btn_name], status)
    
    def close(self):
        GUIBackend.close_window(self.ui)

    def hide(self,):
        GUIBackend.hide_window(self.ui)