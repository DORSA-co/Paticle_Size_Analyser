from typing import Union

from PySide6.QtWidgets import QWidget

from uiFiles.write_signal_hmi_UI import Ui_writeSignalHMI
from uiFiles.read_signal_hmi_UI import Ui_readSignalHMI
from uiUtils.GUIComponents import DraggableWidget
from uiUtils.guiBackend import GUIBackend


        


class InputNodeHMI(DraggableWidget):
    def __init__(self, name: str, dtype:str, parent=None):
        super().__init__(None, parent)        
        self.ui = Ui_readSignalHMI()
        self.ui.setupUi(self)
        
        # Set the object name for drag purposes
        self.setObjectName(name)
        # Use GUIBackend to set the label text
        GUIBackend.set_label_text(self.ui.name_label, str(name))
        # Add the custom widget to the DraggableWidget
        self.addWidget(self.ui.main_frame)

        self.dtype = dtype
        self.name = name

        self.setup_dtype()


    def setup_dtype(self):
        if self.dtype == 'bool':
            GUIBackend.set_wgt_visible(self.ui.numeric_value_indicator, False)
            GUIBackend.set_wgt_visible(self.ui.bool_value_indicator, True)
        else:
            GUIBackend.set_wgt_visible(self.ui.numeric_value_indicator, True)
            GUIBackend.set_wgt_visible(self.ui.bool_value_indicator, False)

    
    

    def set_value(self, val:Union[float, int, bool]):
        if val is None:
            return
        
        if self.dtype == 'bool':
            GUIBackend.set_dynalic_property(self.ui.bool_value_indicator, 'state', bool(val), repolish_style=True)
        
        else:
            val = round(val, 3)
            GUIBackend.set_label_text(self.ui.numeric_value_indicator, str(val))




class outputNodeHMI(DraggableWidget):
    

    def __init__(self, name: str, dtype:str, parent=None):
        super().__init__(None, parent)        
        self.ui = Ui_writeSignalHMI()
        self.ui.setupUi(self)
        
        # Set the object name for drag purposes
        self.setObjectName(name)
        # Use GUIBackend to set the label text
        GUIBackend.set_label_text(self.ui.name_label, str(name))
        # Add the custom widget to the DraggableWidget
        self.addWidget(self.ui.main_frame)
        self.dtype = dtype
        self.name = name

        GUIBackend.set_label_text( self.ui.name_label, str(name))

        self.dtype = dtype
        self.name = name

        self.setup_dtype()


    def setup_dtype(self):
        if self.dtype == 'bool':
            GUIBackend.set_wgt_visible(self.ui.write_bool_value_frame, True)
            GUIBackend.set_wgt_visible(self.ui.numeric_value_input, False)
            
        else:
            GUIBackend.set_wgt_visible(self.ui.write_bool_value_frame, False)
            GUIBackend.set_wgt_visible(self.ui.numeric_value_input, True)


    def get_value(self, ):
        if self.dtype == 'bool':
            return GUIBackend.get_checkbox_value(self.ui.bool_value_input)
        
        else:
            return GUIBackend.get_input(self.ui.numeric_value_input)
        
    
    def set_value(self, value):
        if value is None:
            return
        
        if self.dtype == 'bool':
            return GUIBackend.set_input(self.ui.bool_value_input, value, block_signal=True)
        
        else:
            return GUIBackend.set_input(self.ui.numeric_value_input, value, block_signal=True)
        
    
    def change_connector(self, func):
        if self.dtype == 'bool':
            GUIBackend.checkbox_connector_argument_pass(self.ui.bool_value_input, func, args=(self.name,))
        else:
            GUIBackend.spinbox_connector_argumant_pass(self.ui.numeric_value_input, func, args=(self.name,))