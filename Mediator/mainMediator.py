
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from appAPI import main_API
from PagesAPI.settingPageAPI import settingPageAPI
from backend.Processing.Particel import Particle


class Mediator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Mediator, cls).__new__(cls, *args, **kwargs)
        return cls._instance



    
    def set_main_api(self, api:'main_API'):
        self.__mainAPI = api
    
    # def set_setting_api(self, api:settingPageAPI):
    #     self.__settingAPI = api
    def send(self, event:str, *args, **kwargs):
        if event =='auto_run_changed':
            self.send_auto_run_changed(*args, **kwargs)
        
        if event == 'particels_founded':
            self.send_particels_founded(*args, **kwargs)

    
    def send_auto_run_changed(self,*args, **kwards):
        self.__mainAPI.auto_run_changed(*args, **kwards)

    def send_nodes_log(self, name:str, log:list[dict]):
        self.__mainAPI.settingPageAPI.configSetting.recsive_node_log(name, log )
    
    def send_start_timer(self, t:int):
        #t is second
        self.__mainAPI.settingPageAPI.configSetting.recsive_start_timer(t)

    def send_delay_timer(self, t:int):
        #t is second
        self.__mainAPI.settingPageAPI.configSetting.recsive_delay_timer(t)

    def send_config_timer(self, name, t:int):
        self.__mainAPI.settingPageAPI.configSetting.recsive_live_timer(name, t)

    def send_pipline_log(self, log:str):
        self.__mainAPI.mainPageAPI.recsive_pipline_msg(log)


    def send_step_done(self, name:str,  flag:bool):
        self.__mainAPI.settingPageAPI.configSetting.recsive_step_done(name, flag)

    

    def send_config_delay_done(self, flag):
        self.__mainAPI.settingPageAPI.configSetting.recsive_step_done('delay', flag)

    def send_failed_pipline(self,):
        self.__mainAPI.settingPageAPI.configSetting.recsive_failed_pipline()

    
    def send_start_processing_request(self,):
        self.__mainAPI.mainPageAPI.fast_start()

    def send_stop_processing_request(self,):

        self.__mainAPI.mainPageAPI.recsive_stop_request()
    
    def send_start_processing_status(self, flag:bool):
        self.__mainAPI.configManager.rescive_run_pocessing_status(flag)

    def send_particels_founded(self, particels:list[Particle]):
        self.__mainAPI.configManager.rescive_particels_founded(particels)

    def send_pipline_restart(self,):
        self.__mainAPI.settingPageAPI.configSetting.recsive_restart_pipline()