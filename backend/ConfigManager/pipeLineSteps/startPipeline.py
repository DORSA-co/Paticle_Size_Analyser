import threading

from backend.ConfigManager.Config import Config
from backend.ConfigManager import configFlags
from backend.Utils.threadTimer import timerThread
from backend.PLC.PLCHandler import PLCHandler
from Mediator.mainMediator import Mediator
from backend.ConfigManager.configUtils import configUtils


class startPipeline:

    def __init__(self, config:Config, plc:PLCHandler) -> None:
        self.Config = config
        self.plc = plc
        self.mediator = Mediator()

    
    def run(self,):
        start_mode = self.Config.get_start_mode()

        if start_mode == configFlags.startMode.timer:
            self.run_start_timer()
        
        elif start_mode == configFlags.startMode.signal_event:
            self.read_start_signals()


    
    def run_start_timer(self, ):
        t = self.Config.get_start_time_cycle()
        self.start_timer = timerThread(t)
        self.start_timer.finish_signal.connect(self.start_timer_finish_event)
        self.start_timer.counter_signal.connect(self.start_timer_counter)
        threading.Thread(target=self.start_timer.run_single).start()


    def read_start_signals(self, ):
        signals = self.Config.get_start_signals()
        if len(signals):
            node_names = list(map(lambda x:x['name', signals]))
            self.plc.send_read_request('start_signals', 
                                        node_names,
                                        self.start_signals_update_event)

    
    def start_signals_update_event(self, values:dict):
        signals_info = self.Config.get_start_signals()
        res, log = configUtils.check_signals(signals_info, values)

        #read agin signal if conditions not ok
        if not res:
            # self.send_read_permisions_request()
            timer = timerThread(5)
            timer.finish_signal.connect(self.read_start_signals)
            threading.Thread(target=timer.run_single).start()
        
        else:
            self.mediator.send_nodes_log('start', log)
            self.start_done()


    def start_timer_counter(self, t):
        self.mediator.send_start_timer(t)

    def start_timer_finish_event(self,):
        self.start_done()
    
    def start_done(self,):
        self.mediator.send_config_start_done()

        
    