import os
import sys
import Constants.CONSTANTS as CONSTANTS


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
#---------------------------------------------------------
from uiUtils import GUIComponents
from uiUtils.guiBackend import GUIBackend

class routerUI:

    def __init__(self, ui) -> None:
        self.ui = ui
        self.pages_index = {
            'main'              : 0,
            'reports'           : 1,
            'grading_ranges'    : 2,
            'settings'          : 3,
            'calibration'       : 4,
            'user'              : 5,
            'help'              : 6
        }

        self.tabs = {
            'general_setting':   (self.ui.settingpage_tabs, 0),
            'sample_setting':    (self.ui.settingpage_tabs, 1),
            'export_setting':    (self.ui.settingpage_tabs, 2),
            'storage_setting':   (self.ui.settingpage_tabs, 3),
            'camera_setting':    (self.ui.settingpage_tabs, 4),
            'algorithm_setting': (self.ui.settingpage_tabs, 5),
            
            
            

            'register_user':     (self.ui.user_tabs, 0),
            'edit_user':         (self.ui.user_tabs, 1),
            'all_users':         (self.ui.user_tabs, 2),
        }

        self.main_pages_stackw = self.ui.main_pages_stackw
        
    def go(self, pagename, tabname=None):
        GUIBackend.set_stack_widget_idx(self.main_pages_stackw, self.pages_index[pagename])

        if tabname is not None:
            tab_obj, idx = self.tabs[tabname]
            GUIBackend.set_current_tab( tab_obj,  idx)


class mainUI:
    def __init__(self, ui, login_ui, sample_info, edit_user, auto_rebuild_ui, single_rebuild_manual_ui, db_init_ui):
        #self.__global_setting__ = GlobalUI(ui)
        self.ui = ui
        self.login_ui = login_ui
        self.sample_info = sample_info
        self.edit_user = edit_user
        self.auto_rebuild_ui = auto_rebuild_ui
        self.db_init_ui = db_init_ui

        self.settingPage = settingPageUI(ui)
        self.reportsPage = reportsPageUI(ui, auto_rebuild_ui)
        self.gradingRange = standardsPageUI(ui)
        self.mainPage = mainPageUI(ui, sample_info)
        self.reportPage = reportPageUI(ui, single_rebuild_manual_ui)
        self.usersPage = usersPageUI(ui, login_ui, edit_user)
        self.comparePage = comparePageUI(ui)
        self.validationPage = validationPageUI(ui)

        #self.router = routerUI(ui)

        self.current_page = ('main', 0)
        self.previous_page = ('help', 0)
        self.external_change_page_event = None
        self.sidebar_frame = self.ui.sidebar

        self.pages_index = {
            'main'              : 0,
            'reports'           : 1,
            'grading_ranges'    : 2,
            'settings'          : 3,
            'calibration'       : 4,
            'user'              : 5,
            'help'              : 6,
            'report'            : 7,
            'compare'           : 8,
        }
        
        self.sidebar_pages_buttons = {
            'main': self.ui.sidebar_main_btn,
            'reports': self.ui.sidebar_report_btn,
            'grading_ranges': self.ui.sidebar_grading_ranges_btn,
            'settings': self.ui.sidebar_settings_btn,
            'calibration': self.ui.sidebar_calib_btn,
            'user': self.ui.sidebar_users_btn,
            'help': self.ui.sidebar_help_btn,
        
        }

        self.tabs = {
            'general_setting':   (self.ui.settingpage_tabs, 0),
            'sample_setting':    (self.ui.settingpage_tabs, 1),
            'storage_setting':   (self.ui.settingpage_tabs, 2),
            'camera_setting':    (self.ui.settingpage_tabs, 3),
            'algorithm_setting': (self.ui.settingpage_tabs, 4),
            'register_user':     (self.ui.user_tabs, 0),
            'edit_user':         (self.ui.user_tabs, 1),
            'all_users':         (self.ui.user_tabs, 2),
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
        GUIBackend.button_connector( self.headrs_button['minimize'], lambda :GUIBackend.minimize_win(self.ui) )
        GUIBackend.button_connector( self.headrs_button['maximize'], lambda :GUIBackend.maxmize_minimize(self.ui) )
        GUIBackend.button_connector( self.headrs_button['close'], self.close )
    
    

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
                btn.setStyleSheet(GUIComponents.SIDEBAR_BUTTON_STYLE)
        
            #set style to button of new page to make it diffrent
            self.sidebar_pages_buttons[new_page_name].setStyleSheet(GUIComponents.SIDEBAR_BUTTON_SELECTED_STYLE)

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
            obj, idx = self.tabs[tab_name]
            if tab_name in tabs:
                GUIBackend.set_visible_tab(obj, idx, flag)
            else:
                GUIBackend.set_visible_tab(obj, idx, not(flag))

    def show(self,):
        self.ui.showMaximized()

    def close(self, force=False):
        """shows dialog box for closing application
        """
        if not force:
            btn = self.show_confirm_box('Close', 'Are you sure close app?',['yes','no'])
            if btn == 'no':
                return
        GUIBackend.close_app(self.ui)

    
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

    