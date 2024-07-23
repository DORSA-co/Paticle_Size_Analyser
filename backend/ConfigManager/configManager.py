import time
import threading


from Database.settingDB import settingConfigDB
from backend.Utils.threadTimer import timerThread



class configManager:

    def __init__(self) -> None:
        self.Config = Config()

        


    def __start_timer(self, ):
        t = self.Config.get_start_time_cycle()
        self.start_timer = timerThread(t)
        self.start_timer.finish_signal.connect(self.start_timer_event)
        threading.Thread(target=self.start_timer.run_single).start()
    
    def check_signals(self,):
        pass

    def start_timer_event(self,):
        self.__start_timer()




        






class Config:
    
    def __init__(self) -> None:
        self.load()
    
    def load(self,):
        self.__config = settingConfigDB().load_config()
    

    def can_start_manual(self,) -> bool:
        return bool(self.__config['start_manual'])
    
    def can_stop_manual(self,) -> bool:
        return bool(self.__config['stop_manual'])
    
    def has_plc(self, ) -> bool:
        return bool(self.__config['plc_enable'])
    
    def get_start_mode(self,) -> str:
        return self.__config['start_mode']
    
    def get_stop_mode(self,) -> str:
        return self.__config['stop_mode']
    
    def get_fps_regulator(self, ):
        return self.__config['fps_regulator']
    
    def get_start_time_cycle(self,) -> int:
        t =  self.__config['start_period_time']
        t = t * 60
        return t