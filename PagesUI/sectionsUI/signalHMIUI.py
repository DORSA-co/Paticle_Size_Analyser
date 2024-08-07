from PySide6.QtWidgets import QWidget

from uiFiles.write_signal_hmi_UI import Ui_writeSignalHMI
from uiFiles.read_signal_hmi_UI import Ui_readSignalHMI
from uiUtils.GUIComponents import DraggableWidget
from uiUtils.guiBackend import GUIBackend


        


class InputSignalHMI(DraggableWidget):
    def __init__(self, name: str, parent=None):
        super().__init__(None, parent)        
        self.ui = Ui_readSignalHMI()
        self.ui.setupUi(self)
        
        # Set the object name for drag purposes
        self.setObjectName(name)

        # Use GUIBackend to set the label text
        GUIBackend.set_label_text(self.ui.name_label, str(name))
        
        # Add the custom widget to the DraggableWidget
        self.addWidget(self.ui.main_frame)




class outputSignalHMI():
    

    def __init__(self, name:str) -> None:
        super().__init__()
        self.ui = Ui_readSignalHMI()
        self.ui.setupUi(self)

        GUIBackend.set_label_text( self.ui.name_label, str(name))

