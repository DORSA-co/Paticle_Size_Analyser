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
from PagesUI.sectionsUI.nodeHMIUI import InputNodeHMI, outputNodeHMI
from backend.Utils.mapDictionary import mapDictionary
from backend.Utils.idList import idList
from uiUtils.GUIComponents import DragableScrollArea



class hmiPageUI:
    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui
        
        self.signals = idList()

        self.singals_scroll_area:dict[str, DragableScrollArea] = {
            'input': DragableScrollArea(self.ui.hmi_input_section_frame),
            'output': DragableScrollArea(self.ui.hmi_output_section_frame)

        }
        
        self.__setup_scroll_area()
        self.__external_changed_node_event_func = None
        self.input_nodes = idList()
        self.output_nodes = idList()


    
        


    def __setup_scroll_area(self,):
        GUIBackend.add_widget(self.ui.hmi_input_section_frame, self.singals_scroll_area['input'])
        GUIBackend.add_widget(self.ui.hmi_output_section_frame, self.singals_scroll_area['output'])

        # for scroll_area in self.singals_scroll_area.values():
        #     scroll_area.add

    def connect_change_output_node(self, func):
        self.__external_changed_node_event_func = func
        
    def set_nodes_enable(self, flag):
        GUIBackend.set_disable_enable(self.ui.hmi_nodes_frame, flag)

    def write_message(self, txt):
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.hmi_page_error_label, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.hmi_page_error_label, True)
            GUIBackend.set_label_text(self.ui.hmi_page_error_label, str(txt))


    def add_node(self, node_info:dict):
        assert self.__external_changed_node_event_func is not None, "connect_change_output_node first then call add_node"
        
        if node_info['type'] == 'readable':
            su = InputNodeHMI(
                            name = node_info['name'],
                            dtype= node_info['data_type']
            )    

            self.singals_scroll_area['input'].content_widget.addWidget(su)
            self.input_nodes.append(su, su.name)

            



        elif node_info['type'] == 'writeable':
            su = outputNodeHMI(
                            name = node_info['name'],
                            dtype= node_info['data_type']
            )    

            su.change_connector(self.__external_changed_node_event_func)
            self.singals_scroll_area['output'].content_widget.addWidget(su)

            self.output_nodes.append(su, su.name)




    def set_input_node_value(self, name:str, value):
        su:InputNodeHMI = self.input_nodes.get_by_id(name)
        if su is not None:
            su.set_value(value)