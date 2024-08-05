from PySide6.QtWidgets import QWidget

from uiFiles.output_signal_setting_UI import Ui_outputSignalSetting
from uiFiles.input_signal_setting_UI import Ui_inputSignalSetting
from uiUtils.guiBackend import GUIBackend
from backend.Utils.mapDictionary import mapDictionary


class signalUIParent:
    BOOLEAN_DTYPE = 'bool'
    NUMERIC_DTYPE = 'numeric'
    def __init__(self) -> None:
        self.settings = {}
    

    def signal_name_connector(self, func):
        GUIBackend.combobox_changeg_connector_argument_pass(self.settings['name'], func, args=(self,))


    def set_signals_items(self, items:list[str]):
        current = GUIBackend.get_combobox_selected(self.settings['name'])
        GUIBackend.set_combobox_items(self.settings['name'], items, block_signal=False)
        GUIBackend.set_combobox_current_item(self.settings['name'], current, block_signal=False)


    


class inputSignalUI(QWidget, signalUIParent):
    

    def __init__(self, step_name: str) -> None:
        super().__init__()
        self.ui = Ui_inputSignalSetting()
        self.ui.setupUi(self)

        self.dtype = self.BOOLEAN_DTYPE
        
        self.id = id(self)

        self.step_name = step_name

        self.mapDict = mapDictionary(
            {"cond_bool": {
                        'true':'be True',
                        'false':'be False',
                        },

            "cond_numeric": {
                        '>': '>',
                        '=': '=',
                        '<': '<',
                     },
             }
        )

        self.settings = {
            'name': self.ui.signal_name_combobox,
            'condition': self.ui.condition_combobox,
            'value': self.ui.value_numeric
        }

        

    def set_data_type(self, dtype:str):
        self.dtype = dtype

        if dtype == self.BOOLEAN_DTYPE:
            GUIBackend.set_wgt_visible(self.ui.value_numeric, False )
            GUIBackend.set_combobox_items(self.settings['condition'], self.mapDict.get_values("cond_bool"))
        
        elif dtype == self.NUMERIC_DTYPE:
            GUIBackend.set_wgt_visible(self.ui.value_numeric, True )
            GUIBackend.set_combobox_items(self.settings['condition'], self.mapDict.get_values("cond_numeric"))





    def remove_button_connector(self,func):
        GUIBackend.button_connector_argument_pass(self.ui.remove_btn, func, args=(self,) )

    def get_settings(self,) ->dict:
        res = {}
        res['name'] = GUIBackend.get_input(self.settings['name'])
        res['value'] = GUIBackend.get_input(self.settings['value'])
        res['dtype'] = self.dtype

        cond = GUIBackend.get_input(self.settings['condition'])

        if self.dtype == self.BOOLEAN_DTYPE:
            cond = self.mapDict.value2key('cond_bool', cond)
        else:
            cond = self.mapDict.value2key('cond_numeric', cond)

        res['condition'] = cond

        res['id'] = self.id

        return res

    def set_settings(self, data:dict):
        assert self.dtype is not None, "please set data_type first"
        if data.get('id') is not None:
            self.id = data.pop('id')
        
        GUIBackend.set_input(self.settings['name'], data['name'])
        GUIBackend.set_input(self.settings['value'], data['value'])

        cond = data['condition']
        if self.dtype == self.BOOLEAN_DTYPE:
            cond = self.mapDict.key2value('cond_bool', cond)
        else:
            cond = self.mapDict.key2value('cond_numeric', cond)

        GUIBackend.set_input(self.settings['condition'], cond)
        

    def set_indicator_value(self, value):
        value = f'Value: {value}'
        GUIBackend.set_label_text(self.ui.value_indicator, str(value))

    def set_online_state(self, state:str):
        GUIBackend.set_dynalic_property(self.ui.main_frame, 'state', state , repolish_style=True)




class outputSignalUI(QWidget, signalUIParent):

    def __init__(self, step_name: str,) -> None:
        super().__init__()
        self.ui = Ui_outputSignalSetting()
        self.ui.setupUi(self)

        self.dtype = 'bool'

        self.id = id(self)

        self.mapDict = mapDictionary(
            {"bool_value": {
                        'true':'True',
                        'false':'False',
                     },

            #  "type": {
            #      'numeric': 'Numeric',
            #      'bool': 'Boolean',
            #  }
             }
        )

        self.step_name = step_name
        self.settings = {
            'name': self.ui.signal_name_combobox,
            'value': self.ui.value_bool,
        }
        
        # self.__setup()


    
    
    # def __type_change_event(self,):
    def set_data_type(self, dtype:str):
        self.dtype = dtype

        if dtype == 'bool':
            self.settings['value'] = self.ui.value_bool
            GUIBackend.set_wgt_visible(self.ui.value_numeric, False )
            GUIBackend.set_wgt_visible(self.ui.value_bool, True )
        
        elif dtype == 'numeric':
            self.settings['value'] = self.ui.value_numeric
            GUIBackend.set_wgt_visible(self.ui.value_numeric, True )
            GUIBackend.set_wgt_visible(self.ui.value_bool, False )
            


    def remove_button_connector(self,func):
        GUIBackend.button_connector_argument_pass(self.ui.remove_btn, func, args=(self, ) )


    def get_settings(self,) ->dict:
        res = {}
        value = GUIBackend.get_input(self.settings['name'])
        res['name'] = value

        res['dtype'] = self.dtype

        value = GUIBackend.get_input(self.settings['value'])

        if self.dtype == self.BOOLEAN_DTYPE:
            value = self.mapDict.value2key('bool_value', value)

        res['value'] = value       
        res['id'] = self.id
        return res


    def set_settings(self, data:dict):
        assert self.dtype is not None, "please set data_type first"

        if data.get('id') is not None:
            self.id = data.pop('id')
        
        GUIBackend.set_input(self.settings['name'], data['name'])

        # value = data['type']
        # value = self.mapDict.key2value('type', value)
        # GUIBackend.set_input(self.settings['type'], value)
        # self.__type_change_event()

        value = data['value']
        if self.dtype == 'bool':
            value = self.mapDict.key2value('bool_value', value)
        GUIBackend.set_input(self.settings['value'], value)

        
        


    