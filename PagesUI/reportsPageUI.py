from datetime import datetime

from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat
from PagesUI.dialogWindows.proggressDialogUI import proggressDialogUI
from PagesUI.PageUI import commonUI
from dialogWindows.autoRebuildDialogUI import autoRebuildDialogUI




class reportsPageUI(commonUI):

    def __init__(self, ui):
        self.ui = ui
        self.autoRebuildDialog = autoRebuildDialogUI()
        self.deleteSamplesDialog = proggressDialogUI()

        
        self.deleteSamplesDialog.setup('Remove samples','', operation_name='removed')

        
        
        self.apply_filter_btn = self.ui.reportpage_apply_filters_btn
        self.samples_table = self.ui.reportpage_samples_table
        self.compare_btn = self.ui.reportpage_compare_btn
        self.compare_standards_combobox = self.ui.reportpage_compare_standards_combobox
        self.select_all_checkbox = self.ui.reportspage_all_checkbox
        self.delete_selections_btn = self.ui.reportspage_delete_selections_btn
        self.rebuild_btn = self.ui.reportpage_rebuild_btn

        #-----------------name filter--------------
        self.name_filter_input = self.ui.reportpage_filtername_input
        #--------------username filter-------------
        self.username_filter_input = self.ui.reportpage_filterusername_input
        #----------------date filter---------------
        self.start_date_filter = self.ui.reportpage_start_date_dateedit
        self.end_date_filter = self.ui.reportpage_end_date_dateedit
        #---------------standard filter------------
        self.standards_filter_warning_lbl = self.ui.reportpage_filterstandards_warning_lbl
        self.standards_filter_table = self.ui.reportpage_standards_filter_table
        #----------------ranges filter-------------
        self.ranges_filter_warning_lbl = self.ui.reportpage_filterranges_warning_lbl
        self.ranges_filter_standards_combobox = self.ui.reportpage_filter_standards_combobox
        self.ranges_filter_table = self.ui.reportpage_standards_filter_ranges_table
        

        self.ranges_filter = []

        self.filters_groupbox = {
            'name': self.ui.reportpage_filtername_groupbox,
            'username': self.ui.reportpage_filterusername_groupbox,
            'date': self.ui.reportpage_filterdate_groupbox,
            'standards': self.ui.reportpage_filterstandards_groupbox,
            'ranges': self.ui.reportpage_filterranges_groupbox,
        
        }

        self.filters_frame = {
            'name': self.ui.reportpage_filtername_frame,
            'username': self.ui.reportpage_filterusername_frame,
            'date': self.ui.reportpage_filterdate_frame,
            'standards': self.ui.reportpage_filterstandards_frame,
            'ranges': self.ui.reportpage_filterranges_frame,
        
        }

        self.standards_filter_checkbox = {}
        self.samples_table_checkbox = {}
        self.samples_table_headers= ['-', 'name', 'standard', 'date', 'time', 'username', 'delete', 'see' ]
        self.external_see_report_event_func = None
        self.external_delete_samples_event_func = None


        GUIBackend.set_table_dim(self.samples_table, row=None, col = len(self.samples_table_headers))
        GUIBackend.set_table_cheaders(self.samples_table, self.samples_table_headers)
        GUIBackend.set_cell_width_content_adjust(self.samples_table)
        
        GUIBackend.set_date_input(self.end_date_filter, datetime.now())
        GUIBackend.set_date_input(self.start_date_filter, datetime.now())
        GUIBackend.date_input_connector(self.start_date_filter, self.__internal_date_change_event__)
        GUIBackend.date_input_connector(self.end_date_filter, self.__internal_date_change_event__)

        self.__groupbox_filter_event_connector__()
        GUIBackend.set_cell_width_content_adjust(self.standards_filter_table, None)
        GUIBackend.set_cell_width_content_adjust(self.ranges_filter_table, None)
        GUIBackend.checkbox_connector(self.select_all_checkbox, self.select_all_samples)
        GUIBackend.combobox_changeg_connector(self.ranges_filter_standards_combobox, self.__ranges_filter_standard_changed__)
        GUIBackend.button_connector(self.rebuild_btn, self.autoRebuildDialog.show)

        GUIBackend.set_wgt_visible(self.ranges_filter_warning_lbl, False)
        GUIBackend.set_wgt_visible(self.standards_filter_warning_lbl, False)

        for filter_name in self.filters_frame.keys():
            self.show_filter(filter_name, False)

        self.popupFrame = GUIComponents.overlayMassage(text='Loading...')
    
    def startup(self,):
        GUIBackend.set_checkbox_value(self.select_all_checkbox, False)


    
    def __internal_date_change_event__(self,):
        """set input date ranges to prevent start_date be bigger than end date
        and end_date be lower than start_date.
        this function call when coresponds input change
        """
        from_date,to_date = self.get_date_filter()
        GUIBackend.set_date_input_range(self.start_date_filter, max_date=to_date)
        GUIBackend.set_date_input_range(self.end_date_filter, min_date=from_date)


    def select_all_samples(self,st):
        """select and unselect all samples , corspond to status
        of 'select all' checkbox

        Args:
            st (_type_): _description_
        """
        #get status of all checkbox
        status = GUIBackend.get_checkbox_value(self.select_all_checkbox)
        #set status to all checkboxes of samples
        for sample_checkbox in self.samples_table_checkbox.values():
            GUIBackend.set_checkbox_value(sample_checkbox, status)

    def set_select_all_samples(self, flag):
        GUIBackend.set_checkbox_value(self.select_all_checkbox, flag )
        

    def apply_filter_button_connector(self,func):
        """connect 'apply filter' button into a python func

        Args:
            func (callable): a python function
        """
        GUIBackend.button_connector(self.apply_filter_btn, func)

    def external_see_report_button_connector(self, func):
        self.external_see_report_event_func = func

    def compare_button_connector(self, func):
        GUIBackend.button_connector(self.compare_btn, func)

    def delete_selections_button_connector(self, func):
        GUIBackend.button_connector(self.delete_selections_btn, func)


    def __groupbox_filter_event_connector__(self, ):
        """connect event of groupbox chechbox into an internal functions
        """
        for name in self.filters_groupbox.keys():
            GUIBackend.groupbox_checkbox_connector(
                self.filters_groupbox[name],
                self.__filter_activation_event__(name) )

    def __filter_activation_event__(self,name: str):
        """unvisible a filter when it be unchecked.

        Args:
            name (str): name of filter
        """

        def func():
            if GUIBackend.is_groupbox_checked(self.filters_groupbox[name]):
                self.show_filter(name, True)
                
            
            else:
                self.show_filter(name, False)

        return func
    


    def set_rebuild_status(self, need_rebuild:bool):
        """if status be True, it means that rebuild is need and in UI,
            rebuild button whould be action, and some filters de active.

        Args:
            need_rebuild (bool): _description_
        """
        
        GUIBackend.set_wgt_visible(self.ranges_filter_warning_lbl, need_rebuild)
        GUIBackend.set_wgt_visible(self.standards_filter_warning_lbl, need_rebuild)
        
        GUIBackend.set_disable_enable(self.filters_groupbox['ranges'], not(need_rebuild))
        GUIBackend.set_disable_enable(self.filters_groupbox['standards'], not(need_rebuild))

        GUIBackend.set_disable_enable(self.rebuild_btn, need_rebuild)
                

    

    def __ranges_filter_standard_changed__(self,):
        current_standard_name = GUIBackend.get_combobox_selected(self.ranges_filter_standards_combobox)
        current_standard = None
        for standard in self.standards:
            if standard['name'] == current_standard_name:
                current_standard = standard
                break
        if current_standard is not None:
            self.render_ranges_filter_table(current_standard)
    

    def render_ranges_filter_table(self, standard):
        """show ranges in filter ranges box, corespond to selected standard
        """
        GUIBackend.set_table_dim(self.ranges_filter_table, row=len(standard.get('ranges',[])) , col=4)
        self.ranges_filter = []
        for i,(low,high) in enumerate(standard['ranges']):
            text = f'{low}mm - {high}mm'
            GUIBackend.set_table_cell_value(self.ranges_filter_table, (i,0), text )

            compare_comboxes = GUIComponents.compareComboBox()
            GUIBackend.set_table_cell_widget(self.ranges_filter_table, (i,1), compare_comboxes, layout=True)

            input = GUIComponents.doubleSpinBoxTable()
            #input.set_size(30, 20)

            GUIBackend.set_table_cell_widget(self.ranges_filter_table, (i,2), input, layout=True)

            GUIBackend.set_table_cell_value(self.ranges_filter_table, (i,3), '%' )

            self.ranges_filter.append(
                {   
                    'range': [low, high],
                    'operator': compare_comboxes,
                    'input': input,
                }
            )
        GUIBackend.set_cell_width_content_adjust(self.ranges_filter_table, None)


    

    def show_filter(self, name, flag):
        if flag:
            GUIBackend.set_frame_max_size( self.filters_frame[name], w=None, h=16000 )
        else:
            GUIBackend.set_frame_max_size( self.filters_frame[name], w=None, h=0 )

        

    def get_active_filters(self,):
        res = []
        for key in self.filters_groupbox.keys():
            if GUIBackend.is_groupbox_checked(self.filters_groupbox[key]):
                res.append(key)

        return res


    def get_date_filter(self,) -> tuple[ datetime, datetime ]:
        """returns value of iputs date

        Returns:
            tuple[ datetime, datetime ]: start date, end date
        """
        start = GUIBackend.get_date_input ( self.start_date_filter)
        end = GUIBackend.get_date_input( self.end_date_filter)
        return start, end

    def get_name_filter(self) -> str:
        """returns input filter name value 

        Returns:
            str: _description_
        """
        return GUIBackend.get_input_text(self.name_filter_input)
    

    def get_username_filter(self) -> str:
        """returns filter username value 

        Returns:
            str: _description_
        """
        return GUIBackend.get_input_text(self.username_filter_input)




    def get_standards_filter(self,) -> list[str]:
        res = []
        for standard_name, checkbox in self.standards_filter_checkbox.items():
            if GUIBackend.get_checkbox_value(checkbox):
                res.append(standard_name)

        return res
    

    def get_ranges_filter(self,) -> list[str]:
        res = []
        for i in range(len(self.ranges_filter)):
            operator_combobox = self.ranges_filter[i]['operator']
            value_input = self.ranges_filter[i]['input']

            operator = GUIBackend.get_combobox_selected(operator_combobox)
            value = GUIBackend.get_input(value_input)
            if value == '':
                value = None
            else:
                value = float(value)
            res.append({'operator':operator, 'input':value})
        
        selected_standard = GUIBackend.get_combobox_selected(self.ranges_filter_standards_combobox)
        return res, selected_standard
  

    def set_standards_filter_table_data(self, standards:list[str]):
        """insert standards range into table
        Args:
            datas (list[str]): list of standards name
        """
        
        #set row count
        self.standards_filter_checkbox = {}
        records_count = len(standards)
        GUIBackend.set_table_dim(self.standards_filter_table, row=records_count, col=None)
        
        for i, standard_name in enumerate(standards):
            GUIBackend.set_table_cell_value(self.standards_filter_table, (i,1), standard_name)

            #define checkbox for each row
            cell_checkbox = GUIComponents.tabelCheckbox()
            cell_checkbox.set_size(15,15)

            #insert checkbox into table
            GUIBackend.set_table_cell_widget(self.standards_filter_table, (i,0), cell_checkbox)

            
            self.standards_filter_checkbox[standard_name] = cell_checkbox

    def set_compare_standards_items(self, standards_name:list[str]):
        """set a list of standards name into compare_standard_combobox

        Args:
            standards_name (list[str]): list of standards names

        """
        GUIBackend.set_combobox_items(self.compare_standards_combobox, standards_name)


    def set_ranges_filter_standards(self, standards_name:list[str], standards:list[dict]):
        """insert standards range into table
        Args:
            standards_name (list[str]): list of standards name
            standards (list[dict]): list of standards dictionary (database query of standards)
        """
        self.standards = standards
        GUIBackend.set_signal_connection(self.ranges_filter_standards_combobox, False)
        GUIBackend.set_combobox_items(self.ranges_filter_standards_combobox, standards_name)
        GUIBackend.set_signal_connection(self.ranges_filter_standards_combobox, True)
        self.__ranges_filter_standard_changed__()

    
    def set_delete_sample_event_func(self, func):
        """set a python function as event of delete button samples in table

        Args:
            func (_type_): python function
        """
        self.external_delete_samples_event_func = func

    

    def set_samples_table(self, samples: list[dict]):
        
        samples = samples.copy()
        GUIBackend.set_table_dim(self.samples_table, row=len(samples), col=None)
        self.samples_table_checkbox = {}
        for i,sample in enumerate(samples):
            for feature_name, feature_value in sample.items():
                if feature_name == 'date':
                    feature_value = datetimeFormat.date_to_str(feature_value)
                if feature_name in self.samples_table_headers:
                    j = self.samples_table_headers.index(feature_name)
                    GUIBackend.set_table_cell_value(self.samples_table, (i,j), feature_value)


            checkbox = GUIComponents.tabelCheckbox()
            j = self.samples_table_headers.index('-')
            GUIBackend.set_table_cell_widget(self.samples_table, (i,j), checkbox, True) 
            self.samples_table_checkbox[sample['name_id']] = checkbox


            report_btn = GUIComponents.reportButton()
            j = self.samples_table_headers.index('see')
            GUIBackend.button_connector_argument_pass( report_btn,
                                                       self.external_see_report_event_func,
                                                       args=(sample,)
                                                       )
            GUIBackend.set_table_cell_widget(self.samples_table, (i,j), report_btn, layout=True)

            #define delte button
            delete_btn = GUIComponents.deleteButton()
            j = self.samples_table_headers.index('delete')
            GUIBackend.set_table_cell_widget(self.samples_table, (i,j), delete_btn)
            GUIBackend.button_connector_argument_pass(delete_btn, 
                                        self.external_delete_samples_event_func, 
                                        args=(sample,)
                                        )
            
            
                
    def get_selected_samples(self,) -> list[str]:
        """returns id of those samples that are checked for compare

        Returns:
            list[str]: list of samples id
        """
        res = []
        for sample_id, checkbox in self.samples_table_checkbox.items():
            if GUIBackend.get_checkbox_value(checkbox):
                res.append(sample_id)
        return res
    
    def get_selected_standard_for_campare(self,):
        return GUIBackend.get_combobox_selected(self.compare_standards_combobox)
    

    

