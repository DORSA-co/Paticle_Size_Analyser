import time
import threading

from PySide6.QtCore import QObject, Signal

from backend.Utils.threadTimer import timerThread
from backend.ConfigManager import configFlags
from backend.ConfigManager.Config import Config
from backend.PLC.PLCHandler import PLCHandler

class configManager:

    def __init__(self) -> None:
        self.Config = Config()
        self.plc : PLCHandler = None

        self.start_timer = None
        self.delay_timer = None
        self.stop_timer = None

        self.start_signals_values = {}

        self.start()

        


    def start(self,):
        start_mode = self.Config.get_start_mode()

        if start_mode == configFlags.startMode.timer:
            self.run_start_timer()
        
        elif start_mode == configFlags.startMode.signal_event:
            self.read_start_signals()


    def stop(self, ):
        stop_mode = self.Config.get_stop_mode()

        if stop_mode == configFlags.stopMode.timer:
            self.run_stop_timer()


    def run_start_timer(self, ):
        t = self.Config.get_start_time_cycle()
        self.start_timer = timerThread(t)
        self.start_timer.finish_signal.connect(self.start_timer_finish_event)
        threading.Thread(target=self.start_timer.run_single).start()

    def run_stop_timer(self, t ):
        self.stop_timer = timerThread(t)
        self.stop_timer.finish_signal.connect(self.stop_timer_finish_event)
        threading.Thread(target=self.stop_timer.run_single).start()

    def start_delay_timer(self,):
        t = self.Config.get_start_delay()
        if t == 0:
            self.end_delay_timer()
        else:
            self.delay_timer = timerThread(t)
            self.delay_timer.finish_signal.connect(self.end_delay_timer)
            threading.Thread(target=self.delay_timer.run_single).start()



    def read_start_signals(self, ):
        signals = self.Config.get_start_signals()
        node_names = list(map(lambda x:x['name', signals]))
        self.plc.send_read_request('start_signals', 
                                   node_names,
                                   self.start_signals_update_event)


    def start_signals_update_event(self, values:dict):
        signals_info = self.Config.get_start_signals()
        res, log = self.check_signals(signals_info, values)
        if res:
            self.send_read_permisions_request()

        else:
            timer = timerThread(5)
            timer.finish_signal.connect(self.read_start_signals)
            threading.Thread(target=timer.run_single).start()

    def stop_timer_finish_event(self,):
        pass

    def start_timer_finish_event(self,):
        self.run_start_timer()
        self.send_read_permisions_request()

    def send_read_permisions_request(self,):
        permisions_signals = self.Config.get_permission_signals()
        names = list(map( lambda x:x['name'], permisions_signals))
        if self.plc.is_connect():
            self.plc.send_read_request(request_id='permistions', 
                                       node_names=names, 
                                       answer_func=self.permisions_signal_event)

            
    def permisions_signal_event(self, values:dict):
        signals_info = self.Config.get_permission_signals()
        res, log = self.check_signals(signals_info, values)
        if res:
            if not self.plc.is_connect():
                return
            
            self.write_output_signal('signals1')
            self.start_delay_timer()

    def end_delay_timer(self,):  
        self.write_output_signal('signals2')



    
    def write_output_signal(self, name):
        signals = self.Config.get_output_signals(name)
        nodes_value = self.get_write_signal_dict(signals)
        self.plc.send_write_request(nodes_value)


    def get_write_signal_dict(self, signals:list[dict]) -> dict:
        res = {}
        for signal in signals:
            name = signal['name']
            value = signal['value']
            stype = signal['type']
            if stype == 'bool':
                if value =='true':
                    value = True
                else:
                    value = False
            else:
                value = float(value)

            res[name] = value
        return res


    def check_signals(self, conds:list[dict], values:dict ) -> bool:
        #{'name': 'r1', 'condition': 'true', 'value': 0.0},
        final_res = True
        log = []

        for signal_cond in conds:

            name = signal_cond['name']
            value = values.get(name)    
            res = True
            status = configFlags.signalStatus.ok


            if value is None:
                final_res = False
                res = False
                status = configFlags.signalStatus.none
                
                
            else:                    
                operator = signal_cond['condition']

                if operator == 'true':
                    if isinstance(value, bool):
                        if not value == True:
                            final_res = False
                            res = False
                            status = configFlags.signalStatus.not_pass_condition
                    else:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.wrong_type
                            
                    
                elif operator == 'false':
                    if isinstance(value, bool):
                        if not value == False:
                            final_res = False
                            res = False
                            status = configFlags.signalStatus.not_pass_condition
                    else:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.wrong_type
                            
                
                elif operator == '>':
                    if not value > signal_cond['value']:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.not_pass_condition
                        
                
                elif operator == '<':
                    if not value < signal_cond['value']:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.not_pass_condition
                        

                
                elif operator == '=':
                    if not value == signal_cond['value']:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.not_pass_condition
                        

            log.append(
                    {'name':name, 'result': res, 'status':status}
                )
            
        return final_res, log


        







class signalEventWorer(QObject):
    refresh_signal = Signal(dict)


    def __init__(self, signals_name: list[str]) -> None:
        super().__init__()

        self.signals_name = signals_name

