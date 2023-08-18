from PagesUI.gradingRangesPageUI import gradingRangesPageUI , newStandardTabUI, allStandardsTabUI
from Database.gradingRangesDB import gradingRangesDB
import copy


class dataPasser:
    def __init__(self) -> None:
        self.all_standards = []


class gradingRangesPageAPI:
    def __init__(self, ui:gradingRangesPageUI, database:gradingRangesDB):
        #self.dataPasser = dataPasser
        self.ui = ui
        
        self.new_standard_event_func = None
        self.remove_standard_event_func = None

        self.newStandardTab = newStandardTabAPI(ui.newStandardTab, database,)
        self.allStandardTab = allStandardTabAPI(ui.allStandardsTa, database,)

        self.newStandardTab.set_new_standard_event_func(self.new_standard_added_event)
        self.allStandardTab.set_edit_event_func(self.standard_edit_event)
        self.allStandardTab.set_delete_event_func(self.standard_delete_event)
        self.newStandardTab.set_edit_complete_event_func(self.edit_complete_event)

        
    def set_new_standard_event_func(self, func):
        self.new_standard_event_func = func

    def set_remove_standard_event_func(self, func):
        self.remove_standard_event_func = func
    

    def new_standard_added_event(self,):
        """this event execute when a new standard added
        """
        self.allStandardTab.load_standards()
        if self.new_standard_event_func is not None:
            self.new_standard_event_func()

    def standard_edit_event(self,):
        """this event execute when edit button of a standard in all standards table clicked
        """
        on_edit_standard = self.allStandardTab.get_on_edit_standard()
        print(on_edit_standard)
        self.newStandardTab.enable_edit_mode(on_edit_standard)
        self.ui.open_new_standard_tab()


    def standard_delete_event(self,):
        """this event execute when edit button of a standard in all standards table clicked
        """
        if self.remove_standard_event_func is not None:
            self.remove_standard_event_func()


    def edit_complete_event(self):
        """this event execute when edit complete
        """
        self.allStandardTab.load_standards()
        self.ui.open_all_standard_tab()











class newStandardTabAPI:

    def __init__(self, ui:newStandardTabUI, database:gradingRangesDB,):
        self.ui = ui
        self.database = database
        self.edit_mode = False
        self.on_edit_standard = ''
        self.new_standard_event_func = None
        self.edit_complete_event_func = None
        self.standard_ranges = []


        self.ui.add_range_button_connector(self.add_range)
        self.ui.cancel_button_connector(self.cancel_define_new_standard)
        self.ui.save_button_connector(self.save_standard)
        self.ui.external_ranges_table_connector(self.modify_new_standard_range)
        self.ui.enable_edit_mode(self.edit_mode)
        

    def set_new_standard_event_func(self, func):
        self.new_standard_event_func = func

    def set_edit_complete_event_func(self, func):
        self.edit_complete_event_func = func


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
            if self.has_ranges_overlap(low, high, self.standard_ranges):
                self.ui.show_warning_massage("Warning: Ranges cannot overlap")
                return
    
            self.standard_ranges.append( [ low, high ])
            self.standard_ranges.sort( key= lambda x:x[0])

            self.ui.clear_input_ranges()
            self.ui.set_ranges_table_data(self.standard_ranges)

            self.ui.show_warning_massage(None)

        else:
            self.ui.show_warning_massage("Warning: Lower and Upper couldn't be equal")


    
    def modify_new_standard_range(self,idx, data, status, btn):
        if status == 'delete':
            #remove range from list
            self.standard_ranges.pop(idx)
            #refresh table
            self.ui.clear_input_ranges()
            self.ui.set_ranges_table_data(self.standard_ranges)

        
        elif status =='edit':
            pass
    

    def save_standard(self, ):
        data = {}
        new_range_name = self.ui.get_new_range_name()
        
        data['name'] = new_range_name
        data['ranges'] = self.standard_ranges

        if len(self.standard_ranges)==0:
            self.ui.show_warning_massage("Error: Couldn't save empty range. Please define at least on range")
            return
        
        if len(new_range_name)<3:
            self.ui.show_warning_massage("Error: Standard Name should be at least 3 character")
            return
        
        if self.edit_mode == False:
            if self.database.is_exist(new_range_name):
                self.ui.show_warning_massage("Error: '{}' name is already exist. please choose another name".format(new_range_name))
                return
        else:
            #name of standard edited
            if self.on_edit_standard_name != data['name'] and self.database.is_exist(new_range_name):
                self.ui.show_warning_massage("Error: '{}' name is already exist. please choose another name".format(new_range_name))
                return
                
        
        if self.has_ranges_gap(self.standard_ranges):
            flag = self.ui.show_confirm_box('Warning',
                                             'There is some gap that not defined in any ranges, Are you sure to save this?',
                                             buttons=['yes','cancel'])
            if flag == 'cancel':
                return
        
        
        
        
        if self.edit_mode:
             #remove old record
             self.database.remove(self.on_edit_standard_name)
             
  
        self.database.save(data)
        self.clear()
        if self.edit_mode == False:
            self.ui.show_success_msg("New Standard Saved")
            if self.new_standard_event_func is not None:
                self.new_standard_event_func()
        
        else:
            self.edit_mode = False
            self.on_edit_standard_name = ''
            
            if self.edit_complete_event_func is not None:
                self.edit_complete_event_func()



    def cancel_define_new_standard(self,):
            option = self.ui.show_confirm_box("Cancel", 
                                     "Area You Sure You want Cancel? all change whould be remove",
                                     buttons=['yes', 'no'])
            if option == 'no':
                return
            self.clear()
            if self.edit_mode:
                self.edit_mode = False
                if self.edit_complete_event_func is not None:
                    self.edit_complete_event_func()

    
    def clear(self,):
        #clear upper and high inputs and new range input name
        self.ui.clear_new_standard_inputs()
        #clear new range table
        self.ui.set_ranges_table_data([])
        #save new range into database
        self.standard_ranges = []
        self.ui.show_warning_massage(None)

        self.ui.enable_edit_mode(False)

        


    def enable_edit_mode(self, standard):
        self.edit_mode = True
        self.on_edit_standard_name = standard['name']
        self.standard_ranges = standard['ranges']
        self.ui.clear_input_ranges()
        self.ui.enable_edit_mode(True)
        self.ui.set_ranges_table_data(standard['ranges'])
        self.ui.set_standard_name_input( self.on_edit_standard_name )






class allStandardTabAPI:

    def __init__(self, ui:allStandardsTabUI, database:gradingRangesDB):
        self.ui = ui
        self.database = database

        
        self.standards_list = []
        self.on_edit_standard = {}
        
        self.edit_event_func = None
        self.delete_event_func = None

        #set a function for delete and edit event of all standards table
        self.ui.external_standards_table_connector(self.modify_standards_range) #Delete This line
        #show standards in table
        self.ui.set_standards_table_data(self.standards_list)
        
        #load all standards from database
        self.load_standards()        
        
        #SHOULD BE CHANGED !
        

        


    def load_standards(self):
        self.standards_list = self.database.load_all()
        self.ui.set_standards_table_data(self.standards_list)

    
            
    def set_edit_event_func(self, func):
        self.edit_event_func = func

    def set_delete_event_func(self, func):
        self.delete_event_func = func


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

                if self.delete_event_func is not None:
                    self.delete_event_func()

        
        elif status =='edit':
            self.on_edit_standard = data.copy()
            if self.edit_event_func is not None:
                self.edit_event_func()


    

    def get_on_edit_standard(self,):
        return copy.deepcopy(self.on_edit_standard)





