from dorsaPylon import Collector

from settingPageUI import settingPageUI

class settingPageAPI:
    def __init__(self, ui:settingPageUI ,database, camera):
        self.cameraSetting = cameraSettingTabAPI(ui.cameraSettingTab, database.camera_db, camera)
        self.gradingSetting = gradingSettingTabAPI(ui.gradingSettingTab, database.grading_db)

    def startup(self,):
        self.cameraSetting.startup()











class cameraSettingTabAPI:

    def __init__(self, ui ,database, cameras):
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
        self.ui.cancel_button_connector(self.cancel_setting)
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

    def cancel_setting(self):
        self.load_from_database()

    
    def cancel(self):
        settings = self.load_from_database()
        self.set_camera_setting(settings)


    def load_from_database(self,):
        camera_application = self.ui.get_selected_camera_application()
        settings = self.database.load(camera_application)
        self.ui.set_all_settings(settings)
        return settings











        
class gradingSettingTabAPI:

    def __init__(self, ui, database):
        self.ui = ui
        self.database = database
        self.new_standard_ranges = []
        self.standards_list = []
        self.on_edit_standard = {}
        #when edit a standard , this flag would be True
        self.edit_mode = False

        #load all standards from database
        self.load_standards()
        #set a function for delete and edit event of all standards table
        self.ui.external_standards_table_connector(self.modify_standards_range) #Delete This line
        #show standards in table
        self.ui.set_standards_table_data(self.standards_list)
        
        
        
        #SHOULD BE CHANGED !
        

        self.ui.add_range_button_connector(self.add_range)
        self.ui.cancel_button_connector(self.cancel_define_new_standard)
        self.ui.save_button_connector(self.save_standard)
        self.ui.external_ranges_table_connector(self.modify_new_standard_range)
        self.ui.external_standards_table_connector(self.modify_standards_range)

    def load_standards(self):
        self.standards_list = self.database.load_all()

    def cancel_define_new_standard(self,):
        self.new_standard_ranges = []
        if self.edit_mode:
            self.edit_mode = False
            self.ui.enable_edit_mode(False)


    def has_ranges_overlap(self,low, high, ranges) -> bool:
        """check new low and high has overlap with ranges

        Args:
            low (int): lower limit of new range
            high (_type_): upper limit of new range
            ranges (list): defined ranges list
        """
        for _range_ in ranges:
            if ( low < _range_[1] and high >= _range_[1] ) or ( low <= _range_[0] and high > _range_[0] ):
                return True
        return False
    

    def has_ranges_gap(self, ranges):
        """check is any gap range that has not been defined. 

        Args:
            ranges (_type_): list of ranges
        """
        for i in range(len(ranges)-1):
            if ranges[i][1] != ranges[i+1][0]:
                return True
        return False
                

    def add_range(self,):
        range_data = self.ui.get_range_inputs()
        low = range_data['lower']
        high = range_data['upper']

        if low != high:
            if self.has_ranges_overlap(low, high, self.new_standard_ranges):
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
            pass
            




    def modify_standards_range(self,idx, data, status, btn):
        if status == 'delete':
            flag = self.ui.show_confirm_box('delete', 'are you sure delete', buttons=['yes','cancel'])
            if flag == 'yes':
                #remove range from list
                deleted_standard = self.standards_list.pop(idx)
                #remove from database
                self.database.remove(deleted_standard['name'])
                #refresh table
                self.ui.set_standards_table_data(self.standards_list)

        
        elif status =='edit':
            self.edit_mode = True
            self.new_standard_ranges = data['ranges']
            self.on_edit_standard = data.copy()
            self.ui.set_ranges_table_data(self.new_standard_ranges)
            self.ui.set_standard_name_input( data['name'] )
            self.ui.enable_edit_mode(True)


    def save_standard(self, ):
        data = {}
        new_range_name = self.ui.get_new_range_name()
        
        data['name'] = new_range_name
        data['ranges'] = self.new_standard_ranges

        if len(self.new_standard_ranges)==0:
            self.ui.show_warning_massage("Error: Couldn't save empty range. Please define at least on range")
            return
        
        if len(new_range_name)<3:
            self.ui.show_warning_massage("Error: Standard Name should be at least 3 character")
            return
        
        if self.database.is_exist(new_range_name) and (not self.edit_mode):
            self.ui.show_warning_massage("Error: '{}' name is already exist. please choose another name".format(new_range_name))
            return
        
        if self.has_ranges_gap(self.new_standard_ranges):
            flag = self.ui.show_confirm_box('Warning',
                                             'There is some gap that not defined in any ranges, Are you sure to save this?',
                                             buttons=['yes','cancel'])
            if flag == 'cancel':
                return
        
        #clear upper and high inputs and new range input name
        self.ui.clear_new_standard_inputs()
        #clear new range table
        self.ui.set_ranges_table_data([])
        #save new range into database
        if self.edit_mode:
            #remove old record
            self.database.remove(self.on_edit_standard['name'])
            self.standards_list.remove(self.on_edit_standard)
  
        self.database.save(data)
        #append new range into other ranges
        self.standards_list.append(data)
        #show new stangards into standards tabel
        self.ui.set_standards_table_data(self.standards_list)
        #remove tempory new list varaible
        self.new_standard_ranges = []
        self.ui.show_warning_massage(None)


        if self.edit_mode:
            self.edit_mode = False
            self.on_edit_standard = {}
            self.ui.enable_edit_mode(False)

        #
        
