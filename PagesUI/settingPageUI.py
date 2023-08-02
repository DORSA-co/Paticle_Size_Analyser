from uiUtils import GUIComponents

from uiUtils.guiBackend import GUIBackend



class settingPageUI:
    def __init__(self, ui) -> None:
        self.cameraSettingTab = cameraSettingTabUI(ui)
        self.algorithmSettingTab = algorithmSettingTabUI(ui)
        self.storageSettingTab = storageSettingTabUI(ui)



class commonSettingUI:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.save_mgs = self.ui.settingpage_save_massage_lbl

    def is_saved_massage(self, is_saved):
        if is_saved:
            GUIBackend.set_label_text(self.save_mgs, "setting saved")
        else:
            GUIBackend.set_label_text(self.save_mgs, "*temp setting")

    
    def save_state(self, is_saved):
        if not is_saved:
            GUIBackend.set_enable(self.save_btn)
            GUIBackend.set_enable(self.cancel_btn)
            self.is_saved_massage(is_saved)
        
        else:
            GUIBackend.set_disable(self.save_btn)
            GUIBackend.set_disable(self.cancel_btn)
            self.is_saved_massage(is_saved)


        


class storageSettingTabUI(commonSettingUI):

    def __init__(self, ui) -> None:
        super(storageSettingTabUI, self).__init__(ui)
        self.ui = ui
        self.select_dir_btn = self.ui.settingpage_storage_select_dir_btn
        self.path_input = self.ui.settingpage_storage_path_input
        self.save_btn = self.ui.settingpage_storage_save_btn
        self.cancel_btn = self.ui.settingpage_storage_cancel_btn
        self.__setting_change_connector__()

    def __setting_change_connector__(self,):
        GUIBackend.input_text_connector( self.path_input, lambda : self.save_state(False))

    def select_dir_button_connector(self, func):
        GUIBackend.button_connector(self.select_dir_btn, func)

    
    def open_select_dir_dialog(self,):
        return GUIComponents.selectDirectoryDialog()
    
    def set_path(self, path):
        GUIBackend.set_input(self.path_input, path)

    def save_button_connector(self, func):
        GUIBackend.button_connector(self.save_btn, func)

    def cancel_button_connector(self, func):
        GUIBackend.button_connector(self.cancel_btn, func)


    def get_settings(self, ):
        data = {}
        data['path'] = GUIBackend.get_input(self.path_input)

        return data
    
    def set_settings(self, settings):
        GUIBackend.set_input(self.path_input, settings['path'])

        









class cameraSettingTabUI(commonSettingUI):

    def __init__(self, ui) -> None:
        super(cameraSettingTabUI, self).__init__(ui)
        self.ui = ui

        self.devices_combobox = self.ui.settingpage_camera_device_combobox
        self.fps_spinbox = self.ui.settingpage_camera_fps_spinbox
        self.camera_start_btn = self.ui.settingpage_camera_start_btn
        self.save_btn = self.ui.settingpage_camera_save_btn
        self.cancel_btn = self.ui.settingpage_camera_cancel_btn
        self.restor_btn = self.ui.settingpage_camera_restore_btn
        self.live_img_lbl = self.ui.settingpage_camera_live_lbl
        
        self.__is_start__ = False
        self.__connection_event_function__ = None
        self.__change_setting_event_function__ = None

        


        self.camera_application = 'standard'

        self.settings = {
            #features that can't be changed in grabbing    
            'camera_setting':{
                'width': self.ui.settingpage_camera_width_spinbox,
                'height': self.ui.settingpage_camera_height_spinbox,
                'gain': self.ui.settingpage_camera_gain_spinbox,
                'exposure': self.ui.settingpage_camera_exposure_spinbox,
            },
            'others':{
                'fps': self.ui.settingpage_camera_fps_spinbox,
                'serial_number': self.ui.settingpage_camera_device_combobox
            }
            #'fps': self.ui.settingpage_camera_fps_spinbox,
            }

        self.start_stop_icon = {
            True: ":/assets/Assets/icons/stop50.png",
            False: ":/assets/Assets/icons/play-48.png"
        }

        self.fields_enable_status = {
            True: ['gain', 'exposure'],
            False: ['width','height' ]
        }

        GUIBackend.button_connector(self.camera_start_btn, self.__internal_start_event__)
        
        self.__mange_fields_enable__()
        self.__settings_change_connector__()
        self.save_button_connector(self.__internal_save_event__)
    
    def reset(self):
        self.__is_start__ = False
        #change button icon
        GUIBackend.set_button_icon(self.camera_start_btn, self.start_stop_icon[self.__is_start__])
        #enable and disable setting fields
        self.__mange_fields_enable__()
        GUIBackend.set_disable(self.save_btn)

    def start_stop_event_connector(self, func):
        """connect a function to start and stop button vlick event

        Args:
            func (_type_): a function with one argument that would be True in start and False in Stop
        """
        self.__connection_event_function__ = func

    def change_setting_event_connector(self, func):
        """connect a function to change setting event

        Args:
            func (function()): a function with 3 argument. the first argument is ' that whould be a dictionary whit key setting name and its value
        
        (setting_group, self.camera_application, arg)
        """
        self.__change_setting_event_function__ = func

    def save_button_connector(self, func):
        GUIBackend.button_connector(self.save_btn, func)

    def cancel_button_connector(self, func):
        GUIBackend.button_connector(self.cancel_btn, func)

    def restor_button_connector(self, func):
        GUIBackend.button_connector(self.restor_btn, func)

    def __settings_change_connector__(self,):
        """connect all input fields of setting into an internal function
        """
        for setting_type in self.settings.keys():
            for field_name, field in self.settings[setting_type].items():
                if GUIBackend.is_spinbox(field):
                    GUIBackend.spinbox_connector(field, self.__internal_change_setting_event__(setting_type, field_name))


    
    def __internal_change_setting_event__(self,setting_group, setting_name):
        """got setting that changed and pass it to external function self.__change_setting_event_function__ as an event
        this function connected to change setting input fields and calledc automaticly

        Args:
            setting_group (_type_): group_setting can be 'other' or 'camera_setting'. 'camera_setting' is for camera parameters
            setting_name (_type_): name of setting that changed.
        """
        def func():
            GUIBackend.set_enable(self.save_btn)
            self.is_saved_massage(False)
            #assert self.change_setting_event_connector is not None, "No Function Event determind. use cameraSettingTab.change_setting_event_connector method to do it"
            value = GUIBackend.get_input(self.settings[setting_group][setting_name])
            arg = {setting_name:value}
            if self.__change_setting_event_function__ is not None:
                self.__change_setting_event_function__(setting_group, self.camera_application, arg)
        return func


    
    def __internal_start_event__(self,):
        """this function called when the start button clicked. this function calls manage disable and enable fields and call external function
        """
        #change flag. (True for grabbing)
        self.__is_start__ = not(self.__is_start__)
        #change button icon
        GUIBackend.set_button_icon(self.camera_start_btn, self.start_stop_icon[self.__is_start__])
        #enable and disable setting fields
        self.__mange_fields_enable__()
        #call exteral function as event
        if self.__connection_event_function__ is not None:
            self.__connection_event_function__(self.__is_start__)


    def __mange_fields_enable__(self):
        """mange which fields be enable when change start, stop
        """
        #enable fields corespond to __is_srart__
        for fields_name in self.fields_enable_status[self.__is_start__]:
            GUIBackend.set_enable(self.settings['camera_setting'][fields_name])

        #disable other fields corespond to __is_srart__
        for fields_name in self.fields_enable_status[not(self.__is_start__)]:
            GUIBackend.set_disable(self.settings['camera_setting'][fields_name])

        GUIBackend.set_disable_enable( self.devices_combobox, self.__is_start__ )

    
    def set_camera_devices(self, devices:list):
        """set camera divices comboBox items

        Args:
            devices (list): list of camera devices
        """
        GUIBackend.set_combobox_items(self.devices_combobox, devices)


    def get_camera_device(self,):
        """returns camera diveces that selected in combobox
        """
        return GUIBackend.get_combobox_selected(self.devices_combobox)
    
    
    def get_fps(self):
        return GUIBackend.get_input_spinbox_value(self.fps_spinbox)
    
    def get_camera_settings(self)-> dict:
        """return settings in dictionary format

        Returns:
            dict: a dictionary like {'gain': 50 ,...}
        """
        res = {}
        for sname, sfield in self.settings['camera_setting'].items():
            res[sname] = GUIBackend.get_input(sfield)
        #for multi camera ---------------
        #res['application'] = self.camera_application
        #-------------------------------------
        return res
    
    def get_all_settings(self) -> dict:
        res = self.get_camera_settings()
        res['fps'] = self.get_fps()
        res['serial_number'] = self.get_camera_device()
        return res

    def set_camera_settings(self, settings:dict):
        """set defualt values to input's fields of settings

        Args:
            settings (dict): settings paramaeters. this is a dictionary like {'gain': 50 ,...}
        """
        #for multi camera usage---------------
        #settings.pop('application')
        #-------------------------------------
        for key , value in settings.items():
            field = self.settings['camera_setting'].get(key)
            if field is not None:
                GUIBackend.set_input( field, value )

    
    def set_all_settings(self, settings:dict):
        if settings.get('serial_number'):
            GUIBackend.set_combobox_current_item(self.devices_combobox, settings['serial_number'])
        
        if settings.get('fps'):
            GUIBackend.set_input(self.fps_spinbox, settings['fps'])

        self.set_camera_settings(settings)


    def set_camera_settings_spinbox_ranges(self, args: dict):
        for name, allowable_range in args.items():
            GUIBackend.set_spinbox_range( self.settings['camera_setting'][name], allowable_range )


    def show_live_image(self, img):
        GUIBackend.set_label_image( self.live_img_lbl, img )


    def get_selected_camera_application(self,):
        return self.camera_application
    

    def __internal_save_event__(self):
        self.is_saved_massage(True)
        GUIBackend.set_disable(self.save_btn)















class algorithmSettingTabUI(commonSettingUI):

    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.ui = ui
        self.fields = {
            'threshold': self.ui.settingpage_algorithm_threshould_spinbox,
            'border':self.ui.settingpage_algorithm_border_spinbox
        }

        self.save_btn = self.ui.settingpage_algorithm_save_btn
        self.cancel_btn = self.ui.settingpage_algorithm_cancel_btn
        self.restor_default_btn = self.ui.settingpage_algorithm_restor_default_btn
        self.__change_state_connector__()
        self.save_state(True)
    
    def __change_state_connector__(self,):
        #make save button enable and wrote *not_save if any input changed
        for name, field in self.fields.items():
            if GUIBackend.is_spinbox(field):
                GUIBackend.spinbox_connector(field, lambda :self.save_state(False))

    
    def save_button_connector(self, func):
        GUIBackend.button_connector(self.save_btn, func)

    def cancel_button_connector(self, func):
        GUIBackend.button_connector(self.cancel_btn, func)
    
    def restor_button_connector(self, func):
        GUIBackend.button_connector(self.restor_default_btn, func)


    
    def get_data(self,) -> dict:
        data = {}
        for name, field in self.fields.items():
            data[name] = GUIBackend.get_input(field)
        return data
    
    def set_sata(self, data: dict):
        for name, value in data.items():
            GUIBackend.set_input( self.fields[name], value )

