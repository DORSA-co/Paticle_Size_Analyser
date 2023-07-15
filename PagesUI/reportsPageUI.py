from guiBackend import GUIBackend
import GUIComponents
from datetime import datetime
class reportsPageUI:

    def __init__(self, ui):
        self.ui = ui

        self.filters_groupbox = {
            'name': self.ui.reportpage_filtername_groupbox,
            'date': self.ui.reportpage_filterdate_groupbox,
            'standards': self.ui.reportpage_filterstandards_groupbox,
        
        }

        self.filters_frame = {
            'name': self.ui.reportpage_filtername_frame,
            'date': self.ui.reportpage_filterdate_frame,
            'standards': self.ui.reportpage_filterstandards_frame,
        
        }

        self.start_date_filter = self.ui.reportpage_start_date_dateedit
        self.end_date_filter = self.ui.reportpage_end_date_dateedit
        self.standards_filter_tabel = self.ui.reportpage_standards_filter_tabel

        self.__groupbox_filter_event_connector__()
        GUIBackend.set_cell_width_content_adjust(self.standards_filter_tabel, None)

    
    def startup(self):
        pass


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
                GUIBackend.set_frame_max_size( self.filters_frame[name], w=None, h=16000 )
            
            else:
                GUIBackend.set_frame_max_size( self.filters_frame[name], w=None, h=0 )

        return func


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
            _type_: _description_
        """
        return GUIBackend.get_input_text(self.get_name_filter)


    def get_standards_filter(self,):
        pass


    def set_standards_filter_table_data(self, standards:list[list]):
        """insert standards range into table
        Args:
            datas (list[list]): list of standards name
        """
        
        #set row count
        records_count = len(standards)
        GUIBackend.set_table_dim(self.standards_filter_tabel, row=records_count, col=None)
        
        for i, standard_name in enumerate(standards):
            GUIBackend.set_table_cell_value(self.standards_filter_tabel, (i,1), standard_name)

            #define checkbox for each row
            cell_checkbox = GUIComponents.tabelCheckbox()
            cell_checkbox.set_size(15,15)

            #insert checkbox into table
            GUIBackend.set_table_cell_widget(self.standards_filter_tabel, (i,0), cell_checkbox)

