from PySide6.QtWidgets import QWidget

from uiFiles.node_setting_UI import Ui_NodeSetting
from uiUtils.guiBackend import GUIBackend


class nodeSettinUI(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_NodeSetting()
        self.ui.setupUi(self)
        self.settings = {
            'name': self.ui.node_name_input,
            'type': self.ui.node_type_combobox,
            'ns'  : self.ui.node_ns,
            'i'   : self.ui.node_i,

        }

        

    def remove_button_connector(self,func):
        GUIBackend.button_connector_argument_pass(self.ui.remove_btn, func, args=(self,) )

    def change_setting_connector(self, func):
        for setting_name in self.settings.keys():
            GUIBackend.connector(self.settings[setting_name], 
                                                      func, 
                                                      )

    def get_settings(self,) -> dict:
        res = {}
        for setting_name in self.settings.keys():
            res[setting_name] = GUIBackend.get_input(self.settings[setting_name])
        
        return res
    
    def set_settings(self, data:dict):
        for setting_name in self.settings.keys():
            GUIBackend.set_input(self.settings[setting_name], data[setting_name])

