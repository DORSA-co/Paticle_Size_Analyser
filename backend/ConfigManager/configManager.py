import time
import threading

from PySide6.QtCore import QObject, Signal

from backend.Utils.threadTimer import timerThread
from backend.ConfigManager import configFlags
from backend.ConfigManager.Config import Config
from backend.PLC.PLCHandler import PLCHandler
from Mediator.mainMediator import Mediator
from backend.ConfigManager.configUtils import configUtils
# from backend.ConfigManager.pipeLineSteps import startPipeline
DEBUG = True



class configManager:

    def __init__(self) -> None:
        self.Config = Config()
        self.plc : PLCHandler = None
        self.mediator = Mediator()

        self.start_timer = None
        self.delay_timer = None
        self.stop_timer  = None

        self.start_signals_values = {}
        self.run_start_pipeline()
        # self.startPipline = startPipeline.startPipeline(self.Config, self.plc)
        # self.startPipline.run()

    def uncompleted_pipeline(self,):
        self.run_start_timer()
        self.mediator.send_failed_pipline()


        
    def run_start_pipeline(self,):
        start_mode = self.Config.get_start_mode()

        if start_mode == configFlags.startMode.timer:
            self.run_start_timer()
        
        elif start_mode == configFlags.startMode.signal_event:
            self.run_reading_start_signals()


    
    def run_start_timer(self, ):
        t = self.Config.get_start_time_cycle()
        self.start_timer = timerThread(t)
        self.start_timer.finish_signal.connect(self.start_timer_finish_event)
        self.start_timer.counter_signal.connect(self.start_timer_counter)
        threading.Thread(target=self.start_timer.run_single).start()


    def run_reading_start_signals(self, ):
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
            timer.finish_signal.connect(self.run_reading_start_signals)
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
        self.run_permission_pipline()


    #-------------------------------------------------------------------------------------------------
    #                                       permission
    #-------------------------------------------------------------------------------------------------
    def run_permission_pipline(self,):
        permisions_signals = self.Config.get_permission_signals()
        if len(permisions_signals):
            self.run_reading_permisions_signals(permisions_signals)

        else:
            self.permisions_done(True)




    def run_reading_permisions_signals(self,permisions_signals: list[dict]):

        names = list(map( lambda x:x['name'], permisions_signals))
        if self.Config.has_plc() and self.plc is not None and self.plc.is_connect():

            self.plc.send_read_request( request_id='permistions', 
                                        node_names=names, 
                                        answer_func=self.permisions_signals_event
                                        )
        #****************************************%%%%%%%%%%%%%%%%%%%%%%%%%%%%****************************************
        self.permisions_signals_event(
                {
                    'r1': True,
                    'r2': 49
                }
        )
        #****************************************%%%%%%%%%%%%%%%%%%%%%%%%%%%%****************************************
        


    def permisions_signals_event(self, values:dict):
        signals_info = self.Config.get_permission_signals()
        res, log = configUtils.check_signals(signals_info, values)
        self.mediator.send_nodes_log('permission', log)
        if res:
            # if not self.plc.is_connect():
               # return
            self.permisions_done(True)

        else:
            self.permisions_done(False)
            
    
    def permisions_done(self, res):
        self.mediator.send_config_permision_done(res)

        if res:
            self.write_output_signal('signals1')
            self.run_delay_pipline()

        else:
            self.uncompleted_pipeline()
    
    #-------------------------------------------------------------------------------------------------
    #                                       delay
    #-------------------------------------------------------------------------------------------------

    def run_delay_pipline(self,):
        t = self.Config.get_start_delay()
        if t == 0:
            self.delay_done()
        else:
            self.start_delay_timer(t)

    def start_delay_timer(self, t):
        self.delay_timer = timerThread(t)
        self.delay_timer.finish_signal.connect(self.delay_done)
        self.delay_timer.counter_signal.connect(self.delay_timer_counter)
        threading.Thread(target=self.delay_timer.run_single).start()

    def delay_timer_counter(self, t):
        self.mediator.send_delay_timer(t)


    def delay_done(self,):  
        self.mediator.send_config_delay_done()
        self.write_output_signal('signals2')

        #only for test
        self.uncompleted_pipeline()

    def stop(self, ):
        stop_mode = self.Config.get_stop_mode()

        if stop_mode == configFlags.stopMode.timer:
            self.run_stop_timer()



    def run_stop_timer(self, t ):
        self.stop_timer = timerThread(t)
        self.stop_timer.finish_signal.connect(self.stop_timer_finish_event)
        threading.Thread(target=self.stop_timer.run_single).start()

    

    
        

   

    def stop_timer_finish_event(self,):
        pass




    
    def write_output_signal(self, name):
        signals = self.Config.get_output_signals(name)

        if len(signals):
            if self.Config.has_plc() and self.plc is not None:
                nodes_value = configUtils.get_write_signal_dict(signals)
                self.plc.send_write_request(nodes_value)
        


    


    


        








