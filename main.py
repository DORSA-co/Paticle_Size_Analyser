import os
os.system('cmd /c "pyrcc5 -o Assets.py Assets.qrc"')

from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtSvg 
import sys
import webbrowser
from functools import partial
import texts
import Assets

from PySide6.QtSvg import *
from PyQt5.QtChart import QChart, QChartView, QBarSet,QPercentBarSeries



main_ui_file = 'main_UI.ui'

class Ui(QtWidgets.QMainWindow):
    """this class is used to build class for mainwindow to load GUI application

    :param QtWidgets: _description_
    """

    def __init__(self):
        """this function is used to laod ui file and build GUI application
        """
        
        super(Ui, self).__init__()
        
        # app language
        self.language = 'en'

        # load ui file
        uic.loadUi(main_ui_file, self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

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

        






    #--------------------------------- GLOBAL BUTTON FUNCTIONs ---------------------------------
    def button_connector(self, btn: QtWidgets.QPushButton, func):
        btn.clicked.connect(partial( func ))

    def button_disable(self,  btn: QtWidgets.QPushButton ):
        btn.setDisabled(True)

    def button_enable(self,  btn: QtWidgets.QPushButton ):
        btn.setDisabled(False)

    def button_background(self, btn: QtWidgets.QPushButton, color):
        #convert rgb to rgba
        if len(color) == 3:
            color+= (255,)

        btn.setStyleSheet(f'background-color: rgba{color}')

    def set_button_icon(self, btn: QtWidgets.QPushButton, path):
        #load from resources
        if path[0] == ':':
            icon = QtGui.QIcon( path )
        
        #load from file
        else:
            pixmap = QtGui.QPixmap(path)
            icon = QtGui.QIcon( pixmap )
        
        btn.setIcon(icon)
    
    #--------------------------------- GLOBAL CheckBoc FUNCTIONs ---------------------------------
    def get_checkbox_value(self, chbox: QtWidgets.QCheckBox):
        return chbox.isChecked()
    
    def checkbox_connector(self, chbox: QtWidgets.QCheckBox, func):
        chbox.stateChanged.connect(partial( func ))

    #--------------------------------- GLOBAL CheckBoc FUNCTIONs ---------------------------------
    def set_label_text(self, lbl: QtWidgets.QLabel, text:str):
        lbl.setText(text)

    #--------------------------------- GLOBAL Input FUNCTIONs ---------------------------------
    def get_input_value(self, inpt: QtWidgets.QSpinBox):
        return inpt.value()
        
    #-----------------------------------------------------------------------------------


    def startup_settings(self):
        """this function is used to do startup settings on app start
        """
        return

    def header_button_connector(self):
        """this function is used to connect ui buttons to their functions
        """
        self.button_connector( self.minimize_btn, self.minimize_win )
        self.button_connector( self.maximize_btn, self.maxmize_minimize )
        self.button_connector( self.close_btn, self.close_app )
        # bottom window buttens
        self.dorsa_url_btn.clicked.connect(partial(lambda: webbrowser.open("https://dorsa-co.ir/")))
        return
    

    def sidebar_button_connector(self):
        self.button_connector( self.sidebar_main_btn, self.sidebar_menu_handler('main') )
        self.button_connector( self.sidebar_report_btn, self.sidebar_menu_handler('report'))
        self.button_connector( self.sidebar_settings_btn, self.sidebar_menu_handler('settings') )
        self.button_connector( self.sidebar_calib_btn, self.sidebar_menu_handler('calibration') )
        self.button_connector( self.sidebar_users_btn, self.sidebar_menu_handler('user') )
        self.button_connector( self.sidebar_help_btn, self.sidebar_menu_handler('help') )

        
        
        

    def sidebar_menu_handler(self, pagename):
        def func():
            self.main_pages_stackw.setCurrentIndex(self.pages_index[pagename])
        
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
            self.close()
            sys.exit()

    def maxmize_minimize(self):
        """
        this function chages the window size of app
        Inputs: None
        Returns: None
        """
        if self.isMaximized():
            self.showNormal()

        else:
            self.showMaximized()

    def minimize_win(self):
        """
        this function minimizes the app to taskbar
        Inputs: None
        Returns: None
        """
        self.showMinimized()
    
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


    def mousePressEvent(self, event):
        """mouse press event for moving window

        :param event: _description_
        """

        # accept event only on top and side bars and on top bar
        if event.button() == QtCore.Qt.LeftButton and not self.isMaximized() and event.pos().y()<=self.header.height():
            self._old_pos = event.globalPos()


    def mouseReleaseEvent(self, event):
        """mouse release event for stop moving window

        :param event: _description_
        """

        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None


    def mouseMoveEvent(self, event):
        """mouse move event for moving window

        :param event: _description_
        """

        if self._old_pos is None:
            return

        delta = QtCore.QPoint(event.globalPos() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPos()


    
        


class mainPage:
    
    def __init__(self, ui: Ui):
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

        self.current_status = 'stop'


        #Startup operations-----------------
        self.player_buttons_connect_internal()




    def player_buttons_status(self,state):
        def func():
            if state in ['start', 'fast_start']:
                self.ui.button_disable(self.player_btns['start'])
                self.ui.button_disable(self.player_btns['fast_start'])
                self.ui.button_enable(self.player_btns['stop'])
                self.current_status = 'start'
            
            else:
                self.ui.button_enable(self.player_btns['start'])
                self.ui.button_enable(self.player_btns['fast_start'])
                self.ui.button_disable(self.player_btns['stop'])
                self.current_status = 'stop'
        return func
        

    def player_buttons_connect(self,name:str,  func):
        self.ui.button_connector( self.player_btns[ name ], func)

    
    def player_buttons_connect_internal(self):
        for state, btn in self.player_btns.items():
            self.ui.button_connector(btn, self.player_buttons_status(state) )

    def set_warning_buttons_status(self, name, status):
        if status:
            self.ui.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['ok-icon'])
        else:
            self.ui.set_button_icon(self.warning_btns[name]['btn'],
                                     self.warning_btns[name]['warning-icon'])
            

    
    def report_btn_connector(self, func):
        self.ui.button_connector(self.ui.mainpage_stop_btn, func)

    def toolbox_connector(self, func):
        self.ui.checkbox_connector(self.ui.mainpage_liveview_checkbox, func('live-view'))
        self.ui.checkbox_connector(self.ui.mainpage_drawing_checkbox, func('drawing'))
    
    {'ovality': 0.7}

    def set_information(self, data):
        for name, value in data.items():
            self.ui.set_label_text( self.informations[name],
                                    str(value) 
                                    )
        



class gradingSetting:

    def __init__(self, ui) -> None:
        self.ui = ui

        self.ranges_input = {
            'lower': self.ui.settingpage_grading_low_limit_spinbox,
            'upper': self.ui.settingpage_grading_up_limit_spinbox
        }

    
    def add_range_button_connector(self, func):
        data = {}
        for key in self.ranges_input.keys():
            data[key] = self.ui.get_input_value( 
                self.ranges_input[key]
             )
        
        self.ui.button_connector( self.ui.settingpage_grading_add_range_btn, func(data) )
        
        
        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    main_page = mainPage(window)
    main_page.set_warning_buttons_status('illumination', False)
    window.show()
    app.exec_()