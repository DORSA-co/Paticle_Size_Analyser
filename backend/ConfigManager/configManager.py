import time
import threading

from PySide6.QtCore import QObject, Signal

from backend.Utils.threadTimer import timerThread, recurringThreadTimer #timoutTimerWorker
from backend.ConfigManager import configFlags
from backend.ConfigManager.Config import Config
from backend.PLC.PLCHandler import PLCHandler
from Mediator.mainMediator import Mediator
from backend.ConfigManager.configUtils import configUtils
from backend.Processing.Particel import Particle

# from backend.ConfigManager.pipeLineSteps import startPipeline
DEBUG = True



class configManager:

    def __init__(self,) -> None:
        self.Config = Config()
        self.plc:PLCHandler = None
        self.mediator = Mediator()

        self.start_timer = None
        self.delay_timer = None
        self.stop_timer  = None
        self.stop_algo_timer = None

        self.start_timer_thread:threading.Thread = None

        self.__run_flag = False

        self.timeoutWorker = None

        self.start_signals_values = {}
        # self.startPipline = startPipeline.startPipeline(self.Config, self.plc)
        # self.startPipline.run()

    def run_pipeline(self,):
        self.__run_flag = True
        self.run_start_pipeline()


    def stop_pipeline(self,):
        self.__run_flag = False

    def set_plc(self, plc:PLCHandler):
        self.plc = plc

    @configUtils.print_function_name
    def uncompleted_pipeline(self,):
        self.mediator.send_pipline_restart()

        self.stop_timeout()
        self.run_start_pipeline()
        self.mediator.send_failed_pipline()


    def start_timeout(self, timeout):
        self.timeoutWorker = timerThread(timeout/1000, sleep_time=0.1)
        self.timeoutWorker.finish_signal.connect(self.uncompleted_pipeline)
        threading.Thread( target=self.timeoutWorker.run_single).start()
    
    def stop_timeout(self,):
        if self.timeoutWorker is not None:
            self.timeoutWorker.stop()

    #----------------------------------------------------------------------------------------------------
    
 
    #----------------------------------------------------------------------------------------------------


    @configUtils.print_function_name    
    def run_start_pipeline(self,):
        if not self.__run_flag:
            return
        
        start_mode = self.Config.get_start_mode()

        if start_mode == configFlags.startMode.timer:
            self.run_start_timer()
        
        elif start_mode == configFlags.startMode.signal_event:
            self.run_reading_start_signals()


    @configUtils.print_function_name
    def run_start_timer(self, ):
        if not self.__run_flag:
            return
        
        if self.start_timer_thread is not None and self.start_timer_thread.is_alive():
            self.start_done(False)
            self.uncompleted_pipeline()
        
        t = self.Config.get_start_time_cycle()
        self.start_timer = timerThread(t, name='start_timer')
        self.start_timer.finish_signal.connect(self.start_timer_finish_event)
        self.start_timer.counter_signal.connect(self.start_timer_counter)

        self.start_timer_thread = threading.Thread(target=self.start_timer.run_single, daemon=True)
        self.start_timer_thread.start()

    @configUtils.print_function_name
    def run_reading_start_signals(self, ):
        if not self.__run_flag:
            return
        
        signals = self.Config.get_start_signals()
        if len(signals):
            node_names = list(map(lambda x:x['name'], signals))

            if self.plc is None or not self.plc.is_connect():
                #uncomplete pipline after 3000 ms
                self.start_timeout(3000)
            else:
                self.start_timeout(5000)
                self.plc.send_read_request('start_signals', 
                                            node_names,
                                            self.start_signals_update_event)

    @configUtils.print_function_name
    def start_signals_update_event(self, values:dict):
        if not self.__run_flag:
            return
        
        self.stop_timeout()

        signals_info = self.Config.get_start_signals()
        res, log = configUtils.check_signals(signals_info, values)

        #read agin signal if conditions not ok
        if not res:
            # self.send_read_permisions_request()
            self.start_done(False)
            
            # timer = timerThread(5, name='reading start_signals')
            # timer.finish_signal.connect(self.run_reading_start_signals)
            # threading.Thread(target=timer.run_single).start()
        
        else:
            self.start_done(True)

        self.mediator.send_nodes_log('start', log)


    def start_timer_counter(self, t):
        self.mediator.send_config_timer('start', t)

    @configUtils.print_function_name
    def start_timer_finish_event(self,):
        self.start_done(True)
    

    @configUtils.print_function_name
    def start_done(self, flag:bool):
        if not self.__run_flag:
            return
        
        self.mediator.send_step_done('start', flag)
        if flag:
            self.run_permission_pipline()
        else:
            self.uncompleted_pipeline()


    #-------------------------------------------------------------------------------------------------
    #                                       permission
    #-------------------------------------------------------------------------------------------------
    @configUtils.print_function_name
    def run_permission_pipline(self,):
        if not self.__run_flag:
            return
        
        permisions_signals = self.Config.get_permission_signals()
        if len(permisions_signals):
            self.run_reading_permisions_signals(permisions_signals)

        else:
            self.permisions_done(True)



    @configUtils.print_function_name
    def run_reading_permisions_signals(self,permisions_signals: list[dict]):
        if not self.__run_flag:
            return

        names = list(map( lambda x:x['name'], permisions_signals))
        
        if self.plc is None or not self.plc.is_connect():
            self.permisions_done(False)
            self.uncompleted_pipeline()

        
        else:
            self.start_timeout(5000)
            
            self.plc.send_read_request( request_id='permistions', 
                                        node_names=names, 
                                        answer_func=self.permisions_signals_event
                                        )
            
        
        

        # #****************************************%%%%%%%%%%%%%%%%%%%%%%%%%%%%****************************************
        # self.permisions_signals_event(
        #         {
        #             'r1': True,
        #             'r2': 80
        #         }
        # )
        # #****************************************%%%%%%%%%%%%%%%%%%%%%%%%%%%%****************************************
        

    @configUtils.print_function_name
    def permisions_signals_event(self, values:dict):
        if not self.__run_flag:
            return

        self.stop_timeout()

        signals_info = self.Config.get_permission_signals()
        res, log = configUtils.check_signals(signals_info, values)
        self.mediator.send_nodes_log('permission', log)
        if res:
            # if not self.plc.is_connect():
               # return
            self.permisions_done(True)

        else:
            self.permisions_done(False)
            

    @configUtils.print_function_name
    def permisions_done(self, res):
        self.mediator.send_step_done('permission', res)

        if res:
            self.write_output_signal('signals1')
            self.run_delay_pipline()

        else:
            self.uncompleted_pipeline()
    
    #-------------------------------------------------------------------------------------------------
    #                                       delay
    #-------------------------------------------------------------------------------------------------
    @configUtils.print_function_name
    def run_delay_pipline(self,):
        if not self.__run_flag:
            return
        
        t = self.Config.get_start_delay()
        if t == 0:
            self.delay_done()
        else:
            self.start_delay_timer(t)


    @configUtils.print_function_name
    def start_delay_timer(self, t):
        if not self.__run_flag:
            return
        
        self.delay_timer = timerThread(t, name='delay_timer')
        self.delay_timer.finish_signal.connect(self.delay_done)
        self.delay_timer.counter_signal.connect(self.delay_timer_counter)
        threading.Thread(target=self.delay_timer.run_single).start()

    def delay_timer_counter(self, t):
        self.mediator.send_config_timer('delay', t)

    @configUtils.print_function_name
    def delay_done(self,):  
        if not self.__run_flag:
            return
        
        self.run_processing()
        # #only for test
        # self.uncompleted_pipeline()
    #-------------------------------------------------------------------------------------------------
    #                                       run processing
    #-------------------------------------------------------------------------------------------------
    @configUtils.print_function_name
    def run_processing(self,):
        if not self.__run_flag:
            return
        
        self.mediator.send_start_processing_request()


    @configUtils.print_function_name
    def rescive_run_pocessing_status(self, flag):
        if not self.__run_flag:
            return
        
        self.mediator.send_step_done('delay', flag)

        if flag:
            self.write_output_signal('signals2')
            self.run_stop_pipline()
        else:
            self.uncompleted_pipeline()
    

    
        
    #-------------------------------------------------------------------------------------------------
    #                                       delay
    #-------------------------------------------------------------------------------------------------
    @configUtils.print_function_name
    def run_stop_pipline(self, ):
        if not self.__run_flag:
            return
        
        stop_mode = self.Config.get_stop_mode()
        if stop_mode == configFlags.stopMode.timer:
            self.run_stop_timer()

        elif stop_mode == configFlags.stopMode.signal_event:
            self.run_reading_stop_signals()
            self.run_stop_timer()


        elif stop_mode == configFlags.stopMode.image_detection:
            self.run_image_detection_stop()


    @configUtils.print_function_name
    def run_stop_timer(self,):
        if not self.__run_flag:
            return 
        t = self.Config.get_stop_time()
        self.stop_timer = timerThread(t, name='stop_timer')
        self.stop_timer.finish_signal.connect(self.stop_timer_finish_event)
        self.stop_timer.counter_signal.connect(self.stop_timer_counter)
        threading.Thread(target=self.stop_timer.run_single).start()

    

    def stop_timer_counter(self,t):
        self.mediator.send_config_timer('stop', t)
        

   
    @configUtils.print_function_name
    def stop_timer_finish_event(self,):
        self.stop_done()

    @configUtils.print_function_name
    def run_reading_stop_signals(self,):
        if not self.__run_flag:
            return
        
        signals = self.Config.get_stop_signals()
        if len(signals):
            node_names = list(map(lambda x:x['name'], signals))

            if self.plc is None or not self.plc.is_connect():
                #uncomplete pipline after 3000 ms
                self.start_timeout(3000)
            else:
                self.start_timeout(5000)
                self.plc.send_read_request('stop_signals', 
                                            node_names,
                                            self.stop_signals_update_event)

    def stop_signals_update_event(self, values:dict):
        if not self.__run_flag:
            return
        
        self.stop_timeout()

        signals_info = self.Config.get_start_signals()
        res, log = configUtils.check_signals(signals_info, values)

        #read agin signal if conditions not ok
        if not res:
            self.stop_done(False)
        
        else:
            self.stop_done(True)

        self.mediator.send_nodes_log('stop', log)
    


    @configUtils.print_function_name
    def run_image_detection_stop(self):
        t = self.Config.get_stop_algo_timout()
        emergency_time = 0

        if self.Config.is_stop_emergency_timer_anable():
            emergency_time = self.Config.get_stop_emergency_time()
        
        self.stop_algo_timer = recurringThreadTimer(recurring_timer=t, limit_timer=emergency_time, name='stop_algo')
        # self.stop_algo_timer = timerThread(t, name='stop_algo_timout')
        self.stop_algo_timer.finish_signal.connect(self.stop_algo_timout)
        threading.Thread(target=self.stop_algo_timer.run_single).start()

    #@configUtils.print_function_name
    def rescive_particels_founded(self, particels: list[Particle]):
        if not self.Config.get_stop_mode() == configFlags.stopMode.image_detection:
            return
        
        if self.stop_algo_timer is None:
            return
        
        thresh_size = self.Config.get_stop_algo_thresh_size()
        for particel in particels:
            if particel.avg_diameter > thresh_size:
                self.stop_algo_timer.recurring()
                break
        
    
    @configUtils.print_function_name 
    def stop_algo_timout(self,):
        self.stop_done()



    @configUtils.print_function_name
    def stop_done(self,):
        self.mediator.send_step_done('stop', True)
        self.write_output_signal('signals3')

        self.stop_processing()
        


    def stop_processing(self,):
        self.mediator.send_stop_processing_request()
        self.finish_pipline()


    def finish_pipline(self,):
        self.mediator.send_pipline_restart()
        self.run_start_pipeline()




    
    def write_output_signal(self, name):
        signals = self.Config.get_output_signals(name)

        if len(signals):
            if self.Config.has_plc() and self.plc is not None:
                nodes_value = configUtils.get_write_signal_dict(signals)
                self.plc.send_write_request(nodes_value)
        

        self.mediator.send_step_done(name, True)
        


    


    


        








