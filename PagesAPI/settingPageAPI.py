import os, sys
sys.path.append( os.getcwd() + "/pages_UI" )
sys.path.append( os.getcwd() + "/backend" )
from dorsaPylon import Collector
from settingPageUI import settingPageUI

class settingPageAPI:
    def __init__(self, ui:settingPageUI ,database, camera):
        self.cameraSetting = cameraSettingTabAPI(ui.cameraSettingTab, database, camera)


class cameraSettingTabAPI:

    def __init__(self, ui: settingPageUI ,database, camera):
        self.ui = ui
        self.database = database
        self.camera = camera
        self.camera_collector  = Collector()
        self.is_playing = False
        
        self.set_camera_parms_funcs = {
            'gain': self.camera.Parms.set_gain,
            'exposure': self.camera.Parms.set_exposureTime,
            'width': lambda w: self.camera.Parms.set_roi(None, w, None, None),
            'height': lambda h: self.camera.Parms.set_roi(h, None, None, None),
        }

        self.get_camera_parms_range_funcs = {
            'gain': self.camera.Parms.get_gain_range,
            'exposure': self.camera.Parms.get_exposureTime_range,
            'width': lambda : self.camera.Parms.get_roi_range()[1],
            'height': lambda : self.camera.Parms.get_roi_range()[0],
        }

        self.ui.change_setting_event_connector(self.update_camera_setting)
        self.ui.start_stop_event_connector( self.play_stop_camera )
        self.set_allowed_values_camera_setting()


    def update_camera_setting(self, settings = None):
        #when event happend, settings got value from ui
        if settings is None:
            settings = self.ui.get_settings()
        for setting_name , value in settings.items():
            corespond_parm_function = self.set_camera_parms_funcs[setting_name]
            corespond_parm_function( value )


    def set_allowed_values_camera_setting(self):
        spinboxs_range = {}
        for field_name , get_range_func in self.get_camera_parms_range_funcs.items():
            spinboxs_range[ field_name] = get_range_func()
        
        self.ui.set_settings_spinbox_ranges(spinboxs_range)
        #----------
        available_devices = self.camera_collector.get_all_serials()
        self.ui.set_camera_devices(available_devices)

        
    def play_stop_camera(self,is_playing):
        self.is_playing = is_playing

        if is_playing:
            settings = self.ui.get_settings()
            self.update_camera_setting(settings)
            self.camera.Operations.start_grabbing()
        
        else:
            self.camera.Operations.stop_grabbing()
        
        

    
    def show_live_image(self, img):
        if self.is_playing:
            self.ui.show_live_image(img)

        
