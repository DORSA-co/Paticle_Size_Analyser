from PySide6.QtWidgets import QWidget

from uiFiles.node_setting_UI import Ui_NodeSetting
from uiUtils.guiBackend import GUIBackend
from backend.Utils.mapDictionary import mapDictionary

class nodeSettinUI(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_NodeSetting()
        self.ui.setupUi(self)
        self.settings = {
            'name': self.ui.node_name_input,
            'type': self.ui.node_type_combobox,
            'data_type' : self.ui.node_datatype_combobox,
            'ns'  : self.ui.node_ns,
            'i'   : self.ui.node_i,

        }

        self.map_dict = mapDictionary(
             {
                'data_type': {'bool':'Boolean', 
                              'numeric': 'Numeric'},

                'type': {'writeable': 'Writeable',
                         'readable': 'Readable'}
            }
        )

        GUIBackend.set_combobox_items(self.settings['type'], self.map_dict.get_values('type'))
        GUIBackend.set_combobox_items(self.settings['data_type'], self.map_dict.get_values('data_type'))


        

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
            value = GUIBackend.get_input(self.settings[setting_name])
            if   setting_name == 'type':
                value = self.map_dict.value2key('type', value)

            elif setting_name == 'data_type':
                value = self.map_dict.value2key('data_type', value)

            res[setting_name] = value
        
        return res
    
    def set_settings(self, data:dict):
        for setting_name in self.settings.keys():
            value = data[setting_name]

            if   setting_name == 'type':
                value = self.map_dict.key2value('type', value)

            elif setting_name == 'data_type':
                value = self.map_dict.key2value('data_type', value)

            GUIBackend.set_input(self.settings[setting_name], value )

