
from uiUtils.guiBackend import GUIBackend
from uiUtils import Charts
class reportPageUI:
    
    def __init__(self, ui,):
        self.ui = ui

        self.back_btn = self.ui.sreportpage_back_btn
        self.export_btn = self.ui.sreportpage_export_btn

        self.general_information = {
            'name':self.ui.sreportpage_name_lbl,
            'date':self.ui.sreportpage_date_lbl,
            'time':self.ui.sreportpage_time_lbl,
            'username':self.ui.sreportpage_user_lbl,
            'standard':self.ui.sreportpage_standard_lbl,
            'avrage':self.ui.sreportpage_avrage_lbl,
            'std':self.ui.sreportpage_std_lbl,
            'mode':self.ui.sreportpage_mode_lbl,
        }
        self.statictics_table = self.ui.sreportpage_statictics_table


        #--------------------------------------------------------------------------------------------------------
        self.grading_chart = Charts.BarChart(
                    chart_title = 'Grading',
                    chart_title_color = None,
                    axisX_label = 'Rages',
                    axisY_label = 'Percents',
                    chart_background_color = '#f0f0f0',
                    bar_color = '#4caf50',
                    axis_color = '#404040',
                    axisY_range = (0, 100),
                    axisY_tickCount = 10,
                    animation = False,
                    bar_width = 1,
                    axisY_grid = True,
                )

        #--------------------------------------------------------------------------------------------------------

        self.statictics_table_headers = ['range', 'avrage', 'std', 'count']

        GUIBackend.set_table_dim(self.statictics_table, row=None, col=len(self.statictics_table_headers))
        GUIBackend.set_table_cheaders(self.statictics_table, self.statictics_table_headers)
        GUIBackend.add_widget( self.ui.report_grading_chart_frame, self.grading_chart )
    

    def set_general_information(self, infoes:dict):
        for name, value in infoes.items():
            GUIBackend.set_label_text( self.general_information[name] , value )

    def back_button_connector(self, func):
        GUIBackend.button_connector(self.back_btn, func)


    def set_ranges_statistics_tabel(self, data: list[dict]):
        GUIBackend.set_table_dim(self.statictics_table, row=len(self.statictics_table_headers), col=None)
        for row_idx, row in enumerate(data):
            for name, value in row.items():
                col_idx = self.statictics_table_headers.index(name)
                GUIBackend.set_table_cell_value(self.statictics_table, index=(row_idx, col_idx), value=value)
            

            


    def set_grading_chart(self, values:list[float], ranges:list[list]):
        self.grading_chart.set_chart_y(values)
        ranges_str = list(map( lambda x: f"{x[0]}-{x[1]}", ranges))
        
        self.grading_chart.set_chart_x(ranges_str)
    
