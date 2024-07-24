from PySide6.QtWidgets import QWidget

from uiFiles.output_signal_setting_UI import Ui_outputSignalSetting
from uiFiles.input_signal_setting_UI import Ui_inputSignalSetting
from uiUtils.guiBackend import GUIBackend
from backend.Utils.mapDictionary import mapDictionary

class inputSignalUI(QWidget):

    def __init__(self, step_name: str) -> None:
        super().__init__()
        self.ui = Ui_inputSignalSetting()
        self.ui.setupUi(self)

        self.step_name = step_name

        self.mapDict = mapDictionary(
            {"cond": {
                        'true':'be True',
                        'false':'be False',
                        '>': '>',
                        '=': '=',
                        '<': '<',
                     },
             }
        )

        self.settings = {
            'name': self.ui.signal_name_combobox,
            'condition': self.ui.condition_combobox,
            'value': self.ui.signal_value
        }

        GUIBackend.connector(self.settings['condition'], self.__condition_change_event)
        self.__setup()

    def __setup(self,):
        items = self.mapDict.get_values('cond')
        GUIBackend.set_combobox_items(self.settings['condition'], items)

    
    def __condition_change_event(self,):
        cond_front = GUIBackend.get_input(self.settings['condition'])
        cond_backend = self.mapDict.value2key('cond', cond_front)
        if cond_backend in ['true', 'false']:
            GUIBackend.set_wgt_visible(self.settings['value'], False)
        else:
            GUIBackend.set_wgt_visible(self.settings['value'], True)


    def remove_button_connector(self,func):
        GUIBackend.button_connector_argument_pass(self.ui.remove_btn, func, args=(self,) )

    def get_settings(self,) ->dict:
        res = {}
        for name, field in self.settings.items():
            value = GUIBackend.get_input(field)
            if name == 'condition':
                value = self.mapDict.value2key('cond', value)
            res[name] = value
        return res

    def set_settings(self, data:dict):
        for name, value in data.items():
            if name == 'condition':
                value = self.mapDict.key2value('cond', value)
            GUIBackend.set_input(self.settings[name], value)

    def set_signals_items(self, items:list[str]):
        current = GUIBackend.get_combobox_selected(self.settings['name'])
        GUIBackend.set_combobox_items(self.settings['name'], items)
        GUIBackend.set_combobox_current_item(self.settings['name'], current, block_signal=True)


class outputSignalUI(QWidget):

    def __init__(self, step_name: str) -> None:
        super().__init__()
        self.ui = Ui_outputSignalSetting()
        self.ui.setupUi(self)

        self.mapDict = mapDictionary(
            {"bool_value": {
                        'true':'True',
                        'false':'False',
                     },

             "type": {
                 'numeric': 'Numeric',
                 'bool': 'Boolean',
             }
             }
        )

        self.step_name = step_name
        self.settings = {
            'name': self.ui.signal_name_combobox,
            'value': self.ui.value_bool,
            'type': self.ui.signal_type
        }
        
        GUIBackend.connector(self.settings['type'], self.__type_change_event)
        self.__setup()

    def __setup(self,):
        items = self.mapDict.get_values('type')
        GUIBackend.set_combobox_items(self.settings['type'], items)

        items = self.mapDict.get_values('bool_value')
        GUIBackend.set_combobox_items(self.ui.value_bool, items)
    
    
    def __type_change_event(self,):
        type_front = GUIBackend.get_input(self.settings['type'])
        type_backend = self.mapDict.value2key('type', type_front)

        if type_backend == 'bool':
            self.settings['value'] = self.ui.value_bool
            GUIBackend.set_wgt_visible(self.ui.value_numeric, False )
            GUIBackend.set_wgt_visible(self.ui.value_bool, True )
        
        elif type_backend == 'numeric':
            self.settings['value'] = self.ui.value_numeric
            GUIBackend.set_wgt_visible(self.ui.value_numeric, True )
            GUIBackend.set_wgt_visible(self.ui.value_bool, False )
            


    def remove_button_connector(self,func):
        GUIBackend.button_connector_argument_pass(self.ui.remove_btn, func, args=(self, ) )


    def get_settings(self,) ->dict:
        res = {}
        value = GUIBackend.get_input(self.settings['name'])
        res['name'] = value

        value = GUIBackend.get_input(self.settings['type'])
        value = self.mapDict.value2key('type', value)
        res['type'] = value

        value = GUIBackend.get_input(self.settings['value'])
        if res['type'] == 'bool':
            value = self.mapDict.value2key('bool_value', value)
        res['value'] = value

        return res


    def set_settings(self, data:dict):
        
        GUIBackend.set_input(self.settings['name'], data['name'])

        value = data['type']
        value = self.mapDict.key2value('type', value)
        GUIBackend.set_input(self.settings['type'], value)
        self.__type_change_event()

        value = data['value']
        if data['type'] == 'bool':
            value = self.mapDict.key2value('bool_value', value)
        GUIBackend.set_input(self.settings['value'], value)

        
        


    def set_signals_items(self, items:list[str]):
        current = GUIBackend.get_combobox_selected(self.settings['name'])
        GUIBackend.set_combobox_items(self.settings['name'], items)
        GUIBackend.set_combobox_current_item(self.settings['name'], current, block_signal=True)