
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat
from Constants import CONSTANTS

class manualRebuildDialogUI:
    ui_path = 'uiFiles\\single_rebuild_manual.ui'
    

    def __init__(self) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path)
        self.buttons = {
            'rebuild': self.ui.rebuild_btn,
            'close': self.ui.close_btn,
            'finish': self.ui.finish_btn
        }

        GUIBackend.button_connector(self.buttons['close'], self.close)
        GUIBackend.button_connector(self.buttons['finish'], self.close)
        GUIBackend.set_win_frameless(self.ui)


    def set_standards_items(self, standards:list[str]):
        GUIBackend.set_combobox_items(self.ui.standards_combobox, standards)

    def set_current_standard(self, stanndard_name:str):
        GUIBackend.set_combobox_current_item(self.ui.standards_combobox, stanndard_name)


    def set_grading_parm_items(self, grading_parms:list[str]):
        GUIBackend.set_combobox_items(self.ui.grading_parm_combobox, grading_parms)

    def set_current_grading_parm(self, grading_parm:str):
        for key, value in CONSTANTS.Sample.GRADING_PARMS.items():
            if value == grading_parm:
                GUIBackend.set_combobox_current_item(self.ui.grading_parm_combobox, key)

    
    def get_settings(self,) -> dict:
        info = {}
        info['standard_name']  = GUIBackend.get_combobox_selected(self.ui.standards_combobox)
    
        name =  GUIBackend.get_combobox_selected(self.ui.grading_parm_combobox)
        info['grading_parm']  = CONSTANTS.Sample.GRADING_PARMS[name]

        return info


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
        GUIBackend.set_stack_widget_idx(self.ui.pages , 0)
        GUIBackend.show_window(self.ui, True)

    def go_to_finish(self,):
        GUIBackend.set_stack_widget_idx(self.ui.pages , 1)

    
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