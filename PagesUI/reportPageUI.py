
from uiUtils.guiBackend import GUIBackend
from uiUtils import Charts
import cv2


class reportPageUI:
    
    def __init__(self, ui,):
        self.ui = ui

        self.back_btn = self.ui.sreportpage_back_btn
        self.export_btn = self.ui.sreportpage_export_btn

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

        self.statictics_table_headers  = ['range', 'avrage', 'std', 'count', 'percent']
        self.statictics_table_headers_unit = ['', ' (mm)', ' (mm)', '', ' (%)'] 


        headrs = list( map( lambda x: x[0]+x[1] , zip(self.statictics_table_headers, self.statictics_table_headers_unit)))
        GUIBackend.set_table_dim(self.statictics_table, row=None, col=len(self.statictics_table_headers))
        GUIBackend.set_table_cheaders(self.statictics_table, headrs)
        GUIBackend.add_widget( self.ui.report_grading_chart_frame, self.grading_chart )

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
    
    def set_particle_image(self, img):
        #img = cv2.resize(img, None, fx=1, fy =1)
        GUIBackend.set_label_image(self.particle_image_lbl, img)