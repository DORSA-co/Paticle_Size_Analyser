from __future__ import annotations
from typing import Union

import numpy as np
from PySide6 import QtWidgets


from uiUtils import GUIComponents
import Constants.CONSTANTS as CONSTANTS
from uiUtils.guiBackend import GUIBackend
from PagesUI.PageUI import commonUI
from uiUtils.IO.Mouse import mouseHandeler
from uiFiles.main_UI_ui import Ui_MainWindow

from PagesUI.sectionsUI.signalUI import inputSignalUI, outputSignalUI
from PagesUI.sectionsUI.nodeSettingUI import nodeSettinUI
from backend.Utils.mapDictionary import mapDictionary
from backend.Utils.idList import idList

class settingPageUI:
    def __init__(self, ui:Ui_MainWindow) -> None:
        self.cameraSettingTab = cameraSettingTabUI(ui)
        self.algorithmSettingTab = algorithmSettingTabUI(ui)
        self.storageSettingTab = storageSettingTabUI(ui)
        self.sampleSettingTab = sampleSettingTabUI(ui)
        self.exportSettingTab = exportSettingTabUI(ui)
        self.plcSettingTab = plcSettingTabUI(ui)
        self.configSettingTab = configSettingTabUI(ui)




class commonSettingUI(commonUI):
    def __init__(self, ui:Ui_MainWindow) -> None:
        super(commonSettingUI, self).__init__()
        self.ui = ui
        self.save_mgs = self.ui.settingpage_save_massage_lbl
        self.gif_lbl = self.ui.settingpage_save_gif_lbl
        self.gif_player = GUIComponents.gifPlayer(self.gif_lbl, ':/assets/gifs/Rolling_bg.gif')

        self.save_btn = None
        self.cancel_btn = None
        self.restore_btn = None

    def __show_saved_massage__(self, is_saved):

        if is_saved:
            self.__show_is_saving__()
            GUIComponents.single_timer_runner(400, self.__show_saved__)
            
        else:
            GUIBackend.set_label_text(self.save_mgs, "*temp")
        
    def __show_is_saving__(self,):
        GUIBackend.set_label_text(self.save_mgs, "Settings  is saving")
        self.gif_player.show_and_start_animation()

    def __show_saved__(self,):
        GUIBackend.set_label_text(self.save_mgs, "")
        self.gif_player.hide_and_stop_animation()
    


    def save_state(self, is_saved):
        if not is_saved:
            GUIBackend.set_enable(self.save_btn)
            GUIBackend.set_enable(self.cancel_btn)
            self.__show_saved_massage__(is_saved)
        
        else:
            GUIBackend.set_disable(self.save_btn)
            GUIBackend.set_disable(self.cancel_btn)
            self.__show_saved_massage__(is_saved)


    def save_button_connector(self, func):
        GUIBackend.button_connector(self.save_btn, func)

    def cancel_button_connector(self, func):
        GUIBackend.button_connector(self.cancel_btn, func)
    
    def restor_button_connector(self, func):
        GUIBackend.button_connector(self.restore_btn, func)


class storageSettingTabUI(commonSettingUI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super(storageSettingTabUI, self).__init__(ui)
        self.ui = ui
        self.select_dir_btn = self.ui.settingpage_storage_select_dir_btn
        self.save_btn = self.ui.settingpage_storage_save_btn
        self.cancel_btn = self.ui.settingpage_storage_cancel_btn


        self.settings = {
            # 'database_username': self.ui.settingpage_db_username,
            # 'database_password': self.ui.settingpage_db_password,
            # 'database_host': self.ui.settingpage_db_host,
            'path': self.ui.settingpage_storage_path_input,
            'auto_clean': self.ui.settingpage_storage_auto_clean_checkbox,
            'life_time': self.ui.settingpage_storage_life_time_spinbox,
            }


    def __setting_change_connector__(self,):
        for setting_name,  field_obj in self.settings.items():
                GUIBackend.connector(field_obj,  lambda : self.save_state(False))

    def select_dir_button_connector(self, func):
        GUIBackend.button_connector(self.select_dir_btn, func)

    
    def open_select_dir_dialog(self,):
        return GUIComponents.selectDirectoryDialog()
    
    def set_path(self, path):
        GUIBackend.set_input(self.settings['path'], path)


    def get_settings(self, ):
        data = {}

        for setting_name,  field_obj in self.settings.items():
                data[setting_name] = GUIBackend.get_input(field_obj)
        return data
    
    def set_settings(self, settings: dict):
        for setting_name, value in settings.items():
            obj = self.settings[setting_name]
            if value is not None:
                GUIBackend.set_signal_connection(obj, False)
                GUIBackend.set_input(obj, value)
                GUIBackend.set_signal_connection(obj, True)

        



class sampleSettingTabUI(commonSettingUI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super(sampleSettingTabUI, self).__init__(ui)
        self.ui = ui

        self.autoname_struct_field = self.ui.settingpage_sample_auto_name_input
        self.autoname_groupbox = self.ui.settingpage_sample_auto_name_groupbox
        self.autoname_frame = self.ui.settingpage_sample_autoname_frame
        self.save_btn = self.ui.settingpage_sample_save_btn
        self.cancel_btn = self.ui.settingpage_sample_cancel_btn
        self.autoame_struct_clear_btn = self.ui.settingpage_sample_auto_name_clear_btn
        self.standards_name_combobox = self.ui.settingpage_sample_default_standard_comboxos
        self.grading_parms_combobox = self.ui.settingpage_sample_default_grading_parm_comboxos
        self.save_image_checkbox =  self.ui.settingpage_sample_save_image_checkbox

        self.custom_texts_inputs = {
            'text1': self.ui.settingpage_sample_text1_input
        }


  

        self.name_code_btns = {
            'spacer':   self.ui.settingpage_sample_spacer_code_btn,
            'dash':     self.ui.settingpage_sample_dash_code_btn,
            'year':     self.ui.settingpage_sample_year_code_btn,
            'month':    self.ui.settingpage_sample_month_code_btn,
            'day':      self.ui.settingpage_sample_day_code_btn,
            'hour':     self.ui.settingpage_sample_houre_code_btn,
            'minute':   self.ui.settingpage_sample_minute_code_btn,
            #'standard': self.ui.settingpage_sample_standard_code_btn,
            'username': self.ui.settingpage_sample_username_code_btn,
            'text1':    self.ui.settingpage_sample_text1_code_btn,

        }


        

        self.code_name_buttons_evetn_func = None

        GUIBackend.groupbox_checkbox_connector(self.autoname_groupbox, self.__enable_auto_sample_setting__)
        self.__setting_change_connector__()



    def clear_name_struct_button_connector(self, func):
        GUIBackend.button_connector(self.autoame_struct_clear_btn, func)
        


    def code_name_buttons_connector(self, func):
        self.code_name_buttons_evetn_func = func

        for name, btn in self.name_code_btns.items():
            GUIBackend.button_connector_argument_pass( btn,
                                                       self.code_name_buttons_evetn_func,
                                                       args=(name,) )

    
    def set_autoname_struct_input(self, txt:str):
        """got a text format and set it into name filed and style selected shortcode buttons

        Args:
            txt (str): name format like %DAY%_%YEAR%
        """
        GUIBackend.set_input(self.autoname_struct_field, txt)
        for btn_name, btn in self.name_code_btns.items():
            if  CONSTANTS.NAME_CODES[btn_name] in txt and btn_name not in ['spacer','dash']:
                GUIBackend.set_style(btn, GUIComponents.CODE_NAME_BUTTON_STYLE['active'])

            else:
                GUIBackend.set_style(btn , GUIComponents.CODE_NAME_BUTTON_STYLE['normal'])
                
        
    
    def __enable_auto_sample_setting__(self,):
        """show auto name settings in UI if its check box be enble
        """
        if GUIBackend.is_groupbox_checked(self.autoname_groupbox):
            GUIBackend.set_frame_max_size(self.autoname_frame,w=None, h=17662)
        else:
            GUIBackend.set_frame_max_size(self.autoname_frame,w=None, h=0)


    def __setting_change_connector__(self,):
        GUIBackend.input_text_connector( self.autoname_struct_field, lambda :self.save_state(False) )
        
        for custom_field in self.custom_texts_inputs.values():
            GUIBackend.input_text_connector(custom_field, lambda :self.save_state(False) )
        GUIBackend.groupbox_checkbox_connector(self.autoname_groupbox, lambda :self.save_state(False) )    
        GUIBackend.combobox_changeg_connector(self.standards_name_combobox, lambda :self.save_state(False) )
        GUIBackend.combobox_changeg_connector(self.grading_parms_combobox, lambda :self.save_state(False) )
        GUIBackend.checkbox_connector(self.save_image_checkbox, lambda x:self.save_state(False) )
        
        

    
    def set_settings(self, data:dict):
        for setting_name, setting_value in data.items():
            if setting_name == 'autoname_enable':
                GUIBackend.set_groupbox_checkbox(self.autoname_groupbox, setting_value)
            
            elif setting_name == 'autoname_struct':
                GUIBackend.set_input(self.autoname_struct_field, setting_value)
            
            elif setting_name == 'default_standard':
                GUIBackend.set_combobox_current_item(self.standards_name_combobox, setting_value)

            elif setting_name == 'save_image':
                GUIBackend.set_checkbox_value(self.save_image_checkbox, setting_value)

            elif setting_name == 'default_grading_parm':
                for key, value in CONSTANTS.Sample.GRADING_PARMS.items():
                    if value == setting_value:
                        GUIBackend.set_combobox_current_item(self.grading_parms_combobox, key)
                        break
            
            elif setting_name in self.custom_texts_inputs.keys():
                GUIBackend.set_input_text(self.custom_texts_inputs[setting_name], setting_value)
    
    def get_settings(self):
        data = {}
        data['autoname_struct'] = GUIBackend.get_input(self.autoname_struct_field)
        data['autoname_enable'] = GUIBackend.is_groupbox_checked(self.autoname_groupbox)
        data['default_standard'] = GUIBackend.get_combobox_selected(self.standards_name_combobox)
        data['default_grading_parm'] = CONSTANTS.Sample.GRADING_PARMS[
                    GUIBackend.get_combobox_selected(self.grading_parms_combobox)
                    ]
        
        data['save_image'] = GUIBackend.get_checkbox_value(self.save_image_checkbox)
        for custom_text in self.custom_texts_inputs.keys():
            data[custom_text] = GUIBackend.get_input(self.custom_texts_inputs[custom_text])

        return data

    def set_standards(self, items:list[str]):
        GUIBackend.set_combobox_items(self.standards_name_combobox, items)
    
    def set_grading_parms_items(self, items:list[str]):
        GUIBackend.set_combobox_items(self.grading_parms_combobox, items)
    
    # def set_grading_parm(self, parm_name):
    #     GUIBackend.set_combobox_current_item(self.grading_parms_combobox, parm_name)
    



class cameraSettingTabUI(commonSettingUI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super(cameraSettingTabUI, self).__init__(ui)
        self.ui = ui
        self.mouseHandeler = mouseHandeler()

        self.devices_combobox = self.ui.settingpage_camera_device_combobox
        self.fps_spinbox = self.ui.settingpage_camera_fps_spinbox
        self.camera_start_btn = self.ui.settingpage_camera_start_btn
        self.save_btn = self.ui.settingpage_camera_save_btn
        self.cancel_btn = self.ui.settingpage_camera_cancel_btn
        self.restore_btn = self.ui.settingpage_camera_restore_btn
        self.live_img_lbl = self.ui.settingpage_camera_live_lbl
        self.port_connection_lbl = self.ui.settingpage_camera_port_connection_lbl
        self.serial_retry_btn = self.ui.settingpage_camera_serial_retry_btn
        
        self.point_color_value = self.ui.settingpage_camera_color_value_lbl
        self.point_color_image = self.ui.settingpage_camera_color_img_lbl

        self.__is_start__ = False
        self.__connection_event_function__ = None
        self.__change_setting_event_function__ = None
        self.__image_mouse_event_func__ = None
        self._serial_number = ''
        self.set_color_rgb(0)

        


        self.camera_application = 'standard'

        self.settings = {
            #features that can't be changed in grabbing    
            'camera_setting':{
                'width': self.ui.settingpage_camera_width_spinbox,
                'height': self.ui.settingpage_camera_height_spinbox,
                'gain': self.ui.settingpage_camera_gain_spinbox,
                'exposure': self.ui.settingpage_camera_exposure_spinbox,
                'synchronize': self.ui.settingpage_camera_synchronizer_combobox
            },
            'others':{
                'fps': self.ui.settingpage_camera_fps_spinbox,
                'port': self.ui.settingpage_camera_ports_combobox,
                'serial_number': self.ui.settingpage_camera_device_combobox,
                
            }
            #'fps': self.ui.settingpage_camera_fps_spinbox,
            }

        self.start_stop_icon = {
            True: ":/assets/icons/stop50.png",
            False: ":/assets/icons/play-48.png"
        }

        self.fields_enable_status = {
            True: ['gain', 'exposure'],
            False: ['width','height', ]
        }

        GUIBackend.button_connector(self.camera_start_btn, self.__internal_start_event__)
        
        self.__mange_fields_enable__()
        self.__settings_change_connector__()

    def connect_mouse_image_event(self, func):
        self.image_mouse_event_func = func

    def set_color_rgb(self, value):
        GUIBackend.set_label_text(self.point_color_value, str(value))
        img = np.zeros((50,50), dtype=np.uint8)
        img[:,:] = int(value)
        pixmap = GUIBackend.set_label_image(self.point_color_image, img)
        GUIBackend.fit_label_to_pixmap(self.point_color_image, pixmap  )
    
    def reset(self):
        self.__is_start__ = False
        #change button icon
        GUIBackend.set_button_icon(self.camera_start_btn, self.start_stop_icon[self.__is_start__])
        #enable and disable setting fields
        self.__mange_fields_enable__()
        GUIBackend.set_disable(self.save_btn)
        self.load_default_image()

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
    
    def serial_retry_button_connector(self, func):
        GUIBackend.button_connector(self.serial_retry_btn, func)

    def __settings_change_connector__(self,):
        """connect all input fields of setting into an internal function
        """
        for setting_type in self.settings.keys():
            for field_name, field in self.settings[setting_type].items():
                # if field_name =='serial_number':
                #     continue
  
                GUIBackend.connector(field, self.__internal_change_setting_event__(setting_type, field_name))
    
    def change_camera_connector(self, func):
        GUIBackend.combobox_changeg_connector(self.settings['others']['serial_number'], func)

    
    def __internal_change_setting_event__(self,setting_group, setting_name):
        """got setting that changed and pass it to external function self.__change_setting_event_function__ as an event
        this function connected to change setting input fields and calledc automaticly

        Args:
            setting_group (_type_): group_setting can be 'other' or 'camera_setting'. 'camera_setting' is for camera parameters
            setting_name (_type_): name of setting that changed.
        """
        def func():
            GUIBackend.set_enable(self.save_btn)
            self.save_state(False)
            #assert self.change_setting_event_connector is not None, "No Function Event determind. use cameraSettingTab.change_setting_event_connector method to do it"
            value = GUIBackend.get_input(self.settings[setting_group][setting_name])
            arg = {setting_name:value}
            if self.__change_setting_event_function__ is not None:
                self.__change_setting_event_function__(setting_group, self.camera_application, arg)
        return func

    def stop(self):
        if self.__is_start__:
            self.__internal_start_event__()

    
    def load_default_image(self, ):
        GUIBackend.set_label_image(self.live_img_lbl, CONSTANTS.IMAGES.NO_IMAGE)



    
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

        if not self.__is_start__:
            self.load_default_image()


    def __mange_fields_enable__(self):
        """mange which fields be enable when change start, stop
        """
        #enable fields corespond to __is_srart__
        for fields_name in self.fields_enable_status[self.__is_start__]:
            GUIBackend.set_enable(self.settings['camera_setting'][fields_name])

        #disable other fields corespond to __is_srart__
        for fields_name in self.fields_enable_status[not(self.__is_start__)]:
            GUIBackend.set_disable(self.settings['camera_setting'][fields_name])

        GUIBackend.set_disable_enable( self.devices_combobox, not(self.__is_start__) )

    
    def set_camera_devices(self, devices:list, current=None):
        """set camera divices comboBox items

        Args:
            devices (list): list of camera devices
        """
        GUIBackend.set_signal_connection(self.devices_combobox, False)

        current_device = GUIBackend.get_combobox_selected(self.devices_combobox)
        GUIBackend.set_combobox_items(self.devices_combobox, devices)

        if current_device!='':
            if current is not None:
                GUIBackend.set_combobox_current_item(self.devices_combobox, current)
            
            else:
                GUIBackend.set_combobox_current_item(self.devices_combobox, current_device)

        else:
             GUIBackend.set_combobox_current_item(self.devices_combobox, self._serial_number)

        GUIBackend.set_signal_connection(self.devices_combobox, True)

    def set_ports_items(self, ports:list[str]):
        GUIBackend.set_combobox_items(self.settings['others']['port'], ports)

    def set_synchronize_items(self, items:list[str]):
        GUIBackend.set_combobox_items(self.settings['camera_setting']['synchronize'], items)


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
        res['port'] = GUIBackend.get_combobox_selected(self.settings['others']['port'])
        #res['synchronize'] = GUIBackend.get_combobox_selected(self.settings['camera_setting']['synchronize'])
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
        for name in self.settings['others']:
            if settings.get(name):
                GUIBackend.set_input(self.settings['others'][name], settings[name] )

        self.set_camera_settings(settings)


    def set_camera_settings_spinbox_ranges(self, args: dict):
        for name, allowable_range in args.items():
            GUIBackend.set_spinbox_range( self.settings['camera_setting'][name], allowable_range )


    def show_live_image(self, img):
        if img is not None:
            pixmap = GUIBackend.set_label_image( self.live_img_lbl, img )
            GUIBackend.fit_label_to_pixmap(self.live_img_lbl, pixmap)
            self.mouseHandeler.connect_all(self.live_img_lbl, self.image_mouse_event_func)


    def get_selected_camera_application(self,):
        return self.camera_application
    
    def disable_save_btn(self,):
        GUIBackend.set_disable(self.save_btn)


    def set_com_connection_status(self, status):
        if status:
            GUIBackend.set_label_text(self.port_connection_lbl, 'Ok')
            GUIBackend.set_style(self.port_connection_lbl, "color:rgb(58, 209, 154);")
            
        else:
            GUIBackend.set_label_text(self.port_connection_lbl, 'Not Ok')
            GUIBackend.set_style(self.port_connection_lbl, "color:rgb(255, 95, 84);")
            



class algorithmSettingTabUI(commonSettingUI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super().__init__(ui)
        self.ui = ui
        self.fields = {
            'threshold': self.ui.settingpage_algorithm_threshould_spinbox,
            'border':self.ui.settingpage_algorithm_border_spinbox
        }

        self.save_btn = self.ui.settingpage_algorithm_save_btn
        self.cancel_btn = self.ui.settingpage_algorithm_cancel_btn
        self.restore_btn = self.ui.settingpage_algorithm_restor_default_btn
        self.__change_state_connector__()
    
    def __change_state_connector__(self,):
        #make save button enable and wrote *not_save if any input changed
        for name, field in self.fields.items():
            if GUIBackend.is_spinbox(field):
                GUIBackend.spinbox_connector(field, lambda :self.save_state(False))


    
    def get_data(self,) -> dict:
        data = {}
        for name, field in self.fields.items():
            data[name] = GUIBackend.get_input(field)
        return data
    
    def set_sata(self, data: dict):
        for name, value in data.items():
            GUIBackend.set_input( self.fields[name], value )




class exportSettingTabUI(commonSettingUI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super(exportSettingTabUI , self).__init__(ui)
        self.ui = ui
        self.select_dir_btn = self.ui.settingpage_storage_select_dir_btn
        self.save_btn = self.ui.settingpage_export_save_btn
        self.cancel_btn = self.ui.settingpage_export_cancel_btn
        self.restore_btn = self.ui.settingpage_export_restore_btn

        self.load_report_excel_btn = self.ui.settingpage_export_load_report_excel_btn
        self.load_compare_excel_btn = self.ui.settingpage_export_load_compare_excel_btn
        self.open_report_excel_btn = self.ui.settingpage_export_open_report_excel_btn
        self.open_compare_excel_btn = self.ui.settingpage_export_open_compare_excel_btn

        self.settings = {
            'report_excel': self.ui.settingpage_export_report_excel_path_input,
            'compare_excel': self.ui.settingpage_export_compare_excel_path_input
        }

        self.__setting_change_connector__()

    def __setting_change_connector__(self,):
        for setting_name,  field_obj in self.settings.items():
                GUIBackend.connector(field_obj,  lambda : self.save_state(False))


    def select_dir_buttons_connector(self, func):
        GUIBackend.button_connector_argument_pass(self.load_report_excel_btn, 
                                                  func, 
                                                  ('report_excel',) )

        GUIBackend.button_connector_argument_pass(self.load_compare_excel_btn, 
                                                  func, 
                                                  ('compare_excel',) )
        
    def open_export_file_buttons_connector(self, func):
        GUIBackend.button_connector_argument_pass(self.open_report_excel_btn, 
                                                  func, 
                                                  ('report_excel',) )

        GUIBackend.button_connector_argument_pass(self.open_compare_excel_btn, 
                                                  func, 
                                                  ('compare_excel',) )
    
    def open_select_file_dialog(self,):
        return GUIComponents.selectFileDialog('Excel', '.xlsx')[0]
    
    def set_setting(self, settings:dict[str:str]):
        for name, value in settings.items():
            GUIBackend.set_input(self.settings[name], value)

    def get_settings(self, )-> dict:
        data = {}
        for name,  field_obj in self.settings.items():
                data[name] = GUIBackend.get_input(field_obj)
        return data

    




class plcSettingTabUI(commonSettingUI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super(plcSettingTabUI, self).__init__(ui)
        self.ui = ui
       
        self.save_btn = self.ui.settingpage_plc_save_btn
        self.cancel_btn = self.ui.settingpage_plc_cancel_btn
        # self.restore_btn = self.ui.settingpage_export_restore_btn


        self.ip_sections = {
            'ip1': self.ui.settingpage_plc_ip1_input,
            'ip2': self.ui.settingpage_plc_ip2_input,
            'ip3': self.ui.settingpage_plc_ip3_input,
            'ip4': self.ui.settingpage_plc_ip4_input,

            }
        
        self.settings = {
            'check_connection_ns': self.ui.settingpage_plc_ns_check_connection_inpt,
            'check_connection_i': self.ui.settingpage_plc_i_check_connection_inpt

        }

        self.nodes_ui: list[nodeSettinUI] = []
        GUIBackend.button_connector(self.ui.settingpage_plc_add_node_btn, self.add_node)
        self.__internal_change_setting_connector()
        
        
    
    def __internal_change_setting_connector(self,):
        for ip_sec in self.ip_sections:
            GUIBackend.connector(self.ip_sections[ip_sec], self.__internal_change_setting_event)
        for field in self.settings.values():
            GUIBackend.connector(self.ip_sections[ip_sec], self.__internal_change_setting_event)


    def __internal_change_setting_event(self,):
        self.save_state(False)


    def get_ip(self,) -> str:
        ip = ""
        for section in ['ip1', 'ip2', 'ip3', 'ip4']:
            num = GUIBackend.get_input(self.ip_sections[section])
            ip = ip + num + "."

        #remove last .
        ip = ip[:-1]
        return ip
    
    def set_ip(self, ip:str):
        nums = ip.split('.')
        for i, section in enumerate(['ip1', 'ip2', 'ip3', 'ip4']):
            GUIBackend.set_input(self.ip_sections[section], nums[i])

    def add_node(self,):
        node = nodeSettinUI()
        self.nodes_ui.append(node)
        node.remove_button_connector(self.remove_node_event)
        node.change_setting_connector(self.change_node_settings_event)

        # layout = self.ui.nodesScrollAreaContent.layout()
        # #insert in bottom of layout but before of add button
        # layout.insertWidget(layout.count() - 2, node)
        GUIBackend.insert_widget(self.ui.nodesScrollAreaContent,
                                 node,
                                 pos=-2)

        #scroll to bottom
        GUIComponents.single_timer_runner(150,self.scroll_to_bottom)

    def scroll_to_bottom(self,):
        scroll_bar = self.ui.nodesScrollArea.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())


        

    def remove_node_event(self, node:nodeSettinUI):
        
        layout = self.ui.nodesScrollAreaContent.layout()
        layout.removeWidget(node)

        self.nodes_ui.remove(node)
        node.deleteLater()
        self.save_state(False)


    def change_node_settings_event(self,):
        self.save_state(False)

   
    def set_settings(self, data:dict):
        ip = data.pop('ip')
        self.set_ip(ip)

        for name, value in data.items():
            GUIBackend.set_input(self.settings[name], value)
    
    def get_settings(self ) -> dict:
        data = {}
        data['ip'] = self.get_ip()
        
        for name, field in self.settings.items():
            value = GUIBackend.get_input(field)
            data[name] = value
        return data
    
    def set_nodes_settings(self, nodes_settings:list[dict]):
        for i, setting in enumerate(nodes_settings):
            if i >= len(self.nodes_ui):
                self.add_node()
        
            self.nodes_ui[i].set_settings(setting)

    def get_nodes_settings(self, ) -> list[dict]:
        res = []
        for nu in self.nodes_ui:
            setting = nu.get_settings()
            res.append(setting)
        return res
    
    






class configSettingTabUI(commonSettingUI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super(configSettingTabUI, self).__init__(ui)
        self.ui = ui
       
        self.save_btn = self.ui.settingpage_config_save_btn
        self.cancel_btn = self.ui.settingpage_config_cancel_btn

        

        self.read_signals:idList= []
        self.write_signals:idList = []

        self.mapDict = mapDictionary(
                                    {   'start_mode': {
                                            'timer':'Timer',
                                            'signal': 'Signal',
                                        },

                                        'stop_mode': {
                                            'timer':'Timer',
                                            'signal': 'Signal',
                                            'detection': 'Detection',
                                        },

                                        'lens_type': {
                                            'tele':'Telecentric',
                                            'standard': 'Standard',
                                        },

                                        'fps_regulator':{
                                            'plc': 'PLC',
                                            'micro': 'Microcotroller',
                                        }
                                    }
                                )

        self.signals_wgt = {
            'start_signals': {'add': self.ui.config_start_system_signals_add_btn,
                      'scroll_content': self.ui.config_start_system_signals_scroll_contents,
                      'scroll_area':    self.ui.config_start_system_signals_scroll_area,
                      'type': 'input',
                      },

            'permission_signals': {'add': self.ui.config_permisions_signals_add_btn,
                      'scroll_content': self.ui.config_permisions_signals_scroll_contents,
                      'scroll_area':    self.ui.config_permisions_signals_scroll_area,
                      'type': 'input',
                      },

            'stop_signals': {'add': self.ui.config_stop_system_signals_add_btn,
                      'scroll_content': self.ui.config_stop_system_signals_scroll_contents,
                      'scroll_area':    self.ui.config_stop_system_signals_scroll_area,
                      'type': 'input',
                      },

            'signals1': {'add': self.ui.config_output_signals1_add_btn,
                      'scroll_content': self.ui.config_output_signals1_scroll_contents,
                      'scroll_area':    self.ui.config_output_signals1_scroll_area,
                      'type': 'output',
                      },

            'signals2': {'add': self.ui.config_output_signals2_add_btn,
                      'scroll_content': self.ui.config_output_signals2_scroll_contents,
                      'scroll_area':    self.ui.config_output_signals2_scroll_area,
                      'type': 'output',
                      },

            'signals3': {'add': self.ui.config_output_signals3_add_btn,
                      'scroll_content': self.ui.config_output_signals3_scroll_contents,
                      'scroll_area':    self.ui.config_output_signals3_scroll_area,
                      'type': 'output',
                      },
        }

        self.timer_indicators = {
            'start': self.ui.config_start_timer_indicator_label,
            'delay': self.ui.config_delay_timer_indicator_label,
            'stop':  self.ui.config_stop_timer_indicator_label,

        }

        self.signals_ui: dict[str, idList[Union[outputSignalUI, inputSignalUI]]] = {
            'start_signals':idList(),
            'permission_signals': idList(),
            'stop_signals': idList(),
            'signals1': idList(),
            'signals2': idList(),
            'signals3': idList(),
        }    
        
        self.settings = {
            'lens_type': self.ui.config_lens_type_combobox,
            'pixel_size': self.ui.config_pixel_size,
            'lens_magnification': self.ui.config_lens_magnification,
            'fps_regulator': self.ui.config_fps_regulator_combobox,
            'plc_enable': self.ui.config_plc_enable_checkbox,
            'auto_run_enable': self.ui.config_auto_run_checkbox,

            'stop_emergency_timer_enable': self.ui.config_stop_emergency_timer_checkbox,
            'stop_emergency_timer_time': self.ui.config_stop_emergency_timer_spinbox,

            'start_manual': self.ui.config_start_manual_checkbox,
            'start_mode': self.ui.config_start_mode_comboBox,
            'start_period_time': self.ui.config_start_system_period_spinbox,
            'start_delay': self.ui.config_start_latency_spinbox,
            'stop_manual': self.ui.config_stop_manual_checkbox,
            'stop_mode': self.ui.config_stop_mode_comboBox,
            'stop_delay': self.ui.config_stop_system_delay_spinbox,

            'stop_algo_min_time': self.ui.confog_stop_algo_minimum_run_time,
            'stop_algo_thresh_size': self.ui.confog_stop_algo_thresh_size,
            'stop_algo_timout': self.ui.confog_stop_algo_timout,
        }

        self.step_containers = {
            'start': self.ui.config_start_frame,
            'permission': self.ui.config_permissions_frame,
            'delay': self.ui.config_delay_frame,
            'signals1': self.ui.config_signal1_frame,
            'signals2': self.ui.config_signal2_frame,
            'signals3': self.ui.config_signal3_frame,
            'stop': self.ui.config_stop_frame,
        }

        self.__add_btns_connector()
        GUIBackend.combobox_changeg_connector(self.ui.config_start_mode_comboBox, 
                                              self.start_mode_change)
        
        GUIBackend.combobox_changeg_connector(self.ui.config_stop_mode_comboBox, 
                                              self.stop_mode_change)
        
        GUIBackend.combobox_changeg_connector(self.ui.config_lens_type_combobox, 
                                              self.lens_type_change)
        
        GUIBackend.checkbox_connector(self.ui.config_stop_emergency_timer_checkbox,
                                                    self.stop_emergency_timer_visibility,
                                    )
        
        self.__setup()
    
    def __setup(self,):
        items = self.mapDict.get_values('start_mode')
        GUIBackend.set_combobox_items(self.ui.config_start_mode_comboBox, items)

        items = self.mapDict.get_values('stop_mode')
        GUIBackend.set_combobox_items(self.ui.config_stop_mode_comboBox, items)

        items = self.mapDict.get_values('lens_type')
        GUIBackend.set_combobox_items(self.ui.config_lens_type_combobox, items)

        self.stop_emergency_timer_visibility(False)

    
    def go_live_btn_connector(self, func):
        GUIBackend.button_connector(self.ui.config_go_live_btn, func)

    def start_mode_change(self,):
        mode_front = GUIBackend.get_input(self.ui.config_start_mode_comboBox)    
        mode_backend = self.mapDict.value2key('start_mode', mode_front)
        page = None
        if mode_backend == 'timer':
            page = self.ui.config_start_timer_page
            
        elif mode_backend == 'signal':
            page = self.ui.config_start_signal_page
            
        if page:
            GUIBackend.set_stack_widget_page(self.ui.config_start_system_settings_stackwidget,page)
    
    def stop_emergency_timer_visibility(self, flag):
        GUIBackend.set_wgt_visible(self.ui.config_stop_emergency_timer_spinbox, flag )

    def stop_mode_change(self,):
        mode_front = GUIBackend.get_input(self.ui.config_stop_mode_comboBox)    
        mode_backend = self.mapDict.value2key('stop_mode', mode_front)
        
        page = None
        if mode_backend == 'timer':
            page = self.ui.config_stop_timer_page
            GUIBackend.set_wgt_visible(self.ui.config_stop_emergency_timer_frame, False)

        elif mode_backend == 'signal':
            page = self.ui.config_stop_signal_page
            GUIBackend.set_wgt_visible(self.ui.config_stop_emergency_timer_frame, True)

        elif mode_backend == 'detection':
            page = self.ui.config_stop_detection_page
            GUIBackend.set_wgt_visible(self.ui.config_stop_emergency_timer_frame, True)


        if page:
            GUIBackend.set_stack_widget_page(self.ui.config_stop_system_settings_stackwidget,page)


    def lens_type_change(self,):
        lens_type = GUIBackend.get_input(self.ui.config_lens_type_combobox)    
        lens_type = self.mapDict.value2key('lens_type', lens_type)


        if lens_type == 'tele':
            GUIBackend.set_wgt_visible(self.ui.config_tele_lens_setting_frame, True)
        else:
            GUIBackend.set_wgt_visible(self.ui.config_tele_lens_setting_frame, False)

        

    def __add_btns_connector(self,):
        for step_name in self.signals_wgt.keys():
            GUIBackend.button_connector_argument_pass(self.signals_wgt[step_name]['add'],
                                                      self.add_signal_event,
                                                      args = (step_name,)
                                                      )

    def add_signal_event(self, step_name:str) -> Union[inputSignalUI, outputSignalUI]:
        scroll_content = self.signals_wgt[step_name]['scroll_content']

        

        if self.signals_wgt[step_name]['type'] == 'input':
            signal_ui = inputSignalUI(step_name)
            signal_ui.signal_name_connector(self.__signal_name_changed_event)
            #set names of signals into signal name combobox
            signal_ui.set_signals_items(self.read_signals.ids())
        else:
            signal_ui = outputSignalUI(step_name)
            #first connect name combobox changed event
            signal_ui.signal_name_connector(self.__signal_name_changed_event)
            #set names of signals into signal name combobox
            signal_ui.set_signals_items(self.write_signals.ids())

        signal_ui.remove_button_connector(self.remove_signal_event)

        
        
        self.signals_ui[step_name].append( signal_ui, signal_ui.id  )

        GUIBackend.insert_widget(scroll_content,
                                 signal_ui,
                                 pos=-2
                                 )
        
        GUIComponents.single_timer_runner(150, lambda: self.__scroll_to_bottom(step_name))

        return signal_ui
    
    def __signal_name_changed_event(self,node_name, signal_ui: Union[outputSignalUI, inputSignalUI]):
        #node_name = signal_ui.get_settings()['name']
        if not node_name:
            return
        
        node_setting = {}
        if isinstance(signal_ui, outputSignalUI):
            node_setting = self.write_signals.get_by_id(node_name)

        elif isinstance(signal_ui, inputSignalUI):
            node_setting = self.read_signals.get_by_id(node_name)
        
        signal_ui.set_data_type(node_setting['data_type'])



    def __scroll_to_bottom(self, step_name:str):
        scroll_bar = self.signals_wgt[step_name]['scroll_area'].verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())

    def update_signals_items(self, read_signals:idList, write_signals:idList):
        #read and write signals are idList that the id are signals names and values are dictionary of signals setting
        self.read_signals = read_signals
        self.write_signals = write_signals

        for step_name in self.signals_wgt.keys():
            signal_ui: Union[inputSignalUI, outputSignalUI]
            for signal_ui in self.signals_ui[step_name].values():

                if self.signals_wgt[step_name]['type'] == 'input':
                    signal_ui.set_signals_items(self.read_signals.ids())
                elif self.signals_wgt[step_name]['type'] == 'output':
                    signal_ui.set_signals_items(self.write_signals.ids())


    def remove_signal_event(self, signal:Union[inputSignalUI, outputSignalUI]):
        
        step_name = signal.step_name
        scroll_content = self.signals_wgt[step_name]['scroll_content']
        layout = scroll_content.layout()
        layout.removeWidget(signal)

        self.signals_ui[step_name].remove_by_id(signal.id)
        signal.deleteLater()        


    def get_settings(self,) -> dict:
        res = {}
        for name, field in self.settings.items():
            res[name] = GUIBackend.get_input(field)

        res['lens_type'] = self.mapDict.value2key('lens_type', res['lens_type'])
        res['start_mode'] = self.mapDict.value2key('start_mode', res['start_mode'])
        res['stop_mode'] = self.mapDict.value2key('stop_mode', res['stop_mode'])
        res['fps_regulator'] = self.mapDict.value2key('fps_regulator', res['fps_regulator'])



        
        for step_signal in self.signals_ui.keys():
            res[step_signal] = []
            su: Union[inputSignalUI, outputSignalUI]
            for su in self.signals_ui[step_signal]:
                res[step_signal].append( 
                    su.get_settings()
                )
        
        return res


    def set_settings(self, data:dict) -> dict:
        res = {}
        
        data['start_mode'] = self.mapDict.key2value('start_mode', data['start_mode'])
        data['stop_mode'] = self.mapDict.key2value('stop_mode', data['stop_mode'])
        data['lens_type'] = self.mapDict.key2value('lens_type', data['lens_type'])

        for name, field in self.settings.items():
            if data.get(name):
                res[name] = GUIBackend.set_input(field, data[name])

        
        for step_signal in self.signals_ui.keys():
            #-----------------------------------------------------
            # remove prev signals
            for i in range(self.signals_ui[step_signal].count()):
                su = self.signals_ui[step_signal][0]
                self.remove_signal_event(su)
            #-----------------------------------------------------
            for signal_setting in data[step_signal]:
                node_ui = self.add_signal_event(step_signal)
                old_id = node_ui.id
                node_ui.set_settings(signal_setting)
                new_id = node_ui.id
                self.signals_ui[step_signal].change_id(old_id, new_id)
        

    def set_timer_indicator(self, name:str, t: int):
        h = t//3600
        t = t - h * 3600
        m = t//60
        s = t - m * 60

        str_time = f"{h:02}:{m:02}:{s:02}"
        
        GUIBackend.set_label_text(self.timer_indicators[name],
                                  str_time)
        
    def set_nodes_online_state(self, name:str, log:list[dict]):
        converter = {
            'start': 'start_signals',
            'permission': 'permission_signals'
        }

        name = converter[name]
        signal_ui:Union[inputSignalUI, outputSignalUI]
        for lg in log:
            signal_ui = self.signals_ui[name].get_by_id(lg['id'])
            signal_ui.set_indicator_value(lg['value'])
            if lg['result']:
                signal_ui.set_online_state('active')
            else:
                signal_ui.set_online_state('not_active')
            
    def set_nodes_onile_reset(self,):
        su:Union[inputSignalUI, outputSignalUI]
        for signals in self.signals_ui.values():
            for su in signals.values():
                if isinstance(su, inputSignalUI):
                    su.set_online_state('off')
                    

    def enable_congig_setting(self, flag):
        for frame in self.step_containers.values():
            self.__disabled_singular_widgets(frame, flag)
            # GUIBackend.set_disable_enable(frame, flag)
    
    def __disabled_singular_widgets(self, widget, state:bool):
        
        if isinstance(widget, (QtWidgets.QSpinBox, 
                                QtWidgets.QDoubleSpinBox,
                                QtWidgets.QLabel, 
                                QtWidgets.QDateEdit,
                                QtWidgets.QPushButton,
                                QtWidgets.QLineEdit,
                                QtWidgets.QComboBox,
                                QtWidgets.QCheckBox)):
            GUIBackend.set_disable_enable(widget, state)
            return
            
        else:
            childrens = widget.children()
        
            for ch in childrens:
                self.__disabled_singular_widgets(ch, state)


                
                






    def set_step_state(self, step_name:str,state:str):
        if step_name == 'all':
            for frame in self.step_containers.values():
                GUIBackend.set_dynalic_property(frame, 'state', state, repolish_style=True)
        
        else:
            GUIBackend.set_dynalic_property(self.step_containers[step_name], 'state', state, repolish_style=True)

    
    def set_playing_button_state(self, playing:bool):
        GUIBackend.set_dynalic_property(self.ui.config_go_live_btn, 'playingStyle', playing, repolish_style=True)
