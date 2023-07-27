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
login_ui_file = 'login.ui'

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
from main_API import main_API


#Import Pages UI------------------------------------------
from settingPageUI import settingPageUI
from mainPageUI import mainPageUI
from calibrationPageUI import calibrationPageUI
from usersPageUI import usersPageUI
from reportsPageUI import reportsPageUI
#---------------------------------------------------------
from guiBackend import GUIBackend

class mainUI:
    def __init__(self, ui, login_ui):
        #self.__global_setting__ = GlobalUI(ui)
        self.ui = ui
        self.login_ui = login_ui

        self.settingPage = settingPageUI(ui)
        self.reportsPage = reportsPageUI(ui)
        self.mainPage = mainPageUI(ui)
        self.calibrationPage = calibrationPageUI(ui)
        self.usersPage = usersPageUI(ui, login_ui)

        self.current_page = ('main', 0)
        self.external_change_page_event = None

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

        self.headrs_button = {
            'minimize': self.ui.minimize_btn,
            'maximize': self.ui.maximize_btn,
            'close': self.ui.close_btn,
        }

        self.header_button_connector()
        self.sidebar_button_connector()
        GUIBackend.set_win_frameless(self.ui)

    
        
        

    

        
    #-------------------------------------------------------------------------------------------
    def change_page_connector(self,func):
        self.external_change_page_event = func

    def internal_change_page_event(self, name, idx):
        if self.external_change_page_event is not None:
            self.external_change_page_event(name, idx)



    def header_button_connector(self):
        """this function is used to connect ui buttons to their functions
        """
        GUIBackend.button_connector( self.headrs_button['minimize'], lambda :GUIBackend.minimize_win(self.ui) )
        GUIBackend.button_connector( self.headrs_button['maximize'], lambda :GUIBackend.maxmize_minimize(self.ui) )
        GUIBackend.button_connector( self.headrs_button['close'], self.close )
    
    

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
   
    def get_current_page(self,):
        return self.current_page
    

    def close(self):
        dialog_box = GUIComponents.confirmMessageBox('close', 'Are you sure?', buttons = ['yes', 'no'])
        flag = dialog_box.render()
        if flag == 'yes':
            GUIBackend.close_app(self.ui)

        
       
if __name__ == '__main__':

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    #load .ui files
    window = loader.load(main_ui_file, None)
    login_ui = loader.load(login_ui_file, None)
    #global_ui = GlobalUI(window)

    all_uis = mainUI(window, login_ui)

    
    api = main_API(all_uis)
    

    #------------------------------------------------------------
    # all_uis.mainPage.set_warning_buttons_status('camera_connection', False)
    # all_uis.mainPage.set_warning_buttons_status('camera_grabbing', False)
    # all_uis.mainPage.set_warning_buttons_status('illumination', False)
    # all_uis.mainPage.set_warning_buttons_status('tempreture', False)

    # all_uis.mainPage.set_statistics_table_headers(['<6mm', '6mm-8mm', '8mm-10mm', '10mm-12.5mm'])
    # all_uis.mainPage.set_statistics_table_datas(datas=[['Avrage', 1,2,3,4],
    #                                       ['STD', 5,1,5,4],
    #                                       ['ovality', 5,1,5,4],
    #                                       ['Variance', 5,1,5,4],
    #                                       ])
    
    
    # # #------------------------------------------------------------

    # all_uis.calibrationPage.set_calib_tabel(['2022/12/01','18:30', '0.1', 'mean', '5'])
    # all_uis.calibrationPage.write_calib_result(0.2, 0.1)
    # settings = all_uis.calibrationPage.get_settings()
    # print(settings)

    #------------------------------------------------------------
    
   

    window.show()
    
    

    app.exec()

    