from dorsaPylon import Collector
from Database.settingDB import settingDB, settingAlgorithmDB, settingCameraDB, settingStorageDB
from PagesUI.settingPageUI import settingPageUI, algorithmSettingTabUI, cameraSettingTabUI, storageSettingTabUI

class settingPageAPI:
    def __init__(self, ui:settingPageUI ,database:settingDB, camera):
        self.cameraSetting = cameraSettingTabAPI(ui.cameraSettingTab, database.camera_db, camera)
        self.algorithmSetting = algorithmSettingTabAPI(ui.algorithmSettingTab, database.algorithm_db)
        self.storageSetting = storageSettingTabAPI(ui.storageSettingTab, database.storage_db)

    def startup(self,):
        self.cameraSetting.startup()






class storageSettingTabAPI:

    def __init__(self, ui:storageSettingTabUI ,database:settingStorageDB):
        self.ui = ui
        self.database = database
        self.ui.select_dir_button_connector(self.choose_dir)
        self.ui.save_button_connector(self.save)
        self.ui.cancel_button_connector(self.cancel)
        self.load_from_db()
        self.ui.save_state(True)
    
    def choose_dir(self):
        path = self.ui.open_select_dir_dialog()
        if path != '':
            self.ui.set_path(path)

    def save(self,):
        settings = self.ui.get_settings()
        self.database.save(settings)
        self.ui.save_state(True)

    def cancel(self,):
        state = self.ui.show_confirm_box("Cancel", "Are You Sure?", 
                                 buttons=['yes','no'])
        if state == 'no':
            return
        self.load_from_db()
        self.ui.save_state(True)

    def load_from_db(self):
        settings = self.database.load()
        self.ui.set_settings(settings)






class cameraSettingTabAPI:

    def __init__(self, ui:cameraSettingTabUI ,database, cameras:settingCameraDB):
        self.ui = ui
        self.database = database
        self.cameras = cameras
        self.camera_collector  = Collector()
        self.is_playing = False

        self.set_camera_parms_funcs = { }
        self.get_camera_parms_range_funcs = {}

        #camera_application could be 'standard' and 'zoom' corespond to camera usage for measuring particles
        for camera_application in self.cameras.keys():
        
            set_funcs = {
                'gain': self.cameras[camera_application].Parms.set_gain,
                'exposure': self.cameras[camera_application].Parms.set_exposureTime,
                'width': lambda w: self.cameras[camera_application].Parms.set_roi(None, w, None, None),
                'height': lambda h: self.cameras[camera_application].Parms.set_roi(h, None, None, None),
            }

            range_funcs = {
            'gain': self.cameras[camera_application].Parms.get_gain_range,
            'exposure': self.cameras[camera_application].Parms.get_exposureTime_range,
            'width': lambda : self.cameras[camera_application].Parms.get_roi_range()[1],
            'height': lambda : self.cameras[camera_application].Parms.get_roi_range()[0],
            }

            self.set_camera_parms_funcs[camera_application] = set_funcs
            self.get_camera_parms_range_funcs[camera_application] = range_funcs

        self.load_from_database()
        self.ui.change_setting_event_connector(self.update_setting_event)
        self.ui.start_stop_event_connector( self.play_stop_camera )
        self.ui.save_button_connector(self.save_setting)
        self.ui.cancel_button_connector(self.cancel)
        self.set_allowed_values_camera_setting()
        

    def startup(self):
        self.ui.reset()

    def update_setting_event(self, group_setting, camera_application, settings = None):
        #when event happend, settings argument got value from ui
        #if settings is None:
        #    settings = self.ui.get_camera_settings()
        if group_setting == 'camera_setting':
            self.set_camera_setting(camera_application, settings)
        else:
            pass

    
    def set_camera_setting(self,camera_application, settings):
        #select which camera should be update
        for setting_name , value in settings.items():
            corespond_parm_function = self.set_camera_parms_funcs[camera_application].get(setting_name)
            if corespond_parm_function is not None:
                corespond_parm_function( value )


    def set_allowed_values_camera_setting(self):
        camera_application = self.ui.get_selected_camera_application()
        spinboxs_range = {}
        for field_name , get_range_func in self.get_camera_parms_range_funcs[camera_application].items():
            spinboxs_range[ field_name] = get_range_func()
        
        self.ui.set_camera_settings_spinbox_ranges(spinboxs_range)
        #----------
        available_devices = self.camera_collector.get_all_serials()
        self.ui.set_camera_devices(available_devices)

        
    def play_stop_camera(self,is_playing):
        self.is_playing = is_playing
        camera_application = self.ui.get_selected_camera_application()
        if is_playing:
            settings = self.ui.get_camera_settings()
            self.set_camera_setting(camera_application, settings)
            cam = self.cameras[camera_application]
            cam.Operations.start_grabbing()
        
        else:
            cam = self.cameras[camera_application]
            cam.Operations.stop_grabbing()
    
    def show_live_image(self,):
        camera_application = self.ui.get_selected_camera_application()
        img = self.cameras[camera_application].image
        if self.is_playing:
            self.ui.show_live_image(img)


    def save_setting(self,):
        settings = self.ui.get_all_settings()
        camera_application = self.ui.get_selected_camera_application()
        settings['application'] = camera_application
        self.database.save(settings)
        self.set_camera_setting(camera_application, settings)

    def cancel(self):
        state = self.ui.show_confirm_box("Cancel", "Are You Sure?", 
                                 buttons=['yes','no'])
        if state == 'no':
            return
        
        self.load_from_database()
        self.ui.disable_save_btn()

    def load_from_database(self,):
        camera_application = self.ui.get_selected_camera_application()
        settings = self.database.load(camera_application)
        self.ui.set_all_settings(settings)
        return settings





class algorithmSettingTabAPI:

    def __init__(self, ui:algorithmSettingTabUI, database:settingAlgorithmDB):
        self.ui = ui
        self.database = database

        self.ui.save_button_connector(self.save)
        self.ui.cancel_button_connector(self.cancel)
        self.ui.restor_button_connector(self.restor)

        self.load_from_db()
    
    def load_from_db(self):
        data = self.database.load()
        self.ui.set_sata(data)
        self.ui.save_state(True)

    def save(self,):
        data = self.ui.get_data()
        self.database.save(data)
        self.ui.save_state(True)
    

    def cancel(self):
        self.load_from_db()

    
    def restor(self):
        self.database.restor_default()
        self.load_from_db()