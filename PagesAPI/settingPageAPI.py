import os
from PySide6.QtCore import QThread, QObject, Signal, QMutex

from backend.Camera.dorsaPylon import Collector, Camera
from Database.settingDB import settingDB, settingAlgorithmDB, settingCameraDB, settingStorageDB, settingSampleDB, settingExportDB
from PagesUI.settingPageUI import settingPageUI, algorithmSettingTabUI, cameraSettingTabUI, storageSettingTabUI, sampleSettingTabUI, exportSettingTabUI
from backend.Utils.StorageUtils import storageManager
import Constants.CONSTANTS as CONSTANTS
from uiUtils import GUIComponents


class settingPageAPI:
    def __init__(self, ui:settingPageUI ,database:settingDB, cameras):
        self.cameraSetting = cameraSettingTabAPI(ui.cameraSettingTab, database.camera_db, cameras)
        self.algorithmSetting = algorithmSettingTabAPI(ui.algorithmSettingTab, database.algorithm_db)
        self.storageSetting = storageSettingTabAPI(ui.storageSettingTab, database.storage_db)
        self.sampleSetting = sampleSettingTabAPI(ui.sampleSettingTab, database.sample_db)
        self.exportSetting = exportSettingTabAPI(ui.exportSettingTab, database.export_db)
        # ui.cameraSettingTab.save_state(True)
        # ui.algorithmSettingTab.save_state(True)
        # ui.storageSettingTab.save_state(True)
        # ui.sampleSettingTab.save_state(True)

    def startup(self,):
        self.cameraSetting.startup()
    
    def endup(self,) -> bool:
        cam_flag = self.cameraSetting.endup()
        return cam_flag




class sampleSettingTabAPI:

    def __init__(self, ui:sampleSettingTabUI ,database:settingSampleDB):
        self.ui = ui
        self.database = database

        self.autoname_struct = ''

        self.ui.code_name_buttons_connector(self.code_name_button_event)
        self.ui.clear_name_struct_button_connector(self.clear_struct_button_event)
        self.ui.save_button_connector(self.save_setting)
        self.ui.cancel_button_connector(self.cancel)
        self.load_from_db()

    def set_standards_event(self,standards:list[str]):
        """this function called when a new standard defined

        Args:
            standards (list[str]): names of standards
        """
        standards.insert(0, '-')
        self.ui.set_standards(standards)
        self.load_from_db()

    def code_name_button_event(self, name):
        if CONSTANTS.NAME_CODES[name] not in self.autoname_struct or name == 'spacer':
            self.autoname_struct += CONSTANTS.NAME_CODES[name]
            self.ui.set_autoname_struct_input(self.autoname_struct)

    def clear_struct_button_event(self, ):
        if len(self.autoname_struct) == 0:
            return
        #check if last character is spacer, remove only that
        if self.autoname_struct[-1] == CONSTANTS.NAME_CODE_SPACER:
            self.autoname_struct = self.autoname_struct[:-1]
        
        #check if struct finish by a shortcode, remove that
        elif self.autoname_struct[-1] == CONSTANTS.NAME_CODE_CHAR:
            #last char is % so we search from -2
            idx = self.autoname_struct.rfind(CONSTANTS.NAME_CODE_CHAR,0, -2)
            self.autoname_struct = self.autoname_struct[:idx]
        
        self.ui.set_autoname_struct_input(self.autoname_struct)

    

    def save_setting(self,):
        data = self.ui.get_settings()
        self.database.save(data)
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
        self.autoname_struct = settings.get('autoname_struct', '' )
        self.ui.set_settings(settings)
        self.ui.set_autoname_struct_input(self.autoname_struct)
        self.ui.save_state(True)


    




class storageSettingTabAPI:
    default_folder = 'AppData/Local/Dorsa-PSA-Reports'
    def __init__(self, ui:storageSettingTabUI ,database:settingStorageDB):
        self.ui = ui
        self.database = database
        self.check_storage_path()
        self.ui.select_dir_button_connector(self.choose_dir)
        self.ui.save_button_connector(self.save)
        self.ui.cancel_button_connector(self.cancel)
        self.load_from_db()

    def check_storage_path(self,):
        settings = self.database.load()
        if not os.path.exists(settings.get('path', '')):
            path = storageManager.get_windows_user_path(self.default_folder)
            storageManager.build_dir(path)
            self.ui.set_path(path)
            settings = self.database.load()
            settings['path'] = path
            self.database.save(settings)
    
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
        self.ui.save_state(True)











class cameraSettingTabAPI:
    DEBUG_PROCESS_THREAD = False    
    def __init__(self, ui:cameraSettingTabUI ,database:settingCameraDB, cameras: dict[str, Camera]):
        self.ui = ui
        self.database = database
        self.cameras = cameras
        self.camera_collector  = Collector()
        self.is_playing = False

        self.set_camera_parms_funcs = { }
        self.get_camera_parms_range_funcs = {}
        self.external_camera_change_event = None

        self.device_checker_timer = GUIComponents.timerBuilder(1000, self.check_devices_event)

        #camera_application could be 'standard' and 'zoom' corespond to camera usage for measuring particles
        

        
        self.setup_camera_funcs()
        self.load_from_database()
        self.ui.change_setting_event_connector(self.update_setting_event)
        self.ui.start_stop_event_connector( self.play_stop_camera )
        self.ui.save_button_connector(self.save_setting)
        self.ui.cancel_button_connector(self.cancel)
        self.ui.restor_button_connector(self.restor)
        self.ui.change_camera_connector(self.change_camera)
        self.set_allowed_values_camera_setting()
        

    def startup(self):
        self.ui.reset()
        self.device_checker_timer.start()

    def endup(self,) -> bool:
        """_summary_

        Returns:
            bool: permition for change page. if True page change is acceptable
        """
        for  camera in self.cameras.values():
            camera.Operations.stop_grabbing()
        self.device_checker_timer.stop()
        return True
    
    def setup_camera_funcs(self,):
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

    def update_setting_event(self, group_setting, camera_application, settings = None):
        #when event happend, settings argument got value from ui
        #if settings is None:
        #    settings = self.ui.get_camera_settings()
        if group_setting == 'camera_setting':
            self.set_camera_setting(camera_application, settings)
        else:
            pass

    def set_camera_device_change_event(self, func):
        self.external_camera_change_event = func

    def change_camera(self,):
        device = {'application':'standard',
                  'serial_number': self.ui.get_camera_device()
                  }
        if self.external_camera_change_event is not None:
            pass
            self.external_camera_change_event(device)

        self.setup_camera_funcs()
    
    def set_camera_setting(self,camera_application, settings):
        #select which camera should be update
        for setting_name , value in settings.items():
            corespond_parm_function = self.set_camera_parms_funcs[camera_application].get(setting_name)
            if corespond_parm_function is not None:
                corespond_parm_function( value )


    def set_allowed_values_camera_setting(self):
        camera_application = self.ui.get_selected_camera_application()
        spinboxs_range = {}
        if self.get_camera_parms_range_funcs.get(camera_application) is None:
            return
        
        for field_name , get_range_func in self.get_camera_parms_range_funcs[camera_application].items():
            spinboxs_range[ field_name] = get_range_func()
        
        self.ui.set_camera_settings_spinbox_ranges(spinboxs_range)
        #----------
    
    def check_devices_event(self,):
        self.device_checker_thread = QThread()
        self.device_checker_worker = DeviceTrackingWorker(self.camera_collector)
        if not self.DEBUG_PROCESS_THREAD:
            self.device_checker_worker.moveToThread(self.device_checker_thread)
        self.device_checker_thread.started.connect(self.device_checker_worker.serial_number_finder)
        self.device_checker_worker.finished.connect(self.device_checker_thread.quit)
        self.device_checker_thread.finished.connect(self.device_checker_thread.deleteLater)
        self.device_checker_worker.finished.connect(self.refresh_devices)
        self.device_checker_worker.finished.connect(self.device_checker_worker.deleteLater)

        if self.DEBUG_PROCESS_THREAD:
            self.device_checker_worker.serial_number_finder()
        else:
            self.device_checker_thread.start()


    def refresh_devices(self):
        list_of_available_cameras = self.device_checker_worker.get_available_serials()
        self.ui.set_camera_devices(list_of_available_cameras)


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
        self.ui.save_state(True)

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
        self.ui.save_state(True)
        return settings

    def restor(self):
        self.database.restor_default()
        self.load_from_database()




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
        state = self.ui.show_confirm_box("Cancel", "Are You Sure?", 
                                 buttons=['yes','no'])
        if state == 'no':
            return
        self.load_from_db()

    
    def restor(self):
        self.database.restor_default()
        self.load_from_db()




class exportSettingTabAPI:

    def __init__(self, ui:exportSettingTabUI ,database:settingExportDB):
        self.ui = ui
        self.database = database

        self.ui.select_dir_buttons_connector(self.load_file)
        self.ui.save_button_connector(self.save)
        self.ui.restor_button_connector(self.restore_default)

        self.load_from_db()
    
    def load_file(self, setting_name:str):
        """_summary_

        Args:
            setting_name (str): shows button of which one of 'report_excel' or 'compare_excel' clicked
        """
        path = self.ui.open_select_file_dialog()
        data = {}
        data[setting_name] = path
        self.ui.set_setting(data)
    

    def save(self,):
        data = self.ui.get_settings()
        self.database.save(data)
        self.ui.save_state(True)

    def cancel(self,):
        self.load_from_db()
        self.ui.save_state(True)

    def restore_default(self,):
        self.database.restor_default()
        self.load_from_db()
        self.ui.save_state(True)

    def load_from_db(self,):        
        data = self.database.load()
        self.ui.set_setting(data)
        self.ui.save_state(True)
        

class DeviceTrackingWorker(QObject):
    finished = Signal()
    finished_processing = Signal()
    def __init__(self, collector: Collector) -> None:
        self.collector = collector
        super().__init__()

    def serial_number_finder(self):
        for i in range(1):
            self.available_serials = self.collector.get_all_serials()
        self.finished.emit()

    def get_available_serials(self):
        return self.available_serials
    

