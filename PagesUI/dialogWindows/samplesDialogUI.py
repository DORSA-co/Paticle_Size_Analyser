
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat


class samplesDialogUI:
    ui_path = 'uiFiles\\samples.ui'

    def __init__(self, button_name='load') -> None:

        self.ui = GUIBackend.load_ui(self.ui_path)

        self.samples_table = self.ui.samples_table
        

        self.button_name = button_name
        external_sample_button_event_func = None

        self.samples_table_headers = ['id', 'name', 'standard', 'date', 'time', 'username', self.button_name]
        


        GUIBackend.set_table_dim(self.samples_table, row=None, col=len(self.samples_table_headers))
        GUIBackend.set_table_cheaders(self.samples_table, self.samples_table_headers)
        GUIBackend.set_cell_width_content_adjust(self.samples_table, None)
    


    def show_samples(self, samples: list[dict]):
        GUIBackend.set_table_dim(self.samples_table, row=len(samples), col=None)
        #.samples_table_buttons = {}

        #move on table rows
        for row_idx, sample in enumerate(samples):

            #move on table cols
            for feature_name, feature_value in sample.items():
                if feature_name == 'date':
                    feature_value = datetimeFormat.date_to_str(feature_value)

                if feature_name in self.samples_table_headers:
                    #find index of column by search col name in headers
                    col_idx = self.samples_table_headers.index(feature_name)
                    GUIBackend.set_table_cell_value(self.samples_table, (row_idx, col_idx), feature_value)



            sample_btn = GUIComponents.tableButton(text=self.button_name)
            col_idx = self.samples_table_headers.index(self.button_name)
            GUIBackend.button_connector_argument_pass( sample_btn, self.external_sample_button_event_func, args=(sample,))
            GUIBackend.set_table_cell_widget(self.samples_table, (row_idx, col_idx), sample_btn, layout=True)

    

    def sample_button_connector(self, func):
        self.external_sample_button_event_func = func        


    def show(self,):
        GUIBackend.show_window(self.ui, True)
    
    def close(self):
        GUIBackend.close_window(self.ui)