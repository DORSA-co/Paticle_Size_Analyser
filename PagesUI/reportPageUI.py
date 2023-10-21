import cv2
import math

from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from uiUtils.Charts.barChart import BarChart
from uiUtils.Charts.lineChart import LineChart, Trend
from PagesUI.dialogWindows.exportResultDialogUI import exportResultDialogUI
from PagesUI.PageUI import commonUI


class reportPageUI(commonUI):
    

    def __init__(self, ui,single_rebuild_manual_ui):
        super().__init__()
        self.ui = ui
        self.rebuild_win_ui = single_rebuild_manual_ui
        self.exportDialog = exportResultDialogUI()

        self.back_btn = self.ui.sreportpage_back_btn
        self.export_btn = self.ui.sreportpage_export_btn
        self.rebuild_btn = self.ui.sreportpage_rebuild_btn

        self.particles_table = self.ui.sreportpage_particels_table
        self.particle_image_event_func = None
        self.current_page = self.ui.sreportpage_current_page
        self.end_page = self.ui.sreportpage_end_page

        

        #self.description_lbl = self.ui.sreportpage_description_lbl


        self.particle_navigator_buttons = {
            'prev': self.ui.sreportpage_prev_particle_btn,
            'next': self.ui.sreportpage_next_particle_btn,
            
        }

        self.descriptions = {
            'statictics' : [
                                self.ui.sreportpage_statictics_desc1,
                                self.ui.sreportpage_statictics_desc2,
                            ]
        }

        self.general_information = {
            'name':self.ui.sreportpage_name_lbl,
            'date':self.ui.sreportpage_date_lbl,
            'time':self.ui.sreportpage_time_lbl,
            'username':self.ui.sreportpage_user_lbl,
            'standard':self.ui.sreportpage_standard_lbl,
            'description': self.ui.sreportpage_description_lbl,
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

        self.statictics_table_headers  = ['range', 'avrage', 'std', 'count', 'percent', 'circularity']
        self.statictics_table_headers_unit = ['', ' (mm)', ' (mm)', '', ' (%)', ' %'] 


        headrs = list( map( lambda x: x[0]+x[1] , zip(self.statictics_table_headers, self.statictics_table_headers_unit)))
        GUIBackend.set_table_dim(self.statictics_table, row=None, col=len(self.statictics_table_headers))
        GUIBackend.set_table_cheaders(self.statictics_table, headrs)
        GUIBackend.add_widget( self.ui.report_grading_chart_frame, self.grading_chart )
        GUIBackend.add_widget( self.ui.report_cum_chart_frame, self.cumulative_chart )
        GUIBackend.add_widget( self.ui.report_gaussian_chart_frame, self.gaussian_chart )
        GUIBackend.button_connector(self.rebuild_win_ui.close_btn, self.close_rebuild_win)
        GUIBackend.set_win_frameless(self.rebuild_win_ui)

    def create_connect(func, *args):
        return lambda: func(*args)

    
    def navigator_button_connector(self, func):
  
        for key, btn in self.particle_navigator_buttons.items():
            GUIBackend.button_connector_argument_pass( btn,
                                                      func,
                                                      args=(key,)
                                                )
            
    
    def export_button_connector(self, func):
        GUIBackend.button_connector(self.export_btn, func)
    
    

    def set_general_information(self, infoes:dict):
        for name, value in infoes.items():
            if name in self.general_information:
                GUIBackend.set_label_text( self.general_information[name] , value )


    def set_particle_information(self, infoes:dict):
        for name, value in infoes.items():
            if name in self.particle_information:
                GUIBackend.set_label_text( self.particle_information[name] , str(value) )

    def back_button_connector(self, func):
        GUIBackend.button_connector(self.back_btn, func)

    def rebuild_button_connector(self, func):
        """connects a function to rebuild button in top of report page
        """
        GUIBackend.button_connector(self.rebuild_btn, func)
    
    def dialog_rebuild_button_connector(self, func):
        """connects a function to rebuild button that is in the 
          rebuild dialog
        """
        GUIBackend.button_connector(self.rebuild_win_ui.rebuild_btn, func)


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

    
    def set_particles_image(self, imgs, ncol, nrow):
        imgs_count = len(imgs)
        GUIBackend.set_table_dim(self.particles_table, row=nrow, col=ncol)
        
        for idx in range(ncol*nrow):
            lbl = GUIComponents.LabelTable()
            lbl.set_size(90,90)
            if idx<imgs_count:
                #GUIBackend.set_label_scale(lbl, False)
                GUIBackend.set_label_image(lbl, imgs[idx])
                
                #lbl.mousePressEvent = lambda x:print('s',x)
                lbl.clicked.connect( self.__particle_image_connector_maker__(idx))

            row = int(idx // ncol)
            col = int(idx % ncol)
            GUIBackend.set_table_cell_widget(self.particles_table,
                                                index=(row,col),
                                                widget=lbl,
                                                layout=True)

    
    def __particle_image_connector_maker__(self, img_num):
        def func():
            self.particle_image_event_func(img_num)
        return func
        
    
    def particle_click_connector(self, func):
        self.particle_image_event_func = func

    def handle_navigation_button_enabality(self, current_page, min_page, max_page):
        """handle navigation buttons be enable or disable.
           if current page be minimum, prev button disable
           and if be maximum, next button disable
        """

        if current_page == max_page:
            GUIBackend.set_disable_enable(self.particle_navigator_buttons['next'], False)
        else:
            GUIBackend.set_disable_enable(self.particle_navigator_buttons['next'], True)


        if current_page == min_page:
            GUIBackend.set_disable_enable(self.particle_navigator_buttons['prev'], False)
        else:
            GUIBackend.set_disable_enable(self.particle_navigator_buttons['prev'], True)
        
        
    # def set_description(self, name, idx, text):
    #     GUIBackend.set_label_text( self.descriptions[name][idx], text)

    def show_page_number(self, curent:int, end:int):
        GUIBackend.set_label_text(self.current_page, str(curent))
        GUIBackend.set_label_text(self.end_page, str(end))

    
    def show_rebuild_win(self,):
        GUIBackend.show_window(self.rebuild_win_ui, True)

    def close_rebuild_win(self):
        GUIBackend.close_window(self.rebuild_win_ui)

    def set_rebuild_standards(self, standards:list[str]):
        GUIBackend.set_combobox_items(self.rebuild_win_ui.standards_combobox, standards)
    
    def set_rebuild_current_standard(self, stanndard_name:str):
        GUIBackend.set_combobox_current_item(self.rebuild_win_ui.standards_combobox, stanndard_name)

    def get_rebuild_standard(self,) -> str:
        return GUIBackend.get_combobox_selected(self.rebuild_win_ui.standards_combobox)
    
    def open_export_file_dialog(self,):
        return GUIComponents.selectSaveFile(file_name='Excel',file_extention='.xlsx')