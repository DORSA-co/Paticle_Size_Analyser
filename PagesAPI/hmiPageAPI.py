import os
import time
import threading

from PagesUI.hmiPageUI import hmiPageUI
from Database.settingDB import settingPLCNodesDB
from backend.PLC.PLCHandler import PLCHandler
from backend.Utils.threadTimer import timerThread

class hmiPageAPI:
    def __init__(self, ui:hmiPageUI ,database:settingPLCNodesDB, plc:PLCHandler):
        self.uiHandler = ui
        self.database = database
        self.plc = plc
        self.nodes = []
        self.__updating = False
        
        self.uiHandler.connect_change_output_node(self.output_node_changed_event)
        self.load_nodes()

    def startup(self,):
        self.__updating = True
        self.handle_error()
        self.send_read_requset()

        

    def endup(self,):
        self.__updating = False
        return True
    

    def handle_error(self,):
        if self.plc is None or not self.plc.is_connect():
            self.uiHandler.write_message("PLC is disconnected!")
            self.uiHandler.set_nodes_enable(False)
        
        else:
            self.uiHandler.write_message(None)
            self.uiHandler.set_nodes_enable(True)

    
    

    def set_plc(self, plc:PLCHandler):
        self.plc = plc
        self.handle_error()
        self.send_read_requset()


    def plc_disconnected_event(self,):
        self.handle_error()


    def send_read_requset(self,):
        nodes_names = list(map(lambda x:x['name'], self.nodes))
        if self.plc is not None and self.plc.is_connect():
            self.plc.send_read_request('hmi_read_nodes', nodes_names, self.update_nodes_values_event)
    
    def update_nodes_values_event(self, values:dict):
        for name, value in values.items():
            self.uiHandler.set_input_node_value(name, value)
            self.uiHandler.set_output_node_value(name, value)


        if self.__updating:
            self.timer_reader = timerThread(1, 0.1, 'hmi_plc_read')
            self.timer_reader.finish_signal.connect(self.send_read_requset)
            threading.Thread(target=self.timer_reader.run_single, daemon=False).start()


    
    def load_nodes(self,):
        self.nodes = self.database.load_all()
        for node in self.nodes:
            self.uiHandler.add_node(node)

    def output_node_changed_event(self, value, name:str):
        if self.plc is not None and self.plc.is_connect():
            self.plc.send_write_request({name:value})

        


