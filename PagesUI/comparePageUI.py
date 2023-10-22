
from uiUtils.guiBackend import GUIBackend
from PagesUI.PageUI import commonUI
from uiUtils import GUIComponents
from uiUtils.Charts.lineChart import LineChart, Trend
import random
import numpy as np

class comparePageUI(commonUI):
    
    def __init__(self, ui,):
        
        self.ui = ui
        self.back_btn = self.ui.comparepage_back_btn
        self.compare_table = self.ui.comparepage_compare_table
        self.total_mean_table = self.ui.comparepage_compare_mean_table
        self.progressbar = self.ui.comparepage_progressbar
        self.charts_layout = self.ui.charts_layout
        
        
        

        self.compare_table_headrs = ['name', 'date', 'time']
        GUIBackend.set_table_dim(self.total_mean_table,row=1, col=None)
        self.init_trend_chart()
        GUIBackend.add_widget(self.charts_layout, self.trends_chart)
        


    def init_trend_chart(self,):
        self.trends_chart  = LineChart(
                    chart_title = 'Trends',
                    chart_title_color = '#404040',
                    axisX_label = 'Samples',
                    axisY_label = 'Percent',
                    chart_background_color = '#f0f0f0',
                    chart_legend=True,
                    axis_color = '#404040',
                    axisX_grid=True,
                    axisY_grid=True,
                    axisY_grid_color='#40404040',
                    axisY_range = (0, 100),
                    axisX_tickCount = 10,
                    axisY_tickCount = 10,
                    animation = False,
                )


    def back_button_connector(self, func):
        GUIBackend.button_connector(self.back_btn, func)

    def set_compare_table_ranges_header(self, ranges):

        ranges_str = list(map( lambda x:f"{x[0]}mm - {x[1]}mm", ranges))
        self.ranges_str = ranges_str
        headers = self.compare_table_headrs + ranges_str
        GUIBackend.set_table_dim(self.compare_table,
                                 row=None,
                                 col=len(headers))
        
        GUIBackend.set_table_dim(self.total_mean_table,
                                 row=None,
                                 col=len(ranges_str))
        
        GUIBackend.set_table_cheaders( self.compare_table,
                                       headers
                                      )
        
        GUIBackend.set_table_cheaders( self.total_mean_table,
                                       ranges_str
                                      )


    def set_compare_table(self, data: list[list]):

        GUIBackend.set_table_dim(self.compare_table, row=len(data), col=None)
        start_ranges_idx = len(self.compare_table_headrs) 
        end_ranges_idx = len(self.compare_table_headrs + self.ranges_str)
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                if start_ranges_idx<=col_idx< end_ranges_idx:
                    value = str(value) + ' %'
                
                GUIBackend.set_table_cell_value(self.compare_table, (row_idx, col_idx), value)


    
    def set_total_mean_table(self, data: list[list]):

        for col_idx, value in enumerate(data):
                value = str(value) + ' %'
                GUIBackend.set_table_cell_value(self.total_mean_table, (0, col_idx), value)
            

    def set_progressbar(self, value:int):
        GUIBackend.set_progressbar_value(self.progressbar, value)

    
    def show_page_content(self, show:bool):
        if show:
            GUIBackend.set_max_size(self.ui.compareScrollAreaWidget, h=16777215)
            GUIBackend.set_max_size(self.progressbar, h=0)
        
        else:
            GUIBackend.set_max_size(self.ui.compareScrollAreaWidget, h=0)
            GUIBackend.set_max_size(self.progressbar, h=100)



    def show_trends_chart(self, datas:np.ndarray, ranges:list[list]):
        sample_count = len(datas)
        y_range_max = int(datas.max()) + 5

        
        self.trends_chart.set_axisY_range((0,y_range_max))
        #self.trends_chart.remove_all_trends()
        
        
        for i, _range in enumerate(ranges):
            range_str = f'{_range[0]}mm - {_range[1]}mm'
            
            color = random.randrange(0, 2**24)
            color = str(hex(color))
            color = '#' + color[2:]

            trend = Trend(name=range_str, line_color=color, line_width=2)
            trend.add_data(np.arange(sample_count), datas[:,i])
            self.trends_chart.add_trend(trend)

            