
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from appAPI import main_API
from PagesAPI.settingPageAPI import settingPageAPI


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

    def send_nodes_log(self, name:str, log:list[dict]):
        self.__mainAPI.settingPageAPI.configSetting.recsive_node_log(name, log )
    
    def send_start_timer(self, t:int):
        #t is second
        self.__mainAPI.settingPageAPI.configSetting.recsive_start_timer(t)

    def send_delay_timer(self, t:int):
        #t is second
        self.__mainAPI.settingPageAPI.configSetting.recsive_delay_timer(t)

    def send_config_start_done(self,):
        # self.__mainAPI.configManager.send_config_start_done()
        self.__mainAPI.settingPageAPI.configSetting.recsive_step_done('start', True)

    def send_config_delay_done(self,):
        # self.__mainAPI.configManager.send_config_start_done()
        self.__mainAPI.settingPageAPI.configSetting.recsive_step_done('delay', True)


    def send_config_permision_done(self, res:bool):
        self.__mainAPI.settingPageAPI.configSetting.recsive_step_done('permission', res)

    def send_config_delay_done(self,):
        self.__mainAPI.settingPageAPI.configSetting.recsive_step_done('delay', True)

    def send_failed_pipline(self,):
        self.__mainAPI.settingPageAPI.configSetting.recsive_failed_pipline()

    