import os, sys
sys.path.append( os.getcwd() + "/pages_UI" )
sys.path.append( os.getcwd() + "/backend" )
from dorsaPylon import Collector

from settingPageUI import settingPageUI

class settingPageAPI:
    def __init__(self, ui:settingPageUI ,database, camera):
        self.cameraSetting = cameraSettingTabAPI(ui.cameraSettingTab, database, camera)
        self.gradingSetting = gradingSettingTabAPI(ui.gradingSettingTab)


class cameraSettingTabAPI:

    def __init__(self, ui ,database, camera):
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

        
class gradingSettingTabAPI:

    def __init__(self, ui, ):
        self.ui = ui
        self.new_standard_ranges = []

        self.ui.add_range_button_connector(self.add_range)
        self.ui.external_ranges_table_connector(self.modify_new_standard_range)

    
    def add_range(self,):
        range_data = self.ui.get_range_inputs()
        low = range_data['lower']
        high = range_data['upper']

        if low != high:
            for _range_ in self.new_standard_ranges:
                if ( low < _range_[1] and high >= _range_[1] ) or ( low <= _range_[0] and high > _range_[0] ):
                    self.ui.show_warning_massage("Warning: Ranges cannot overlap")
                    return

            self.new_standard_ranges.append( [ low, high ])
            self.new_standard_ranges.sort( key= lambda x:x[0])

            self.ui.clear_input_ranges()
            self.ui.set_ranges_table_data(self.new_standard_ranges)

            self.ui.show_warning_massage(None)

        else:
            self.ui.show_warning_massage("Warning: Lower and Upper couldn't be equal")


    
    def modify_new_standard_range(self,idx, data, status, btn):
        if status == 'delete':
            #remove range from list
            self.new_standard_ranges.pop(idx)
            #refresh table
            self.ui.clear_input_ranges()
            self.ui.set_ranges_table_data(self.new_standard_ranges)

        
        elif status =='edit':
            print('e')