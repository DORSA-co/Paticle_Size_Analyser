import os
import typing
import sys

#----------------------Compile Resource File-----------------------
#os.system('cmd /c "pyrcc5 -o Assets.py Assets.qrc"') #PyQt
os.system('CMD /C pyside6-rcc Assets.qrc -o Assets.py')#PySide

#----------------------Add Lib Files to path-----------------------
sys.path.append( os.getcwd() + "/pagesUI" )
sys.path.append( os.getcwd() + "/uiUtils" )
sys.path.append( os.getcwd() + "/backend" )
sys.path.append( os.getcwd() + "/backend/Camera" )
sys.path.append( os.getcwd() + "/PagesAPI" )
sys.path.append( os.getcwd() + "/PagesUI" )
#------------------------------------------------------------------
main_ui_file = 'main_UI.ui'

#----------------------Load Madouls -------------------------------
from PySide6 import QtWidgets, QtCore, QtGui 
from PySide6.QtUiTools import QUiLoader
import webbrowser
from functools import partial
import texts
import Assets
import time
import GUIComponents
import cv2


#Import Pages UI------------------------------------------
from settingPageUI import settingPageUI
from mainPageUI import mainPageUI
from calibrationPageUI import calibrationPageUI
from usersPageUI import usersPageUI
from reportsPageUI import reportsPageUI
#---------------------------------------------------------
from guiBackend import GUIBackend

class UIs:
    def __init__(self, ui):
        self.__global_setting__ = GlobalUI(ui)

        self.settingPage = settingPageUI(ui)
        self.reportsPage = reportsPageUI(ui)
        self.mainPage = mainPageUI(ui)
        self.calibrationPage = calibrationPageUI(ui)
        self.usersPage = usersPageUI(ui)

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

        
        # chrome_path_win = "C://Program Files//Google//Chrome//Application//chrome.exe"
        # chrome_path_linux = '/usr/bin/google-chrome %s'
        # if sys.platform.startswith('win'):
            # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_win))
        # elif sys.platform.startswith('linux'):
            # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path_linux))

        # button connector

        self.current_page = ('main', 0)

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

        self.external_change_page_event = None

        

    

        
    #-------------------------------------------------------------------------------------------
    def change_page_connector(self,func):
        self.external_change_page_event = func

    def internal_change_page_event(self, name, idx):
        if self.external_change_page_event is not None:
            self.external_change_page_event(name, idx)

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
            current_page_idx = GUIBackend.get_stack_widget_idx(self.ui.main_pages_stackw)
            new_page_idx = self.pages_index[pagename]

            if current_page_idx != new_page_idx:
                #pass new page index and name to internal_change_page_event method
                self.internal_change_page_event(pagename, new_page_idx)

                GUIBackend.set_stack_widget_idx( self.ui.main_pages_stackw,  new_page_idx)
                #save new page into an atribute for some using
                self.current_page = (pagename, new_page_idx)
                
                #reset styles of all btns (actully for rest style of buttons of previous page)
                for btn in self.sidebar_buttons.values():
                    btn.setStyleSheet(GUIComponents.SIDEBAR_BUTTON_STYLE)
                
                #set style to button of new page to make it diffrent
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


    def get_current_page(self,):
        return self.current_page
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
    #global_ui = GlobalUI(window)
    all_uis = UIs(window)



    # screen = app.primaryScreen()
    # print('Screen: %s' % screen.name())
    # size = screen.size()
    # print('Size: %d x %d' % (size.width(), size.height()))
    # rect = screen.availableGeometry()
    # print('Available: %d x %d' % (rect.width(), rect.height()))

    #------------------------------------------------------------
    all_uis.mainPage.set_warning_buttons_status('camera_connection', False)
    all_uis.mainPage.set_warning_buttons_status('camera_grabbing', False)
    all_uis.mainPage.set_warning_buttons_status('illumination', False)
    all_uis.mainPage.set_warning_buttons_status('tempreture', False)

    all_uis.mainPage.set_statistics_table_headers(['<6mm', '6mm-8mm', '8mm-10mm', '10mm-12.5mm'])
    all_uis.mainPage.set_statistics_table_datas(datas=[['Avrage', 1,2,3,4],
                                          ['STD', 5,1,5,4],
                                          ['ovality', 5,1,5,4],
                                          ['Variance', 5,1,5,4],
                                          ])
    
    
    # #------------------------------------------------------------

    all_uis.calibrationPage.set_calib_tabel(['2022/12/01','18:30', '0.1', 'mean', '5'])
    all_uis.calibrationPage.write_calib_result(0.2, 0.1)
    settings = all_uis.calibrationPage.get_settings()
    print(settings)

    #------------------------------------------------------------
    

    # #------------------------------------------------------------
    # def test_users_func(idx, users, status, btn):
    #     print(users, status)

    # all_users_tab.table_external_event_connector(test_users_func)
    
    # all_users_tab.set_users_table([{'username':'amir', 'password':'******', 'role': 'user'},
    #                                 {'username':'its.big', 'password':'********', 'role': 'admin'}])
    # #------------------------------------------------------------
    all_uis.reportsPage.set_standards_filter_table_data (['Gondle1', 'Gondle2'])
    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------

    from main_API import main_API

    api = main_API(all_uis)
   

    window.show()
    

    app.exec()

    