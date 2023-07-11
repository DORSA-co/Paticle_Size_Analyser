import os
import typing
import sys

#os.system('cmd /c "pyrcc5 -o Assets.py Assets.qrc"') #PyQt
os.system('CMD /C pyside6-rcc Assets.qrc -o Assets.py')#PySide
sys.path.append( os.getcwd() + "/pages_UI" )

#from PyQt5 import uic
from PySide6 import QtWidgets, QtCore, QtGui 
from PySide6.QtUiTools import QUiLoader
import webbrowser
from functools import partial
import texts
import Assets
#from PySide6.QtChart import QChart, QChartView, QBarSet,QPercentBarSeries
import time
from Charts.BarChart import BarChart
import GUIComponents
import cv2
main_ui_file = 'main_UI.ui'

from settingUI import settingUI

class UiHandeler:
    def __init__(self, ui):
        self.setting = settingUI(ui)

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

        webbrowser
        # chrome_path_win = "C://Program Files//Google//Chrome//Application//chrome.exe"
        # chrome_path_linux = '/usr/bin/google-chrome %s'
        # if sys.platform.startswith('win'):
            # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_win))
        # elif sys.platform.startswith('linux'):
            # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_linux))

        # button connector

        self.pages_index = {
            'main'       : 0,
            'report'     : 1,
            'settings'   : 2,
            'calibration': 3,
            'user'       : 4,
            'help'       : 5
        }

        
        self.sidebar_buttons = {
            'main': self.ui.sidebar_main_btn,
            'report': self.ui.sidebar_report_btn,
            'settings': self.ui.sidebar_settings_btn,
            'calibration': self.ui.sidebar_calib_btn,
            'user': self.ui.sidebar_users_btn,
            'help': self.ui.sidebar_help_btn,
        }


        self.header_button_connector()
        self.sidebar_button_connector()

        # startup settings
        self.startup_settings()

        

    

        
    #-------------------------------------------------------------------------------------------


    def startup_settings(self):
        """this function is used to do startup settings on app start
        """
        return

    def header_button_connector(self):
        """this function is used to connect ui buttons to their functions
        """
        GUIBackend.button_connector( self.ui.minimize_btn, self.minimize_win )
        GUIBackend.button_connector( self.ui.maximize_btn, self.maxmize_minimize )
        GUIBackend.button_connector( self.ui.close_btn, self.close_app )
        # bottom window buttens
        #self.dorsa_url_btn.clicked.connect(partial(lambda: webbrowser.open("https://dorsa-co.ir/")))
        return
    

    def sidebar_button_connector(self):
        for page_name in self.sidebar_buttons.keys():
            GUIBackend.button_connector( self.sidebar_buttons[page_name], self.sidebar_menu_handler(page_name) )
        

        
        
        

    def sidebar_menu_handler(self, pagename):
        def func():
            GUIBackend.set_stack_widget_idx( self.ui.main_pages_stackw, self.pages_index[pagename] )
            for btn in self.sidebar_buttons.values():
                btn.setStyleSheet(GUIComponents.SIDEBAR_BUTTON_STYLE)
            
            self.sidebar_buttons[pagename].setStyleSheet(GUIComponents.SIDEBAR_BUTTON_SELECTED_STYLE)
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

       
if __name__ == '__main__':

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load(main_ui_file, None)
    global_ui = GlobalUI(window)
    main_page = mainPage(window)
    grading_setting_page = gradingSettingTab(window)
    calib_page = CalibrationPage(window)
    all_users_tab = AllUserTab(window)
    camera_setting_tab = cameraSettingTab(window)

    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))

    #------------------------------------------------------------
    main_page.set_warning_buttons_status('camera_connection', False)
    main_page.set_warning_buttons_status('camera_grabbing', False)
    main_page.set_warning_buttons_status('illumination', False)
    main_page.set_warning_buttons_status('tempreture', False)



    main_page.set_statistics_table_headers(['<6mm', '6mm-8mm', '8mm-10mm', '10mm-12.5mm'])
    main_page.set_statistics_table_datas(datas=[['Avrage', 1,2,3,4],
                                          ['STD', 5,1,5,4],
                                          ['ovality', 5,1,5,4],
                                          ['Variance', 5,1,5,4],
                                          ])
    
    
    #------------------------------------------------------------
    # #main_page.player_buttons_connect('start', lambda :main_page.set_warning_massage('dama balast'))
    def test_func(idx, data, status, btn):
            print(idx, data, status)
    
    grading_setting_page.external_ranges_table_connector(test_func)
    grading_setting_page.set_ranges_table_data([[1,4,6],[2,6,8]])
    #------------------------------------------------------------

    calib_page.set_calib_tabel(['2022/12/01','18:30', '0.1', 'mean', '5'])
    calib_page.write_calib_result(0.2, 0.1)
    settings = calib_page.get_settings()
    print(settings)

    #------------------------------------------------------------
    def test_users_func(idx, users, status, btn):
        print(users, status)

    all_users_tab.table_external_event_connector(test_users_func)
    
    all_users_tab.set_users_table([{'username':'amir', 'password':'******', 'role': 'user'},
                                    {'username':'its.big', 'password':'********', 'role': 'admin'}])
    #------------------------------------------------------------
    
    #------------------------------------------------------------
    def test_change_cam_setting(arg):
        print(arg)
    camera_setting_tab.change_setting_event_connector(test_change_cam_setting)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------

    from main_API import main_API

    api = main_API(global_ui)
    #collector = Collector()

    #get avialble cameras That Are GigE

    #-----------------------------------------------------------------
    # #get all avialble cameras 
    # all_cameras = collector.get_all_cameras(camera_class=None)
    # print(all_cameras)

    # #-----------------------------------------------------------------
    # #get specific camera
    # cam = collector.get_camera_by_serial('23804186')
    # print(cam)
    # cam.Operations.start_grabbing()
    # #define your ideal pixel_type, defualt is BGR8
    # cam.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)
    # #-----------------------------------------------------------------
    # img = cam.getPictures()
    # cv2.imshow('img', img)
    # cv2.waitKey(20)

    

    # cth = cameraThread(cam)
    # thread = QThread()
    # cth.moveToThread(thread)
    # thread.started.connect(cth.grabber)
    # cth.success_grab_signal.connect(test)
    # thread.start()




    window.show()
    

    app.exec()

    