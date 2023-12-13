
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat
from Constants import CONSTANTS

class sampleInfoDialogUI:
    ui_path = 'uiFiles\\sample_info.ui'
    

    def __init__(self) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path)
        self.buttons = {
            'cancel': self.ui.cancel_btn,
            'run': self.ui.run_btn
        }

        GUIBackend.button_connector(self.buttons['cancel'], self.close)
        GUIBackend.set_win_frameless(self.ui)


    def set_standards_items(self, standards:list[str]):
        GUIBackend.set_combobox_items(self.ui.standards_name_combobox, standards)

    def set_current_standard(self, stanndard_name:str):
        GUIBackend.set_combobox_current_item(self.ui.standards_name_combobox, stanndard_name)


    def set_grading_parm_items(self, grading_parms:list[str]):
        GUIBackend.set_combobox_items(self.ui.grading_parm_combobox, grading_parms)

    def set_current_grading_parm(self, grading_parm:str):
        for key, value in CONSTANTS.Sample.GRADING_PARMS.items():
            if value == grading_parm:
                GUIBackend.set_combobox_current_item(self.ui.grading_parm_combobox, key)

    def set_sample_name(self, name:str):
        GUIBackend.set_input(self.ui.sample_name_input, name)

    
    def disable_sample_name(self, flag):
        GUIBackend.set_disable_enable(self.ui.sample_name_input, flag)

    
    def get_info(self, ) -> dict:
        info = {}
        info['name'] = GUIBackend.get_input_text(self.ui.sample_name_input)
        info['standard'] = GUIBackend.get_combobox_selected(self.ui.standards_name_combobox)
        info['grading_parm'] = CONSTANTS.Sample.GRADING_PARMS[ 
            GUIBackend.get_combobox_selected(self.ui.grading_parm_combobox)
                    ]
        info['description'] = GUIBackend.get_textarea_text(self.ui.description_inpt)
        return info
    


    def write_error_massage(self, txt:str):
        """Write Errors message for sample info dialog box

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.error_lbl, True)
            GUIBackend.set_label_text(self.ui.error_lbl, txt)
    

    def show(self,):
        GUIBackend.set_input_text(self.ui.description_inpt,'')
        GUIBackend.show_window(self.ui, True)

    def go_to_finish(self,):
        GUIBackend.set_stack_widget_idx(self.ui.pages , 1)

    
    def button_connector(self, btn_name, func):
        GUIBackend.button_connector(self.buttons[btn_name], func)

    def enable_buttons(self,btn_name, status):
        GUIBackend.set_disable_enable(self.buttons[btn_name], status)
    
    def close(self):
        GUIBackend.close_window(self.ui)
