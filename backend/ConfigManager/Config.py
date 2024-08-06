from Database.settingDB import settingConfigDB
from backend.ConfigManager import configFlags


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
    
    def is_auto_run_enable(self,) -> bool:
        return bool(self.__config['auto_run_enable'])
    
    def is_stop_emergency_timer_anable(self,) -> bool:
        return bool(self.__config['stop_emergency_timer_enable'])
    
    def get_stop_emergency_time(self,) -> int:
        return int(self.__config['stop_emergency_timer_time']) * 60
    
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
    
    def get_stop_time(self,) -> int:
        t = self.__config['stop_delay']
        t *= 60
        return t
    
    def get_start_delay(self, ):
        return self.__config['start_delay']
    
    def get_permission_signals(self,) -> list[dict]:
        return self.__config['permission_signals']

    def get_output_signals(self, name:str) -> list[dict]:
        return self.__config[name]
        
        
        return []
    
    def get_start_signals(self,) -> list[dict]:
        return self.__config['start_signals']
    
    def get_stop_signals(self,) -> list[dict]:
        return self.__config['stop_signals']
    
    def get_stop_algo_min_time(self,) -> int:
        return self.__config['stop_algo_min_time']
    
    def get_stop_algo_thresh_size(self,) -> float:
        return self.__config['stop_algo_thresh_size']
    
    def get_stop_algo_timout(self,):
        return self.__config['stop_algo_timout']


    def is_telecentric_lens(self,) -> bool:
        return self.__config['lens_type'] == configFlags.lensType.telecentric
    
    def is_standard_lens(self,) -> bool:
        return self.__config['lens_type'] == configFlags.lensType.standard
    
    def get_magnification(self,) -> float:
        return self.__config['lens_magnification']
    
    def get_pixel_size(self,) -> float:
        return self.__config['pixel_size']