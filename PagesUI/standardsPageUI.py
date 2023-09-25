from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from PagesUI.PageUI import commonUI



class standardsPageUI():

    def __init__(self, ui) -> None:
        self.ui = ui
        self.allStandardsTa = allStandardsTabUI(ui)
        self.newStandardTab = newStandardTabUI(ui)
        
        

    def open_new_standard_tab(self,):
        GUIBackend.set_current_tab(self.ui.gradingranges_tabs, 1)
    
    def open_all_standard_tab(self,):
        GUIBackend.set_current_tab(self.ui.gradingranges_tabs, 0)




class allStandardsTabUI(commonUI):

    def __init__(self, ui) -> None:
        self.ui = ui        
        
        self.standards_table = self.ui.settingpage_grading_standards_table
        self.standards_table_external_event_function = None
        self.standards_table_headers = ['no', 'edit', 'delete', 'name', 'ranges']

        #set tables dim
        GUIBackend.set_table_dim(self.standards_table, 1 , len(self.standards_table_headers))
        #set tables headers
        GUIBackend.set_table_cheaders(self.standards_table, headers=self.standards_table_headers)

        

        #col 1 and 2 adjust to content
        GUIBackend.set_cell_width_content_adjust(self.standards_table, [0,1,2, 3])


    

    
    def external_standards_table_connector(self, func):
        """connect edit and delete button of each record in defined ranges tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, row data, 'edit' or 'delete' flag, button )
        """
        self.standards_table_external_event_function = func


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
            GUIBackend.button_connector_argument_pass( edit_btn,
                                         self.standards_table_external_event_function,
                                         args=(i, datas[i], 'edit',  edit_btn) )
            
            GUIBackend.button_connector_argument_pass( del_btn,
                                         self.standards_table_external_event_function,
                                         args =(i, datas[i], 'delete',  del_btn ) )

            #insert buttons into table
            #item_count = len(row_data)
            GUIBackend.set_table_cell_widget(self.standards_table, (i, 1), edit_btn)
            GUIBackend.set_table_cell_widget(self.standards_table, (i, 2), del_btn)
            #----------------------------------------------------------------------------

            #set row datas
            for j in range(len(row_data)):
                GUIBackend.set_table_cell_value(self.standards_table, (i, j+3), row_data[j])


    












class newStandardTabUI(commonUI):
    
    def __init__(self, ui) -> None:
        self.ui = ui

        self.ranges_table_headers = ['no', 'low (mm)', 'high (mm)', 'delete']

        self.ranges_input = {
            'lower': self.ui.settingpage_grading_low_limit_spinbox,
            'upper': self.ui.settingpage_grading_up_limit_spinbox
        }

        self.ranges_table = self.ui.settingpage_grading_ranges_table
        self.range_name_input = self.ui.settingpage_grading_name_inpt
        self.add_range_btn = self.ui.settingpage_pelletizing_add_range_btn
        self.cancel_btn = self.ui.settingpage_grading_cancel_btn
        self.save_btn = self.ui.settingpage_grading_save_btn
        self.warning_lbl = self.ui.settingpage_grading_warning_lbl
        self.ranges_table_external_event_function = None
        self.standards_groupbox = self.ui.settingpage_grading_standards_groupbox
        self.success_msg_frame = self.ui.gradingranges_new_standard_success_frame
        self.success_msg_lbl = self.ui.gradingranges_new_standard_success_lbl
        self.new_standards_groupbox = self.ui.settingpage_grading_new_standards_groupbox
        self.edit_mode_lbl = self.ui.settingpage_grading_editmode_lbl

        

        GUIBackend.set_table_dim(self.ranges_table, 1 , len(self.ranges_table_headers))
        GUIBackend.set_table_cheaders(self.ranges_table, headers=self.ranges_table_headers)
        #GUIBackend.button_connector(self.cancel_btn, self.clear_new_standard_inputs)
        GUIBackend.spinbox_connector( self.ranges_input['lower'] , self.__validation_input_ranges__ )

        self.show_warning_massage(None)
        self.show_success_msg(None)
    

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
                            * idx (_type_): row index that its button clicked
                            * dat(_type_): row datas that its button clicked
                            * status (_type_): be 'delete' when delete button clicked and 'edit' when edit button clicked
                            * btn (_type_): button object that clickeda 
        """
        self.ranges_table_external_event_function = func

    
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
            GUIBackend.button_connector_argument_pass( del_btn,
                                         self.ranges_table_external_event_function, 
                                         args = (i, datas[i], 'delete',  del_btn ) )

            #insert buttons into table
            item_count = len(row_data)
            #GUIBackend.set_table_cell_widget(self.ranges_table, (i, item_count + 1), edit_btn)
            GUIBackend.set_table_cell_widget(self.ranges_table, (i, item_count + 1), del_btn)




    def show_success_msg(self, txt):
        #diologbox = GUIComponents.confirmMessageBox('congratulations', txt, buttons=['ok'])
        #diologbox.render()
        if txt is not None:
            GUIBackend.set_wgt_visible( self.success_msg_frame, True)
            GUIBackend.set_label_text( self.success_msg_lbl, txt)
            GUIComponents.single_timer_runner(3000, lambda : self.show_success_msg(None))
        else:
            GUIBackend.set_wgt_visible(self.success_msg_frame, False)


    def enable_edit_mode(self, status):
        """changes the page appearance for editing a standard

        Args:
            status (_type_): _description_
        """
        if status:
            GUIBackend.set_wgt_visible(self.edit_mode_lbl, True)
            GUIBackend.set_groupbox_title(self.new_standards_groupbox, 'Editing')
            GUIBackend.hide_tab_header(self.ui.gradingranges_tabs, True)
            
        else:
            GUIBackend.set_wgt_visible(self.edit_mode_lbl, False)
            GUIBackend.set_groupbox_title(self.new_standards_groupbox, 'Define new Standard')
            GUIBackend.hide_tab_header(self.ui.gradingranges_tabs, False)