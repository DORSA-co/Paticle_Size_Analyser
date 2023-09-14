
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from uiUtils.Charts.barChart import BarChart
from uiUtils.Charts.lineChart import LineChart, Trend
import cv2
import math

class reportPageUI:
    

    def __init__(self, ui,):
        self.ui = ui

        self.back_btn = self.ui.sreportpage_back_btn
        self.export_btn = self.ui.sreportpage_export_btn
        self.particles_table = self.ui.sreportpage_particels_table


        self.particle_navigator_buttons = {
            'next': self.ui.sreportpage_next_particle_btn,
            'prev': self.ui.sreportpage_prev_particle_btn
        }

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

        self.particle_information = {
            'max_radius': self.ui.sreportpage_particle_max_r_lbl,
            'avrage_radius': self.ui.sreportpage_particle_avg_r_lbl,
            'area': self.ui.sreportpage_particle_area_lbl,
            'volume': self.ui.sreportpage_particle_volume_lbl,
            'max_radius': self.ui.sreportpage_particle_max_r_lbl,
        }

        self.particle_image_lbl = self.ui.sreportpage_particle_image_lbl
        self.statictics_table = self.ui.sreportpage_statictics_table


        #--------------------------------------------------------------------------------------------------------
        self.grading_chart = BarChart(
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
        

        self.cumulative_chart  = LineChart(
                    chart_title = 'Cumulative',
                    chart_title_color = '#404040',
                    axisX_label = 'Rages',
                    axisY_label = 'Percent',
                    chart_background_color = '#f0f0f0',
                    chart_legend=False,
                    axis_color = '#404040',
                    axisX_grid=True,
                    axisY_grid=True,
                    axisY_grid_color='#40404040',
                    axisY_range = (0, 100),
                    axisX_tickCount = 10,
                    axisY_tickCount = 10,
                    animation = False,
                )
        self.cumulative_trend = Trend(name='', line_color='#20647d', line_width=2)
        self.cumulative_chart.add_trend(self.cumulative_trend)

        self.gaussian_chart  = LineChart(
                    chart_title = 'Guassian',
                    chart_title_color = '#404040',
                    axisX_label = 'Rages',
                    axisY_label = 'Percent',
                    chart_background_color = '#f0f0f0',
                    chart_legend=False,
                    axis_color = '#404040',
                    axisX_grid=True,
                    axisY_grid=True,
                    axisY_grid_color='#40404040',
                    axisY_range = (0, 100),
                    axisX_tickCount = 10,
                    axisY_tickCount = 10,
                    animation = False,
                )
        self.gaussian_trend = Trend(name='', line_color='#d4594e', line_width=4)
        self.gaussian_chart.add_trend(self.gaussian_trend)

        #--------------------------------------------------------------------------------------------------------

        self.statictics_table_headers  = ['range', 'avrage', 'std', 'count', 'percent']
        self.statictics_table_headers_unit = ['', ' (mm)', ' (mm)', '', ' (%)'] 


        headrs = list( map( lambda x: x[0]+x[1] , zip(self.statictics_table_headers, self.statictics_table_headers_unit)))
        GUIBackend.set_table_dim(self.statictics_table, row=None, col=len(self.statictics_table_headers))
        GUIBackend.set_table_cheaders(self.statictics_table, headrs)
        GUIBackend.add_widget( self.ui.report_grading_chart_frame, self.grading_chart )
        GUIBackend.add_widget( self.ui.report_cum_chart_frame, self.cumulative_chart )
        GUIBackend.add_widget( self.ui.report_gaussian_chart_frame, self.gaussian_chart )

    def create_connect(func, *args):
        return lambda: func(*args)

    
    def navigator_button_connector(self, func):
        def make_func_arg(key):
                def _func_():
                    func(key)
                return _func_
        
        for key, btn in self.particle_navigator_buttons.items():
            GUIBackend.button_connector( btn,
                                        make_func_arg(key) 
            )
            
    
    
    

    def set_general_information(self, infoes:dict):
        for name, value in infoes.items():
            GUIBackend.set_label_text( self.general_information[name] , value )

    def set_particle_information(self, infoes:dict):
        for name, value in infoes.items():
            GUIBackend.set_label_text( self.particle_information[name] , str(value) )

    def back_button_connector(self, func):
        GUIBackend.button_connector(self.back_btn, func)


    def set_ranges_statistics_tabel(self, data: list[dict]):
        GUIBackend.set_table_dim(self.statictics_table, row=len(data), col=len(self.statictics_table_headers))
        for row_idx, row in enumerate(data):
            for name, value in row.items():
                col_idx = self.statictics_table_headers.index(name)
                GUIBackend.set_table_cell_value(self.statictics_table, index=(row_idx, col_idx), value=value)
            
                if name == 'range':
                    GUIBackend.set_table_cell_color(self.statictics_table, 
                                                    index=(row_idx, col_idx),
                                                     bg_color=(6, 76, 130), 
                                                     color=(255,255,255))
            


    def set_grading_chart(self, values:list[float], ranges:list[list]):
        self.grading_chart.set_chart_y(values)
        self.grading_chart.set_chart_x(ranges)


    # def set_cumulative_chart_range(self,min_value, max_value):
    #     self.cumulative_chart.set_axisX_range((min_value, max_value))

    def set_cumulative_chart_value(self, xs, ys):
        self.clear_cumulative_chart()
        self.cumulative_chart.set_axisX_range((min(xs), max(xs)))
        self.cumulative_trend.add_data(xs, ys)
        
    def clear_cumulative_chart(self,):
        self.cumulative_trend.clear()

    
    def set_gaussian_chart_value(self, xs, ys):
        self.clear_gaussian_chart()

        self.gaussian_chart.set_axisX_range((min(xs), max(xs)))
        self.gaussian_chart.set_axisY_range((min(ys), max(ys)))
        self.gaussian_trend.add_data(xs, ys)
        
    def clear_gaussian_chart(self,):
        self.gaussian_trend.clear()
    
    


    def set_particle_image(self, img):
        #img = cv2.resize(img, None, fx=1, fy =1)
        GUIBackend.set_label_image(self.particle_image_lbl, img)

    
    def set_particles_image(self, imgs, ncol=5):
        count = len(imgs)
        nrow = int(math.ceil(count / ncol))
        GUIBackend.set_table_dim(self.particles_table, row=nrow, col=ncol)
        
        i = 0
        j = 0
        for img in imgs:
            lbl = GUIComponents.LabelTable()
            lbl.set_size(100,100)
            print(img.shape)
            #GUIBackend.set_label_scale(lbl, False)
            GUIBackend.set_label_image(lbl, img)
            GUIBackend.set_table_cell_widget(self.particles_table,
                                             index=(i,j),
                                             widget=lbl,
                                             layout=True)
            i+=1
            if i>=5:
                j+=1
                i=0

