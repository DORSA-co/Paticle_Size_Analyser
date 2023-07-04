import os
import typing
#os.system('cmd /c "pyrcc5 -o Assets.py Assets.qrc"') #PyQt
os.system('CMD /C pyside6-rcc Assets.qrc -o Assets.py')#PySide
#from PyQt5 import uic
from PySide6 import QtWidgets, QtCore, QtGui 
from PySide6.QtUiTools import QUiLoader
import sys
import webbrowser
from functools import partial
import texts
import Assets

#from PySide6.QtChart import QChart, QChartView, QBarSet,QPercentBarSeries
#from PyQt5.QtCore import QObject, pyqtSignal , pyqtSlot, QThread
import time
from Charts.BarChart import BarChart


main_ui_file = 'main_UI.ui'

class GlobalUI():
    """this class is used to build class for mainwindow to load GUI application

    :param QtWidgets: _description_
    """

    def __init__(self, ui):
        """this function is used to laod ui file and build GUI application
        """
        
        self.ui = ui




        
        # app language
        self.language = 'en'

        # load ui file
        #uic.loadUi(main_ui_file, self)



        self.ui.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        #
        self._old_pos = None
        self.app_close_flag = False

        # webbrowser
        chrome_path_win = "C://Program Files//Google//Chrome//Application//chrome.exe"
        chrome_path_linux = '/usr/bin/google-chrome %s'
        if sys.platform.startswith('win'):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_win))
        elif sys.platform.startswith('linux'):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_linux))

        # button connector
        self.header_button_connector()
        self.sidebar_button_connector()

        # startup settings
        self.startup_settings()

        self.pages_index = {
            'main'       : 0,
            'report'     : 1,
            'settings'   : 2,
            'calibration': 3,
            'user'       : 4,
            'help'       : 5
        }

        


    

        
    #-------------------------------------------------------------------------------------------


    def startup_settings(self):
        """this function is used to do startup settings on app start
        """
        return

    def header_button_connector(self):
        """this function is used to connect ui buttons to their functions
        """
        GUIManager.button_connector( self.ui.minimize_btn, self.minimize_win )
        GUIManager.button_connector( self.ui.maximize_btn, self.maxmize_minimize )
        GUIManager.button_connector( self.ui.close_btn, self.close_app )
        # bottom window buttens
        #self.dorsa_url_btn.clicked.connect(partial(lambda: webbrowser.open("https://dorsa-co.ir/")))
        return
    

    def sidebar_button_connector(self):
        GUIManager.button_connector( self.ui.sidebar_main_btn, self.sidebar_menu_handler('main') )
        GUIManager.button_connector( self.ui.sidebar_report_btn, self.sidebar_menu_handler('report'))
        GUIManager.button_connector( self.ui.sidebar_settings_btn, self.sidebar_menu_handler('settings') )
        GUIManager.button_connector( self.ui.sidebar_calib_btn, self.sidebar_menu_handler('calibration') )
        GUIManager.button_connector( self.ui.sidebar_users_btn, self.sidebar_menu_handler('user') )
        GUIManager.button_connector( self.ui.sidebar_help_btn, self.sidebar_menu_handler('help') )

        
        
        

    def sidebar_menu_handler(self, pagename):
        def func():
            GUIManager.set_stack_widget_idx( self.ui.main_pages_stackw, self.pages_index[pagename] )
        
        return func
    

    def close_app(self):
        """
        this function closes the app
        Inputs: None
        Returns: None
        """
        # create message to confirm close
        res = self.show_alert_window(title=texts.TITLES['close_app'][self.language], message=texts.WARNINGS['app_close_confirm'][self.language], need_confirm=True, level=1)

        if res:
            self.app_close_flag = True

            # close app window and exit the program
            self.ui.close()
            sys.exit()

    def maxmize_minimize(self):
        """
        this function chages the window size of app
        Inputs: None
        Returns: None
        """
        if self.ui.isMaximized():
            self.ui.showNormal()

        else:
            self.ui.showMaximized()

    def minimize_win(self):
        """
        this function minimizes the app to taskbar
        Inputs: None
        Returns: None
        """
        self.ui.showMinimized()
    
    def show_alert_window(self, title, message, need_confirm=False, level=0):
        """this function is used to create a confirm window
        :param title: _description_, defaults to 'Message'
        :type title: str, optional
        :param message: _description_, defaults to 'Message'
        :type message: str, optional
        :return: _description_
        :rtype: _type_
        """

        level = 0 if level<0 or level>2 else level

        # create message box
        alert_window = QtWidgets.QMessageBox()

        # icon
        if level==0:
            alert_window.setIcon(QtWidgets.QMessageBox.Information)
        elif level==1:
            alert_window.setIcon(QtWidgets.QMessageBox.Warning)
        elif level==2:
            alert_window.setIcon(QtWidgets.QMessageBox.Critical)

        # message and title
        alert_window.setText(message)
        alert_window.setWindowTitle(title)
        # buttons
        if not need_confirm:
            alert_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            alert_window.button(QtWidgets.QMessageBox.Ok).setText(texts.TITLES['ok'][self.language])
        else:
            alert_window.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
            alert_window.button(QtWidgets.QMessageBox.Ok).setText(texts.TITLES['confirm'][self.language])
            alert_window.button(QtWidgets.QMessageBox.Cancel).setText(texts.TITLES['cancel'][self.language])
        
        alert_window.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

        # show
        returnValue = alert_window.exec()

        if not need_confirm:
            return True if returnValue == QtWidgets.QMessageBox.Ok else True
        else:
            return True if returnValue == QtWidgets.QMessageBox.Ok else False


    # def mousePressEvent(self, event):
    #     """mouse press event for moving window

    #     :param event: _description_
    #     """

    #     # accept event only on top and side bars and on top bar
    #     if event.button() == QtCore.Qt.LeftButton and not self.isMaximized() and event.pos().y()<=self.header.height():
    #         self._old_pos = event.globalPos()


    # def mouseReleaseEvent(self, event):
    #     """mouse release event for stop moving window

    #     :param event: _description_
    #     """

    #     if event.button() == QtCore.Qt.LeftButton:
    #         self._old_pos = None


    # def mouseMoveEvent(self, event):
    #     """mouse move event for moving window

    #     :param event: _description_
    #     """

    #     if self._old_pos is None:
    #         return

    #     delta = QtCore.QPoint(event.globalPos() - self._old_pos)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self._old_pos = event.globalPos()


    
class GUIManager:

    @staticmethod
    def set_wgt_visible( wgt:QtWidgets.QWidget, status:bool):
        """changes visibility of a given Qt widget

        Args:
            wgt (QtWidgets.QWidget): a Qt widget like QPushButton
            status (bool): True of visible and False for hide
        """
        wgt.setVisible(status)
            



    #--------------------------------- GLOBAL BUTTON FUNCTIONs ---------------------------------
    @staticmethod
    def button_connector( btn: QtWidgets.QPushButton, func):
        """Connects a PyQt Button clicked event into a function

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            func (_type_): function that execute when event happend
        """
        btn.clicked.connect(partial( func ))

    @staticmethod
    def button_disable( btn: QtWidgets.QPushButton ):
        """disables a PyQt Button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
        """
        btn.setDisabled(True)


    @staticmethod
    def button_enable( btn: QtWidgets.QPushButton ):
        """enables a PyQt Button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
        """
        btn.setDisabled(False)

    @staticmethod
    def button_background( btn: QtWidgets.QPushButton, color):
        """changes background color of button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            color (tuple): color of background in format of 'rgb' or 'rgba'
        """
        #convert rgb to rgba
        if len(color) == 3:
            color+= (255,)

        btn.setStyleSheet(f'background-color: rgba{color}')

    @staticmethod
    def set_button_icon( btn: QtWidgets.QPushButton, path):
        """sets icon of PyQt button

        Args:
            btn (QtWidgets.QPushButton): PyQt button object
            path (_type_): path of icon's file or url of recource's icon
        """
        #load from resources
        if path[0] == ':':
            icon = QtGui.QIcon( path )
        
        #load from file
        else:
            pixmap = QtGui.QPixmap(path)
            icon = QtGui.QIcon( pixmap )
        
        btn.setIcon(icon)
    
    
    #--------------------------------- GLOBAL CheckBoc FUNCTIONs ---------------------------------
    @staticmethod
    def get_checkbox_value(chbox: QtWidgets.QCheckBox) -> bool:
        """returns state of Qt checkbox

        Args:
            chbox (QtWidgets.QCheckBox): Qt CheckBox object

        Returns:
            bool: return True if checked. else return False
        """
        return chbox.isChecked()
    
    @staticmethod
    def checkbox_connector(chbox: QtWidgets.QCheckBox, func):
        """connects a function to event of Qt checkbox change state

        Args:
            chbox (QtWidgets.QCheckBox): Qt CheckBox object
            func (_type_): name of funtion
        """
        chbox.stateChanged.connect(partial( func ))

    #--------------------------------- GLOBAL CheckBoc FUNCTIONs ---------------------------------
    @staticmethod
    def set_label_text(lbl: QtWidgets.QLabel, text:str):
        """sets a text into the given Qt Label

        Args:
            lbl (QtWidgets.QLabel): Qt label object
            text (str): text that you want show in label
        """
        lbl.setText(text)

    #--------------------------------- GLOBAL Input FUNCTIONs ---------------------------------
    @staticmethod
    def get_input_value( inpt: QtWidgets.QSpinBox)-> float:
        """return value of a given spinbox

        Args:
            inpt (QtWidgets.QSpinBox): Qt label object

        Returns:
            float: value of spinbox
        """
        return inpt.value()
    

    #--------------------------------- GLOBAL Tabel FUNCTIONs ---------------------------------
    @staticmethod
    def set_tabel_dim(tabel: QtWidgets.QTableWidget, row:int , col:int):
        """sets number of column and row of given Qt tabel
        if pass 'None' into row or col, it dosen't changed

        Args:
            tabel (QtWidgets.QTableWidget): Qt tabelWidget object
            row (int): numbr fo row
            col (int): number of col
        """
        if col is not None:
            tabel.setColumnCount(col)
        
        if row is not None:
            tabel.setRowCount(row)

    #headers = ['title1', 'title2',...]
    @staticmethod
    def set_tabel_cheaders(tabel: QtWidgets.QTableWidget, headers:list[str]):
        """sets headers of given Qt tabel

        Args:
            tabel (QtWidgets.QTableWidget): Qt tabelWidget object
            headers (list[str]): list of headers. like headers = ['title1', 'title2',...]
        """
        tabel.setHorizontalHeaderLabels(headers)


    @staticmethod
    def set_tabel_cell_color(tabel: QtWidgets.QTableWidget, index:tuple, color=None, bg_color=None):
        """changes text color and background color of custom cell of a given Qt tabel

        Args:
            tabel (QtWidgets.QTableWidget): Qt tabelWidget object
            index (tuple): position of cell (row_idx, col_idx)
            color (_type_, optional): color of text. if pass None, color doesn't change. Defaults to None.
            bg_color (_type_, optional): background color of cell. if pass None, color doesn't change. Defaults to None.
        """
        if bg_color is not None:
            tabel.item(*index).setBackground(QtGui.QColor(*bg_color))

        if color is not None:
            tabel.item(*index).setForeground(QtGui.QBrush(QtGui.QColor(*color)))
        
    @staticmethod
    def set_tabel_cell_widget(tabel: QtWidgets.QTableWidget, idx: tuple, widget):
        """insert a Qt widget (like QPushButton) into a custom cell of given Qt tabel

        Args:
            tabel (QtWidgets.QTableWidget): Qt tabelWidget object
            idx (tuple): position of cell (row_idx, col_idx)
            widget (_type_): Qt widget that you want insert into cell of tabel
        """
        tabel.mainpage_statistics_tabel.setCellWidget(*idx, widget)

    @staticmethod
    def set_tabel_cell_value(tabel: QtWidgets.QTableWidget,index:tuple, value):
        """sets a text or number into custom cell of given Qt table

        Args:
            tabel (QtWidgets.QTableWidget): Qt tabelWidget object
            index (tuple): position of cell (row_idx, col_idx)
            value (_type_): a text or number  that you want set into cell of tabel
        """
        item = QtWidgets.QTableWidgetItem(str(value))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        tabel.setItem(*index, item )

    
    
    @staticmethod
    def set_tabel_row(tabel: QtWidgets.QTableWidget, row:int, values:list):
        """sets a row data into specific row of a given Qt tabel

        Args:
            tabel (QtWidgets.QTableWidget): Qt tabelWidget object
            row (int): index of row that you want insert data into it
            values (list): list of text or number
        """
        for i,value in enumerate(values):
            GUIManager.set_tabel_cell_value(tabel,(row,i), value)
    
    @staticmethod
    def set_tabel_datas(tabel: QtWidgets.QTableWidget, datas:list[list]):
        """sets given data into specific row of a given Qt tabel

        Args:
            tabel (QtWidgets.QTableWidget): Qt tabelWidget object
            datas (list[list]): data of tabel. like [ ['ali','184'], ['hamid', '193']]
        """
        for row, row_datas in enumerate(datas):
            GUIManager.set_tabel_row(tabel, row, row_datas)        



    #--------------------------------- GLOBAL StackWidget FUNCTIONs ---------------------------------
    @staticmethod
    def set_stack_widget_idx(stw: QtWidgets.QStackedWidget, idx ):
        """change current index of given Qt stack widget

        Args:
            stw (QtWidgets.QStackedWidget): Qt stack widget object
            idx (_type_): custom index to set as current index
        """
        stw.setCurrentIndex(idx)



class mainPage:
    
    def __init__(self, ui):
        self.ui = ui
        
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
            'avrage': self.ui.mainpage_avrage_lbl,
            'std': self.ui.mainpage_std_lbl,
            'fps': self.ui.mainpage_fps_lbl

        }

        self.player_btns = {
            'start': self.ui.mainpage_start_btn,
            'stop' : self.ui.mainpage_stop_btn,
            'fast_start': self.ui.mainpage_faststart_btn
        }


        self.bar_chart_widget = BarChart(
                    chart_title = 'Grading',
                    chart_title_color = 'white',
                    axisX_label = 'Rages',
                    axisY_label = 'Percents',
                    chart_background_color = 'black',
                    bar_color = '#0c1a66',
                    axis_color = 'white',
                    axis_grid=False,
                    axisY_range = (0, 100),
                    axisY_tickCount = 10,
                    animation = True,
                    bar_width = 1,
                )


        self.current_status = 'stop'
        self.statistics_tabel = self.ui.mainpage_statistics_tabel
        self.warning_msg_lbl = self.ui.mainpage_warning_massage_lbl
        #self.ui.mainpage_grading_chart_frame



        #Startup operations-----------------
        self.player_buttons_connect_internal()
        GUIManager.set_wgt_visible(self.warning_msg_lbl, False)

        
        
        # self.ui.mainpage_right_frame.addWidget(self.chart1)



    
    def player_buttons_status(self,state):
        def func():
            if state in ['start', 'fast_start']:
                GUIManager.button_disable(self.player_btns['start'])
                GUIManager.button_disable(self.player_btns['fast_start'])
                GUIManager.button_enable(self.player_btns['stop'])
                self.current_status = 'start'
            
            else:
                GUIManager.button_enable(self.player_btns['start'])
                GUIManager.button_enable(self.player_btns['fast_start'])
                GUIManager.button_disable(self.player_btns['stop'])
                self.current_status = 'stop'
        return func
        

    def player_buttons_connect(self,name:str,  func):
        GUIManager.button_connector( self.player_btns[ name ], func)

    
    def player_buttons_connect_internal(self):
        for state, btn in self.player_btns.items():
            GUIManager.button_connector(btn, self.player_buttons_status(state) )

    def set_warning_buttons_status(self, name, status):
        if status:
            GUIManager.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['ok-icon'])
        else:
            GUIManager.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['warning-icon'])
            
    
    def report_btn_connector(self, func):
        GUIManager.button_connector(self.ui.mainpage_stop_btn, func)

    def toolbox_connector(self, func):
        GUIManager.checkbox_connector(self.ui.mainpage_liveview_checkbox, func('live-view'))
        GUIManager.checkbox_connector(self.ui.mainpage_drawing_checkbox, func('drawing'))
    

    def set_information(self, data):
        for name, value in data.items():
            GUIManager.set_label_text( self.informations[name],
                                    str(value) 
                                    )
    
    def set_statistics_tabel_datas(self, datas):
        cols_count = len(datas[0])
        #set cols count
        GUIManager.set_tabel_dim(self.statistics_tabel, None, col=cols_count)
        #insert datas into tabel
        GUIManager.set_tabel_datas(self.statistics_tabel, datas)

        #set first column ( row headers) color diffrence
        for row in range(len(datas)):
            GUIManager.set_tabel_cell_color(self.statistics_tabel, (row,0), bg_color=(6, 76, 130), color=(255,255,255))

    def set_statistics_tabel_headers(self, headers):
        #first columns should be empty for rows header
        headers = [''] + headers
        GUIManager.set_tabel_cheaders(self.statistics_tabel, headers)

    def set_warning_massage(self, text):
        text = "Warning: " + text
        self.warning_msg_lbl.setText(text)
        GUIManager.set_wgt_visible(self.warning_msg_lbl, True)
      
        # self.worker = timerThread()
        # self.thread = QThread()

        # #self.worker.progress.connect(self.update_progress)
        # #self.worker.completed.connect(self.complete)
        # self.worker.moveToThread(self.thread)
        # self.thread.started.connect(self.worker.wait('test', 5, 0.5))

        # self.thread.start()
        # print("DDDD")

        # self.thread = QThread()
        # # Step 3: Create a worker object
        # self.worker = timerThread()
        # self.worker.add('test')
        # # Step 4: Move worker to the thread
        # self.worker.moveToThread(self.thread)
        # # Step 5: Connect signals and slots
        # self.thread.started.connect(self.worker.wait)
        # self.worker.completed.connect(self.thread.quit)
        # self.worker.completed.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        # # Step 6: Start the thread
        # self.thread.start()








class gradingSetting:

    def __init__(self, ui) -> None:
        self.ui = ui

        self.ranges_input = {
            'lower': self.ui.settingpage_grading_low_limit_spinbox,
            'upper': self.ui.settingpage_grading_up_limit_spinbox
        }

        self.defined_ranges_tabel = self.ui.settingpage_grading_ranges_tabel
        selfdefined_ranges_tabel_editor_function = lambda x: None
    
    def add_range_button_connector(self, func):
        data = {}
        for key in self.ranges_input.keys():
            data[key] = self.ui.get_input_value( 
                self.ranges_input[key]
             )
        
        GUIManager.button_connector( self.ui.settingpage_grading_add_range_btn, func(data) )
        
    
    def defined_ranges_tabel_connector(self, func):
        self.defined_ranges_tabel_editor_function = func

    
    def set_ranges_tabel_data(self, datas):
        for row_data in datas:
            pass


# class timerThread(QObject):
#     completed =  pyqtSignal()

#     def __init__(self,) -> None:
#         super().__init__()
#         self.ts = {}
#         self.on_threads_flag = {}

#     def wait(self,name, wait_time, step=1):
#         #set value into ts and flag 
#         self.on_threads_flag[name] = True
#         self.ts[name] = 0

#         #wait untile timer is lower than wait_time
#         while self.ts[name] < wait_time:
#             time.sleep(step)
#             self.ts[name] += step
#             print( self.ts[name] )

#         self.on_threads_flag[name] = False
#         self.completed.emit()


#     def is_thread_running(self, name):
#         return self.on_threads_flag[name]
    
#     def reset_wait_timer(self, name):
#         self.ts[name] = 0

#     def add(self, name):
#         self.ts[name] = 0
#         self.on_threads_flag[name] = False

        
if __name__ == '__main__':

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load(main_ui_file, None)
    global_ui = GlobalUI(window)

    # #window = Ui()
    main_page = mainPage(window)
    #-------------------
    main_page.set_warning_buttons_status('camera_connection', False)
    main_page.set_warning_buttons_status('camera_grabbing', False)
    main_page.set_warning_buttons_status('illumination', False)
    main_page.set_warning_buttons_status('tempreture', False)



    # main_page.set_statistics_tabel_headers(['<6mm', '6mm-8mm', '8mm-10mm', '10mm-12.5mm'])
    # main_page.set_statistics_tabel_datas(datas=[['MEAN', 1,2,3,4],
    #                                       ['STD', 5,1,5,4],
    #                                       ['ovality', 5,1,5,4]
    #                                       ])
    
    
    
    # #main_page.player_buttons_connect('start', lambda :main_page.set_warning_massage('dama balast'))
    
    #-------------------
    window.show()
    

    app.exec_()

    