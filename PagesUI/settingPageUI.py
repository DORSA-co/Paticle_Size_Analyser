from guiBackend import GUIBackend
import GUIComponents





class settingPageUI:
    def __init__(self, ui) -> None:
        self.cameraSettingTab = cameraSettingTabUI(ui)
        self.gradingSettingTab = gradingSettingTabUI(ui)



class commonSettingUI:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.save_mgs = self.ui.settingpage_save_massage_lbl

    def is_saved_massage(self, is_saved):
        if is_saved:
            GUIBackend.set_label_text(self.save_mgs, "setting saved")
        else:
            GUIBackend.set_label_text(self.save_mgs, "*temp setting")

        





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









class gradingSettingTabUI(commonSettingUI):

    def __init__(self, ui) -> None:
        self.ui = ui
        super(gradingSettingTabUI, self).__init__(ui)

        self.ranges_input = {
            'lower': self.ui.settingpage_grading_low_limit_spinbox,
            'upper': self.ui.settingpage_grading_up_limit_spinbox
        }

        self.ranges_table = self.ui.settingpage_grading_ranges_table
        self.standards_table = self.ui.settingpage_grading_standards_table
        self.range_name_input = self.ui.settingpage_grading_name_inpt
        self.add_range_btn = self.ui.settingpage_pelletizing_add_range_btn
        self.cancel_btn = self.ui.settingpage_grading_cancel_btn
        self.save_btn = self.ui.settingpage_grading_save_btn
        self.warning_lbl = self.ui.settingpage_grading_warning_lbl
        self.standards_groupbox = self.ui.settingpage_grading_standards_groupbox
        self.new_standards_groupbox = self.ui.settingpage_grading_new_standards_groupbox
        self.edit_mode_lbl = self.ui.settingpage_grading_editmode_lbl

        self.ranges_table_external_event_function = None
        self.standards_table_external_event_function = None
        
        #self.ranges_table_headers = ['no', 'low (mm)', 'high (mm)', 'edit', 'delete']
        self.ranges_table_headers = ['no', 'low (mm)', 'high (mm)', 'delete']
        self.standards_table_headers = ['no', 'edit', 'delete', 'name', 'ranges']

        #set tables dim
        GUIBackend.set_table_dim(self.ranges_table, 1 , len(self.ranges_table_headers))
        GUIBackend.set_table_dim(self.standards_table, 1 , len(self.standards_table_headers))

        #set tables headers
        GUIBackend.set_table_cheaders(self.ranges_table, headers=self.ranges_table_headers)
        GUIBackend.set_table_cheaders(self.standards_table, headers=self.standards_table_headers)

        GUIBackend.button_connector(self.cancel_btn, self.clear_new_standard_inputs)
        #show saved massage
        GUIBackend.button_connector(self.save_btn, self.__saved_new_range__)
        
        GUIBackend.spinbox_connector( self.ranges_input['lower'] , self.__validation_input_ranges__ )

        #col 1 and 2 adjust to content
        GUIBackend.set_cell_width_content_adjust(self.standards_table, [0,1,2, 3,4])

        #hide warning
        self.show_warning_massage(None)

        self.enable_edit_mode(False)



    def save_button_connector(self, func):
        GUIBackend.button_connector(self.save_btn, func)


    def cancel_button_connector(self, func):
        GUIBackend.button_connector(self.cancel_btn, func)


    def show_warning_massage(self, txt):
        """show warning in ui
            - hide warning by pass 'None' to text
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.warning_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.warning_lbl, True)
            GUIBackend.set_label_text( self.warning_lbl, txt)


    def clear_new_standard_inputs(self):
        #clear 
        self.clear_input_ranges()

        GUIBackend.set_input_text(self.range_name_input,"")
        #clear tabel
        GUIBackend.clear_table( self.ranges_table )
        #insert an empty row for better ui
        GUIBackend.set_table_dim(self.ranges_table, 1 , len(self.ranges_table_headers))
    

    def set_standard_name_input(self, name):
        GUIBackend.set_input_text(self.range_name_input,name)


    def enable_edit_mode(self, status):
        """changes the page appearance for editing a standard

        Args:
            status (_type_): _description_
        """
        if status:
            GUIBackend.set_wgt_visible(self.edit_mode_lbl, True)
            GUIBackend.set_frame_max_size(self.standards_groupbox, w = 0, h=None)
            GUIBackend.set_groupbox_title(self.new_standards_groupbox, 'Editing')
            
        else:
            GUIBackend.set_wgt_visible(self.edit_mode_lbl, False)
            GUIBackend.set_frame_max_size(self.standards_groupbox, w = 16777215, h=None)
            GUIBackend.set_groupbox_title(self.new_standards_groupbox, 'Define new Standard')

    def add_range_button_connector(self, func):
        """connect add new range button into a function

        Args:
            func (_type_): clicked event function
        """        
        GUIBackend.button_connector( self.add_range_btn, func )

    
    def get_range_inputs(self)-> dict:
        """returns low and upper input fields

        Returns:
            dict: {'lower': low_value, 'upper': up_value}
        """
        data = {}
        for key in self.ranges_input.keys():
            data[key] = GUIBackend.get_input_spinbox_value( 
                self.ranges_input[key]
             )
        return data
    
    def get_new_range_name(self) -> str:
        return GUIBackend.get_input_text(self.range_name_input)

    def clear_input_ranges(self):
        for wdgt in self.ranges_input.values():
            GUIBackend.set_spinbox_value(wdgt, 0)

    
    def __validation_input_ranges__(self):
        """make upper input ranges from (lower, 2500)
        """
        low = GUIBackend.get_input_spinbox_value( self.ranges_input['lower']) 
        GUIBackend.set_spinbox_range(self.ranges_input['upper'], (low, 1e5))
        
    
    def external_ranges_table_connector(self, func):
        """connect edit and delete button of each record in defined ranges tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, row data, 'edit' or 'delete' flag, button )
        """
        self.ranges_table_external_event_function = func

    
    def ranges_table_event(self, idx, data, status, btn):
        """this function exec when edit or delete button clicked on defined ranges table

        Args:
            idx (_type_): row index that its button clicked
            data (_type_): row datas that its button clicked
            status (_type_): be 'delete' when delete button clicked and 'edit' when edit button clicked
            btn (_type_): button object that clicked
        """
        def func():
            #
            # Write Internal Code Here
            #
            self.ranges_table_external_event_function(idx, data, status, btn)
        return func


    
    def set_ranges_table_data(self, datas:list[list]):
        """insert ranges tnto defined ranges table
        Args:
            datas (list[list]): list of row lits datas
        """
        assert self.ranges_table_external_event_function is not None, "ERROR: First determine an event Function for edit and delete button by 'gradingSettingPage.external_ranges_table_connector' method "
        
        #set row count
        records_count = len(datas)
        GUIBackend.set_table_dim(self.ranges_table, row = records_count, col=None)
        
        for i, row_data in enumerate(datas):
            
            
            #set number of record
            GUIBackend.set_table_cell_value(self.ranges_table, (i, 0), i + 1)
            
            #set row datas
            for j in range(len(row_data)):
                GUIBackend.set_table_cell_value(self.ranges_table, (i, j+1), row_data[j])
            

            #define edit and delete button
            #edit_btn = GUIComponents.editButton()
            del_btn = GUIComponents.deleteButton()

            #connect buttons to event function 
            #GUIBackend.button_connector( edit_btn, self.ranges_table_event(i, datas[i], 'edit',  edit_btn) )
            GUIBackend.button_connector( del_btn, self.ranges_table_event(i, datas[i], 'delete',  del_btn ) )

            #insert buttons into table
            item_count = len(row_data)
            #GUIBackend.set_table_cell_widget(self.ranges_table, (i, item_count + 1), edit_btn)
            GUIBackend.set_table_cell_widget(self.ranges_table, (i, item_count + 1), del_btn)



    def external_standards_table_connector(self, func):
        """connect edit and delete button of each record in defined ranges tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, row data, 'edit' or 'delete' flag, button )
        """
        self.standards_table_external_event_function = func

    def standards_table_event(self, idx, data, status, btn):
        """this function exec when edit or delete button clicked on standards table

        Args:
            idx (_type_): row index that its button clicked
            data (_type_): row datas that its button clicked
            status (_type_): be 'delete' when delete button clicked and 'edit' when edit button clicked
            btn (_type_): button object that clicked
        """
        def func():
            #
            # Write Internal Code Here
            #
            self.standards_table_external_event_function(idx, data, status, btn)
        return func

    def set_standards_table_data(self, datas:list[list]):
        """insert standards range into table
        Args:
            datas (list[list]): list of row lits datas
        """
        assert self.standards_table_external_event_function is not None, "ERROR: First determine an event Function for edit and delete button by 'gradingSettingPage.externalstandards_table_connector' method "
        
        #set row count
        records_count = len(datas)
        GUIBackend.set_table_dim(self.standards_table, row=records_count, col=None)
        
        prepared_datas = []
        #make ranges into text format like (0mm , 6mm) - ,...
        for standard in datas:

            ranges_txt = ""
            for range_ in standard['ranges']:
                ranges_txt += f"( {range_[0]}mm , {range_[1]}mm )  -  "
                        
            #remove lats " - " charecter
            ranges_txt = ranges_txt[:-5]
            prepared_datas.append([ standard['name'], ranges_txt ])


        for i, row_data in enumerate(prepared_datas):
            
            #set number of record
            GUIBackend.set_table_cell_value(self.standards_table, (i, 0), i + 1)
            
            #----------------------------------------------------------------------------
            #define edit and delete button
            edit_btn = GUIComponents.editButton()
            del_btn = GUIComponents.deleteButton()

            #connect buttons to event function 
            GUIBackend.button_connector( edit_btn, self.standards_table_event(i, datas[i], 'edit',  edit_btn) )
            GUIBackend.button_connector( del_btn, self.standards_table_event(i, datas[i], 'delete',  del_btn ) )

            #insert buttons into table
            #item_count = len(row_data)
            GUIBackend.set_table_cell_widget(self.standards_table, (i, 1), edit_btn)
            GUIBackend.set_table_cell_widget(self.standards_table, (i, 2), del_btn)
            #----------------------------------------------------------------------------

            #set row datas
            for j in range(len(row_data)):
                GUIBackend.set_table_cell_value(self.standards_table, (i, j+3), row_data[j])
            

            


    def __saved_new_range__(self):
        self.is_saved_massage(True)

    def show_confirm_box(Self, title, massage, buttons):
        cmb = GUIComponents.confirmMessageBox(title, massage, buttons = buttons)
        return cmb.render()
