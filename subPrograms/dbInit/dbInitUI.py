
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
import time

class dbInitUI:
    ui_path = 'uiFiles\\db_init.ui'

    def __init__(self,) -> None:

        self.ui = GUIBackend.load_ui(self.ui_path)

        self.master_password_inpt = self.ui.master_password_inpt
        self.next_btn = self.ui.next_btn
        self.prev_btn = self.ui.prev_btn
        self.pages_frame = self.ui.pages
        self.close_btn = self.ui.close_btn
        self.error_lbl = self.ui.error_lbl

        self.db_meta = {
            'database_username': self.ui.db_username_inpt,
            'database_password': self.ui.db_password_inpt,
            'database_host': self.ui.db_host_inpt,

        }
        
        GUIBackend.set_win_frameless(self.ui)
        GUIBackend.button_connector(self.close_btn, self.close)
        GUIBackend.button_connector(self.prev_btn, self.go_prev_page)

        GUIBackend.set_input_password(self.master_password_inpt)
        GUIBackend.set_input_password(self.db_meta['database_password'])

        self.startup()
    
    def startup(self):
        self.set_page(0)
        GUIBackend.set_input(self.db_meta['database_host'], 'localhost')
        GUIBackend.button_disable(self.prev_btn)
        self.write_error(None)

    def get_page(self):
        return GUIBackend.get_stack_widget_idx(self.pages_frame)
    
    def set_page(self, idx):
        return GUIBackend.set_stack_widget_idx(self.pages_frame, idx)
    
    def go_next_page(self,):
        max_page_idx = GUIBackend.get_stack_widget_count(self.pages_frame) - 1
        idx = GUIBackend.get_stack_widget_idx(self.pages_frame)
        
        idx += 1
        idx = min(idx, max_page_idx)

        GUIBackend.set_stack_widget_idx(self.pages_frame, idx)
        self.write_error(None)
        GUIBackend.button_enable(self.prev_btn)
        if idx == max_page_idx:
            GUIBackend.set_button_text(self.next_btn, 'Finish')
    
    def go_prev_page(self,):
        idx = GUIBackend.get_stack_widget_idx(self.pages_frame)
        idx -= 1
        idx = max(idx, 0)
        
        GUIBackend.set_stack_widget_idx(self.pages_frame, idx)
        self.write_error(None)
        GUIBackend.set_button_text(self.next_btn, 'Next')

        if idx == 0:
            GUIBackend.button_disable(self.prev_btn)
        else:
            GUIBackend.button_enable(self.prev_btn)



    def next_button_connector(self, func):
        GUIBackend.button_connector(self.next_btn, func)
    
    def get_maser_password(self,):
        return GUIBackend.get_input(self.master_password_inpt)
    
    def set_maser_password(self,txt):
        return GUIBackend.set_input(self.master_password_inpt, txt)
    
    def get_db_meta(self):
        data = {}
        for key, field in self.db_meta.items():
            data[key] = GUIBackend.get_input(field)
        return data
    
    def write_error(self, txt):
        if txt is None:
            GUIBackend.set_wgt_visible(self.error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.error_lbl, False)
            def func():
                GUIBackend.set_wgt_visible(self.error_lbl, True)
                GUIBackend.set_label_text(self.error_lbl, txt)
            GUIComponents.single_timer_runner(50, func)
    
    

    def show(self,):
        GUIBackend.show_window(self.ui, True)
    
    def close(self):
        GUIBackend.close_window(self.ui)