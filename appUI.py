import os
import sys
import time

from uiFiles.main_UI_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

#----------------------Compile Resource File-----------------------
sys.path.append( os.getcwd() + "/pagesUI" )
sys.path.append( os.getcwd() + "/uiUtils" )
sys.path.append( os.getcwd() + "/backend" )
sys.path.append( os.getcwd() + "/backend/Camera" )
sys.path.append( os.getcwd() + "/PagesAPI" )
sys.path.append( os.getcwd() + "/PagesUI" )
#------------------------------------------------------------------


#Import Pages UI------------------------------------------
from PagesUI.settingPageUI import settingPageUI
from PagesUI.mainPageUI import mainPageUI
from PagesUI.validationPageUI import validationPageUI
from PagesUI.usersPageUI import usersPageUI
from PagesUI.reportsPageUI import reportsPageUI
from PagesUI.standardsPageUI import standardsPageUI
from PagesUI.reportPageUI import reportPageUI
from PagesUI.comparePageUI import comparePageUI
from PagesUI.hmiPageUI import hmiPageUI

#---------------------------------------------------------
from uiUtils import GUIComponents
from uiUtils.guiBackend import GUIBackend
import Constants.CONSTANTS as CONSTANTS
from uiUtils.IO.Mouse import mouseHandeler, MouseEvent



class mainUI(QMainWindow):
    def __init__(self, login_ui, edit_user, db_init_ui):
        #self.__global_setting__ = GlobalUI(ui)
        super(mainUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.popupLoading = GUIComponents.overlayMassage(text='Loading...')

        self.mouseHandeler = mouseHandeler()

        self.login_ui = login_ui
        self.edit_user = edit_user
        self.db_init_ui = db_init_ui

        self.__win_old_pos = (0,0)
        self.move_refresh_time = 0

        self.settingPage = settingPageUI(self.ui)
        self.reportsPage = reportsPageUI(self.ui)
        self.gradingRange = standardsPageUI(self.ui)
        self.mainPage = mainPageUI(self.ui)
        self.reportPage = reportPageUI(self.ui)
        self.usersPage = usersPageUI(self.ui, login_ui, edit_user)
        self.comparePage = comparePageUI(self.ui)
        self.validationPage = validationPageUI(self.ui)
        self.validationPage = validationPageUI(self.ui)
        self.hmiPage = hmiPageUI(self.ui)


        #self.router = routerUI(ui)

        self.current_page = ('main', 0)
        self.previous_page = ('help', 0)
        self.external_change_page_event = None
        self.sidebar_frame = self.ui.sidebar

        self.pages_index = {
            'main'              : 0,
            'reports'           : 1,
            'grading_ranges'    : 2,
            'hmi'               : 3,
            'settings'          : 4,
            'calibration'       : 5,
            'user'              : 6,
            'help'              : 7,
            'report'            : 8,
            'compare'           : 9,
        }
        
        self.sidebar_pages_buttons = {
            'main': self.ui.sidebar_main_btn,
            'reports': self.ui.sidebar_report_btn,
            'grading_ranges': self.ui.sidebar_grading_ranges_btn,
            'hmi': self.ui.sidebar_hmi_btn,
            'settings': self.ui.sidebar_settings_btn,
            'calibration': self.ui.sidebar_calib_btn,
            'user': self.ui.sidebar_users_btn,
            'help': self.ui.sidebar_help_btn,
        
        }

        self.tabs:dict[str, tuple] = {
            'sample_setting':    (self.ui.settingpage_tabs, self.ui.settingpage_sample_tab),
            'storage_setting':   (self.ui.settingpage_tabs, self.ui.settingpage_storage_tab),
            'camera_setting':    (self.ui.settingpage_tabs, self.ui.settingpage_camera_tab),
            'plc_setting':       (self.ui.settingpage_tabs, self.ui.settingpage_plc_tab),
            'algorithm_setting': (self.ui.settingpage_tabs, self.ui.settingpage_algorithm_tab),
            'config_setting':    (self.ui.settingpage_tabs, self.ui.settingpage_config_tab),

            'register_user':     (self.ui.user_tabs, self.ui.user_register_tab),
            'edit_user':         (self.ui.user_tabs, self.ui.user_profile_tab),
            'all_users':         (self.ui.user_tabs, self.ui.all_users_tab),
        }

        self.__not_activa_tabs = []


        self.headrs_button = {
            'minimize': self.ui.minimize_btn,
            'maximize': self.ui.maximize_btn,
            'close': self.ui.close_btn,
        }


        
        self.all_style_repoblish()
        self.header_button_connector()
        self.sidebar_button_connector()
        GUIBackend.set_win_frameless(self)
        

        self.mouseHandeler.connect_all(self.ui.header, self.header_mouse_event)


    def all_style_repoblish(self,):
        #for widget in self.ui.
        for atr_name in dir(self.ui):
            atr = getattr(self.ui, atr_name)
            try:
                atr.style().unpolish(atr)
                atr.style().polish(atr)
            except:
                pass

    def header_mouse_event(self,e:MouseEvent):
        if e.is_move():
            #update moving window every 10ms
            if time.time() - self.move_refresh_time > 0.01:
                if GUIBackend.is_maximize(self):
                    GUIBackend.show_normal(self)
                    
                self.move_refresh_time = time.time()
                new_pos = e.get_postion()
                delta = new_pos - self.__win_old_pos
                GUIBackend.relative_move(self, tuple(delta))

        elif e.is_click() and e.is_left_btn():
            self.__win_old_pos = e.get_postion()
 
    #-------------------------------------------------------------------------------------------
    def change_page_connector(self,func):
        self.external_change_page_event = func

    # def hide_tab(self,)

    def internal_change_page_event(self, current_page_name, new_page_name):
        """this event happend user clicked new page that is diffrent from current page
        and calls external event func

        Args:
            name (str): name of current page
            idx (str): name of new page that its button clicked
        """
        if self.external_change_page_event is not None:
            self.external_change_page_event(current_page_name, new_page_name)



    def header_button_connector(self):
        """this function is used to connect ui buttons to their functions
        """
        GUIBackend.button_connector( self.headrs_button['minimize'], lambda :GUIBackend.minimize_win(self) )
        GUIBackend.button_connector( self.headrs_button['maximize'], lambda :GUIBackend.maxmize_minimize(self) )
        GUIBackend.button_connector( self.headrs_button['close'], self.close_win )
    
    

    def sidebar_button_connector(self):
        for page_name in self.sidebar_pages_buttons.keys():
            GUIBackend.button_connector( self.sidebar_pages_buttons[page_name], self.sidebar_menu_handler(page_name) )
        


    def sidebar_menu_handler(self, new_page_name:str):
        """event happend when side bar menu button clicked

        Args:
            new_page_name (str): name of page that its button clicked
        """
        def func():
            current_page_idx = GUIBackend.get_stack_widget_idx(self.ui.main_pages_stackw)
            new_page_idx = self.pages_index[new_page_name]

            if current_page_idx != new_page_idx:
                #pass new page index and name to internal_change_page_event method
                self.internal_change_page_event(self.current_page[0], new_page_name)
        return func
    

    def __change_page__(self,new_page_name:str):
        """changes page of ui

        Args:
            new_page_name (str): name of new page
        """
        new_page_idx = self.pages_index[new_page_name]
        self.previous_page = self.current_page
        self.current_page = (new_page_name, new_page_idx)

        GUIBackend.set_stack_widget_idx( self.ui.main_pages_stackw,  new_page_idx)
        #save new page into and previous page
        
        
        #reset styles of all btns (actully for rest style of buttons of previous page)
        if new_page_name in self.sidebar_pages_buttons.keys():
            for btn in self.sidebar_pages_buttons.values():
                btn.setProperty("activeStyle",False)
                btn.style().unpolish(btn)
                btn.style().polish(btn)
        
            #set style to button of new page to make it diffrent
            # self.sidebar_pages_buttons[new_page_name].setStyleSheet(GUIComponents.SIDEBAR_BUTTON_SELECTED_STYLE)
            btn = self.sidebar_pages_buttons[new_page_name]
            btn.setProperty("activeStyle",True)
            btn.style().unpolish(btn)
            btn.style().polish(btn)



    def get_current_page(self,) -> tuple[str, int]:
        """returns current page's name and index

        Returns:
            tuple[str, int]: (name of current page, index of current page)
        """
        return self.current_page
    
    def get_previous_page(self,)-> tuple[str, int]:
        """returns previous page's name and index

        Returns:
            tuple[str, int]: tuple[str, int]: (name of previous page, index of previous page)
        """
        return self.previous_page
    
    
    def go_to_page(self, page_name):
        """changes page to

        Args:
            page_name (_type_): _description_
        """
        if page_name in CONSTANTS.HIDE_SIDEBAR_PAGES:
            self.show_sidebar(False)
        else:
            self.show_sidebar(True)
        
        self.__change_page__(page_name)
    
    def set_access_pages(self, pages:list[str], flag:bool = True):
        """enable or disable some pages

        Args:
            pages (list[str]): list of page names 
            flag (bool): if True, make pages enable. if False, make pages disable
        """
        if isinstance(pages, str):
            if pages == 'all':
                pages = list(self.sidebar_pages_buttons.keys())

        for page_name in self.sidebar_pages_buttons.keys():
            btn = self.sidebar_pages_buttons[page_name]
            if page_name in pages:
                GUIBackend.set_wgt_visible( btn, flag )
            else:
                GUIBackend.set_wgt_visible(btn , not(flag))
        
        self.go_to_page(pages[0])

    


    
    def set_access_tabs(self, tabs: list[str], flag:bool = True):
        """enable or disable some tabs

        Args:
            tabs (dict[list]): list of tabs name
            flag (bool): if True, make tabs enable. if False, make tabs disable
        """
        if isinstance(tabs, str):
            if tabs == 'all':
                tabs = self.tabs.keys()
        for tab_name in self.tabs:
            tab_parent, tab = self.tabs[tab_name]
            
            if tab_name in self.__not_activa_tabs:
                continue

            if tab_name in tabs:
                GUIBackend.set_visible_tab(tab_parent, tab, True)

            else:
                GUIBackend.set_visible_tab(tab_parent, tab, False)


    def deactive_tab(self, tab_name:str):
        self.__not_activa_tabs.append(tab_name)
        tab_parent, tab = self.tabs[tab_name]
        GUIBackend.set_visible_tab(tab_parent, tab, False)


    def show(self,):
        self.showMaximized()

    def close_win(self, force=False):
        """shows dialog box for closing application
        """
        if not force:
            btn = self.show_confirm_box('Close', 'Are you sure close app?',['yes','no'])
            if btn == 'no':
                return
    
        GUIBackend.close_app(self)

    
    def show_sidebar(self, flag):
        if not flag:
            GUIBackend.set_frame_max_size(self.sidebar_frame, w=0, h=None)
            GUIBackend.set_frame_min_size(self.sidebar_frame, w=0, h=None)
        else:
            GUIBackend.set_frame_max_size(self.sidebar_frame, w=CONSTANTS.SIDEBAR_MAX_WIDTH, h=None)
            GUIBackend.set_frame_min_size(self.sidebar_frame, w=CONSTANTS.SIDEBAR_MIN_WIDTH, h=None)

    def show_confirm_box(Self, title, massage, buttons):
        cmb = GUIComponents.confirmMessageBox(title, massage, buttons = buttons)
        return cmb.render()
        
    
    def show_db_init(self):
        GUIBackend.set_win_frameless(self.db_init_ui)
        GUIBackend.show_window(self.db_init_ui, True)

    def change_cursure(self, name):
        GUIBackend.cursor_changer(name)
        



