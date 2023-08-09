from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from datetime import datetime
class reportsPageUI:

    def __init__(self, ui):
        self.ui = ui

        self.start_date_filter = self.ui.reportpage_start_date_dateedit
        self.end_date_filter = self.ui.reportpage_end_date_dateedit
        self.standards_filter_table = self.ui.reportpage_standards_filter_table
        self.apply_filter_btn = self.ui.reportpage_apply_filters_btn
        self.samples_table = self.ui.reportpage_samples_table
        self.name_filter_input = self.ui.reportpage_filtername_input
        self.username_filter_input = self.ui.reportpage_filterusername_input

        self.filters_groupbox = {
            'name': self.ui.reportpage_filtername_groupbox,
            'username': self.ui.reportpage_filterusername_groupbox,
            'date': self.ui.reportpage_filterdate_groupbox,
            'standards': self.ui.reportpage_filterstandards_groupbox,
        
        }

        self.filters_frame = {
            'name': self.ui.reportpage_filtername_frame,
            'username': self.ui.reportpage_filterusername_frame,
            'date': self.ui.reportpage_filterdate_frame,
            'standards': self.ui.reportpage_filterstandards_frame,
        
        }
        

        self.standards_filter_checkbox = {}
        self.samples_table_headers= ['compare', 'id', 'name', 'standard', 'date','time', 'username', 'see' ]
        self.external_see_report_event_func = None


        GUIBackend.set_table_dim(self.samples_table, row=None, col = len(self.samples_table_headers))
        GUIBackend.set_table_cheaders(self.samples_table, self.samples_table_headers)
        GUIBackend.set_cell_width_content_adjust(self.samples_table)
        
        GUIBackend.set_date_input(self.end_date_filter, datetime.now())
        GUIBackend.set_date_input(self.start_date_filter, datetime.now())

        self.__groupbox_filter_event_connector__()
        GUIBackend.set_cell_width_content_adjust(self.standards_filter_table, None)


        for filter_name in self.filters_frame.keys():
            self.show_filter(filter_name, False)


    
    def startup(self):
        pass

    def apply_filter_button_connector(self,func):
        GUIBackend.button_connector(self.apply_filter_btn, func)

    def external_see_report_button_connector(self, func):
        self.external_see_report_event_func = func


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
    

    def __internal_see_report_event__(self, sample):

        def func():
            self.external_see_report_event_func(sample)
        
        return func
    

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


    def set_standards_filter_table_data(self, standards:list[list]):
        """insert standards range into table
        Args:
            datas (list[list]): list of standards name
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



    def set_samples_table(self, samples: list[dict]):

        GUIBackend.set_table_dim(self.samples_table, row=len(samples), col=None)

        for i,sample in enumerate(samples):
            for feature_name, feature_value in sample.items():
                if feature_name == 'date':
                    feature_value = feature_value.strftime("%Y/%m/%d")
                if feature_name in self.samples_table_headers:
                    j = self.samples_table_headers.index(feature_name)
                    GUIBackend.set_table_cell_value(self.samples_table, (i,j), feature_value)


            checkbox = GUIComponents.tabelCheckbox()
            j = self.samples_table_headers.index('compare')
            GUIBackend.set_table_cell_widget(self.samples_table, (i,j), checkbox)



            report_btn = GUIComponents.reportButton()
            j = self.samples_table_headers.index('see')
            GUIBackend.button_connector( report_btn, self.__internal_see_report_event__(sample))
            GUIBackend.set_table_cell_widget(self.samples_table, (i,j), report_btn)
            
            
                
