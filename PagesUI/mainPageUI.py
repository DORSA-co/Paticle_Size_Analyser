from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
import Charts




class mainPageUI:
    
    def __init__(self, ui, sample_info):
        self.ui = ui
        self.sample_info = sample_info

        self.current_status = 'stop'
        self.warning_msg_lbl = self.ui.mainpage_warning_massage_lbl
        self.close_warning_msg_btn = self.ui.mainpage_close_error_btn
        self.warning_msg_frame = self.ui.mainpage_error_msg_frame
        self.live_img_lbl = self.ui.mainpage_live_image_lbl
        self.report_btn = self.ui.mainpage_report_button
        

        self.external_warning_button_event_func = None

        self.error_slide_animation = GUIComponents.singleAnimation(self.warning_msg_frame, b'maximumHeight', 400, 0, 120)
        
        self.warning_btns = {
            'camera_connection': {
                'btn':self.ui.mainpage_camera_connection_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-connection-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-connection-red-50.png'
                },
            'camera_grabbing': {
                'btn': self.ui.mainpage_camera_grabbing_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-camera-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-camera-red-50.png'
                },

            'illumination': {
                'btn': self.ui.mainpage_illumination_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-headlight-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-headlight-red-50.png'
            },
                             
            'tempreture': {
                'btn': self.ui.mainpage_tempreture_warning_btn,
                'ok-icon':':/assets/Assets/icons/icons8-thermometer-green-50.png',
                'warning-icon':':/assets/Assets/icons/icons8-thermometer-red-50.png'
            }
        }
        
        self.informations = {
            'ovality': self.ui.mainpage_mean_oval_lbl,
            'avrage' : self.ui.mainpage_avrage_lbl,
            'std'    : self.ui.mainpage_std_lbl,
            'fps'    : self.ui.mainpage_fps_lbl

        }

        self.player_btns = {
            'start': self.ui.mainpage_start_btn,
            'stop' : self.ui.mainpage_stop_btn,
            'fast_start': self.ui.mainpage_faststart_btn
        }


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
        
        self.seccond_chart = Charts.BarChart(
                    chart_title = 'Grading',
                    chart_title_color = None,
                    axisX_label = 'Rages',
                    axisY_label = 'Percents',
                    chart_background_color = '#f0f0f0',
                    bar_color = '#4caf50',
                    axis_color = '#404040',
                    #axis_grid = False,
                    axisY_range = (0, 100),
                    axisY_tickCount = 10,
                    animation = True,
                    bar_width = 1,
                )
        
        
        

        
        
        GUIBackend.add_widget( self.ui.mainpage_grading_chart_frame, self.grading_chart )
        GUIBackend.add_widget( self.ui.mainpage_second_chart_frame, self.seccond_chart )
        GUIBackend.button_connector(self.sample_info.cancel_btn, self.cancel_start )
        for name in self.warning_btns.keys():
            GUIBackend.button_connector(self.warning_btns[name]['btn'], self.internal_warning_button_event(name))
        GUIBackend.button_connector(self.close_warning_msg_btn, self.close_warning_msg)
        #Startup operations-----------------
        #-----------------------------------------------------------
        self.startup()
    
    def startup(self):
        self.write_error_msg(None)
        self.close_warning_msg()
        self.write_sample_info_error_msg(None)
        self.enable_reports(False)
        
    def warning_buttons_connector(self, func):
        self.external_warning_button_event_func = func


    def internal_warning_button_event(self, name:str):
        """this function execute when each of error button clicked

        Args:
            name (str): name of button that pressed. it coulbe be one key if self.warning_btns dictionary
        """
        def func():
            self.open_warning_msg()
            if self.external_warning_button_event_func is not None:
                self.external_warning_button_event_func(name)
        
        return func
    
    def open_warning_msg(self,):
        self.error_slide_animation.toggle()

    def close_warning_msg(self,):
        self.error_slide_animation.backward()


    def cancel_start(self):
        GUIBackend.close_window(self.sample_info)

    
    def set_player_buttons_status(self,state:str):
        """manage enable and disable, player buttons in diffent state.

        Args:
            state (str): state of playing. it could be one of 'start' and 'stop'
        """
        if state == 'start':
            GUIBackend.button_disable(self.player_btns['start'])
            GUIBackend.button_disable(self.player_btns['fast_start'])
            GUIBackend.button_enable(self.player_btns['stop'])
            
        
        elif state == 'stop':
            GUIBackend.button_enable(self.player_btns['start'])
            GUIBackend.button_enable(self.player_btns['fast_start'])
            GUIBackend.button_disable(self.player_btns['stop'])
            
            

        else:
            assert True, "invalid input, input can be only 'start' or 'stop' "

    

    def player_buttons_connect(self,name:str,  func):
        """connect click event of start or fast_start or stop button into a function

        Args:
            name (str): name of button. it could be one of the 'start', 'fast_start' and 'stop' 
            func (_type_): event function for click
        """
        GUIBackend.button_connector( self.player_btns[ name ], func)

    
    def run_button_connect(self, func):
        GUIBackend.button_connector(self.sample_info.run_btn, func)



    def set_warning_buttons_status(self, name: str, status: bool):
        """change situation of warning buttons and set them in ok (green) or warning (red) state

        Args:
            name (str): name of warning that could be one of ['camera_connection', 'camera_grabbing', 'illumination', 'tempreture']
            status (bool): 'True' for ok and 'False' for warning
        """
        assert name in self.warning_btns.keys(), f" {name} warning doesn't exist. it could be only ['camera_connection', 'camera_grabbing', 'illumination', 'tempreture']"
        if status:
            GUIBackend.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['ok-icon'])
        else:
            GUIBackend.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['warning-icon'])
            
    
    def report_button_connector(self, func):
        """connect a function to clicked event of report button

        Args:
            func (_type_): function
        """
        GUIBackend.button_connector(self.report_btn, func)

    # def toolbox_connector(self, func):
    #     """connect a function to change event of toolbox checkboxes of main page

    #     Args:
    #         func (_type_): this function should be have one argumant. the value of this argument would be 'live-view' or 'drawing'.
    #     """
    #     GUIBackend.checkbox_connector(self.ui.mainpage_liveview_checkbox, func('live-view'))
    #     GUIBackend.checkbox_connector(self.ui.mainpage_drawing_checkbox, func('drawing'))


    def get_toolboxes(self, ):
        data = {}
        data['live'] = GUIBackend.get_checkbox_value(self.ui.mainpage_liveview_checkbox)
        data['drawing'] = GUIBackend.get_checkbox_value(self.ui.mainpage_drawing_checkbox)
        return data
    

    def set_information(self, data:dict):
        """set data into information box of main page

        Args:
            data (dict): data is a dictionary that it keys are name of info and values are value of that infos.
            allowable are 'ovality', 'avrage', 'std', 'fps'
        """
        for name, value in data.items():
            if name in ['avrage', 'std']:
                value = "{0:.2f} mm".format(value)
            GUIBackend.set_label_text(  self.informations[name],
                                        str(value) 
                                    )
            
        #self.set_statistics_table_datas()
    
    def set_statistics_table_datas(self, datas: list[list]):
        """set data into statistics table of mainpage. 

        Args:
            datas (list[list]): list of row list. first item in each row sould be name of row. 
            - for e.g [ ['avrage', 12, 13.5, ...], ['std', 0.5, 0.76, ...]]
        """
        cols_count = len(datas[0])
        #set cols count
        GUIBackend.set_table_dim(self.statistics_table, None, col=cols_count)
        #insert datas into table
        GUIBackend.set_table_datas(self.statistics_table, datas)

        #set first column ( row headers) color diffrence
        for row in range(len(datas)):
            GUIBackend.set_table_cell_color(self.statistics_table, (row,0), bg_color=(6, 76, 130), color=(255,255,255))

    def set_statistics_table_headers(self, headers:list[str]):
        """set heaaders of statistics table in mainpage. these are ranges of particles

        Args:
            headers (list[str]): list of headers like: [ '<6mm', '6mm-8mm' ,...]
        """
        #first columns should be empty for rows header
        headers = [''] + headers
        GUIBackend.set_table_cheaders(self.statistics_table, headers)

    def set_warning_massage(self, text):
        text = "Warning: " + text
        self.warning_msg_lbl.setText(text)
        GUIBackend.set_wgt_visible(self.warning_msg_lbl, True)


    
    def set_live_img(self, img):
        GUIBackend.set_label_image(self.live_img_lbl, img)


    
    def set_sample_info_standards_items(self, items: list[str]) -> None: 
        GUIBackend.set_combobox_items(self.sample_info.standards_name_combobox, items)
    
    def get_sample_info(self, ) -> dict:
        info = {}
        info['name'] = GUIBackend.get_input_text(self.sample_info.sample_name_input)
        info['standard'] = GUIBackend.get_combobox_selected(self.sample_info.standards_name_combobox)

        return info
    

    def show_dialog_box(self, title, txt , buttons):
        box = GUIComponents.confirmMessageBox(title, txt, buttons)
        flag = box.render()
        return flag
    


    def write_error_msg(self, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.mainpage_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.mainpage_error_lbl, True)
            GUIBackend.set_label_text(self.ui.mainpage_error_lbl, txt)
            GUIComponents.single_timer_runner(10000, lambda : self.write_error_msg(None))
        
    
    def write_sample_info_error_msg(self, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.sample_info.error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.sample_info.error_lbl, True)
            GUIBackend.set_label_text(self.sample_info.error_lbl, txt)
            


    def show_sample_info_window(self,):
        """show sample info dialog window
        """
        GUIBackend.show_window(self.sample_info)

    def close_sample_info_window(self,):
        """close sample info
        """
        GUIBackend.close_window(self.sample_info)


    def enable_reports(self,flag):
        GUIBackend.set_disable_enable(self.report_btn, flag)
    
    


    def set_grading_chart_ranges(self, ranges:list[list]):
        ranges_str = list(map( lambda x: f"{x[0]}-{x[1]}", ranges))
        self.grading_chart.set_chart_x(ranges_str)
    
    def set_grading_chart_values(self, values:list[float]):
        self.grading_chart.set_chart_y(values)