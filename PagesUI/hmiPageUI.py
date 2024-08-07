from __future__ import annotations
from typing import Union

import numpy as np
from PySide6 import QtWidgets


from uiUtils import GUIComponents
import Constants.CONSTANTS as CONSTANTS
from uiUtils.guiBackend import GUIBackend
from PagesUI.PageUI import commonUI
from uiUtils.IO.Mouse import mouseHandeler
from uiFiles.main_UI_ui import Ui_MainWindow

from PagesUI.sectionsUI.signalHMIUI import InputSignalHMI, outputSignalHMI
from backend.Utils.mapDictionary import mapDictionary
from backend.Utils.idList import idList
from uiUtils.GUIComponents import DragableScrollArea


class hmiPageUI:
    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui

        self.input_scroll_area = DragableScrollArea(self.ui.hmi_input_section_frame)
        GUIBackend.add_widget(self.ui.hmi_input_section_frame, self.input_scroll_area,)

        
        for i in range(5):
            self.input_scroll_area.content_widget.addWidget(InputSignalHMI(str(i)),)
  

    def add_signal(self, signal_type:str, dtype:str):
        pass





