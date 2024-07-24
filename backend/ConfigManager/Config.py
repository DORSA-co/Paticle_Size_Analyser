from Database.settingDB import settingConfigDB

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
    
    def get_start_delay(self, ):
        return self.__config['start_delay']
    
    def get_permission_signals(self,) -> list[dict]:
        return self.__config['permission_signals']

    def get_output_signals(self, name:str) -> list[dict]:
        if name == 'signals1':
            return self.__config['signals1']
        
        return []
    
    def get_start_signals(self,) -> list[dict]:
        return self.__config['start_signals']