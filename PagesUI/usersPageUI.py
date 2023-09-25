from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
import CONSTANTS
from PagesUI.PageUI import commonUI


class usersPageUI:
    def __init__(self, ui, login_ui, edit_user_ui):
        #self.login_ui = login_ui
        self.registerTab = RegisterUserTabUI(ui)
        self.allUserTab = AllUserTabUI(ui, edit_user_ui)
        self.loginUserBox = LoginUserBoxUI(ui, login_ui)
        self.editUserTab = EditUserTabUI(ui)


class LoginUserBoxUI:

    def __init__(self, ui, login_ui,) -> None:
        self.ui = ui
        self.login_ui = login_ui


        self.logined_username_lbl = self.ui.toolbar_logined_username_lbl
        
        self.toolbar_login_logout_btn = self.ui.toolbar_login_logout_btn

        GUIBackend.set_input_password(self.login_ui.password_input)
        GUIBackend.set_win_frameless(self.login_ui)
        GUIBackend.button_connector(self.login_ui.close_btn, self.close_login_window)
        #GUIBackend.button_connector(self.login_logout_button, self.show_window)
        #self.show_login()
    
    def close_login_window(self,):
        self.login_ui.close()
        self.clear_login_inputs()

        
    def profile_login_logout_button_connector(self, func):
        GUIBackend.button_connector(self.toolbar_login_logout_btn, func)
    
    def login_button_connector(self, func):
        GUIBackend.button_connector(self.login_ui.login_btn, func)

    #def register_button_connector(self, func):
    #    GUIBackend.button_connector(self.login_ui.register_btn, func)

    def show_login(self):
        self.write_login_error(None)
        GUIBackend.show_window(self.login_ui, always_on_top=True)

    def close_window(self):
        GUIBackend.close_window(self.login_ui)


    def get_login_inputs(self):
        username = GUIBackend.get_input(self.login_ui.username_input)
        password = GUIBackend.get_input(self.login_ui.password_input)
        return {'username':username.lower(), 'password':password}

    def clear_login_inputs(self):
        GUIBackend.set_input(self.login_ui.username_input, "")
        GUIBackend.set_input(self.login_ui.password_input, "")

    def write_login_error(self, txt:str):
        """Write Errors message in Logun

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.login_ui.login_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.login_ui.login_error_lbl, True)
            GUIBackend.set_label_text( self.login_ui.login_error_lbl, txt)


    def set_logedin_username(self, username):
        if username is None:
            GUIBackend.set_wgt_visible(self.logined_username_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.logined_username_lbl, True)
            GUIBackend.set_label_text( self.logined_username_lbl, username)


    def show_logout(Self, username):
        cmb = GUIComponents.confirmMessageBox('logout', 
                                              "{} do you want logout?".format(username), buttons = ['yes', 'no'])
        btn = cmb.render() 
        return btn == 'yes'
            

    def set_toolbar_login_button_icon(self, state:str):
        """change icon of login_logout button in toolbar of top of software

        Args:
            state (str): flags that determine icon. it could be 'login' or 'logout'
        """
        if state == 'login':
            GUIBackend.set_button_icon(self.toolbar_login_logout_btn, ":/assets/icons/icons8-user-50.png")
        
        elif state == 'logout':
            GUIBackend.set_button_icon(self.toolbar_login_logout_btn, ":/assets/icons/icons8-logout-white-50.png")
            



class RegisterUserTabUI:
    
    def __init__(self, ui) -> None:
        self.ui = ui    

        self.register_error_lbl = self.ui.userspage_register_error_lbl
        self.register_success_lbl = self.ui.userspage_register_success_lbl
        self.register_success_box = self.ui.userspage_register_success_frame
        self.register_btn = self.ui.userspage_add_user_btn


        self.register_users_field = {
            'username' : self.ui.userpage_username_inpt,
            'password' : self.ui.userpage_password_inpt,
            'password_confirm': self.ui.userpage_confirm_password_inpt,
            'role': self.ui.userpage_user_role_combobox
        }

        
        #set input type as password to show password as *
        for name in ['password', 'password_confirm']:
            GUIBackend.set_input_password(self.register_users_field[name])
        
        self.hide_success_msg()
        self.reset()

    def reset(self):
        """reset ui to default
        """
        self.set_register_fields( {
            'username' : "",
            'password' : "",
            'password_confirm': "",
        })
        self.write_register_error(None)

    
    def set_user_roles_items(self, items: list[str]):
        GUIBackend.set_combobox_items(self.register_users_field['role'], items)

    def register_button_connector(self, func):
        """connect function into register button clicked event
        """
        GUIBackend.button_connector(self.register_btn, func)
    
    def get_register_fields(self)-> dict:
        """returns register fields in dictionary type

        Returns:
            dict: infos in format {
            'username':xxxx,
            'password':xxxx,
            'password_confirm':xxxx,
            'role':xxxx,}
        """
        infos = {}
        for name, field in self.register_users_field.items():
            infos[name] = GUIBackend.get_input(field)
        
        infos['username'] = infos['username'].lower()
        return infos
    

    def set_register_fields(self, data:dict):
        """set register fields

        data (dict):
            input datas informat like {
                'username':xxxx,
                'password':xxxx,
                'password_confirm':xxxx,
        """
        for name, value in data.items():
            GUIBackend.set_input(self.register_users_field[name], value)
        
    
    
    def write_register_error(self, txt:str):
        """Write Errors message in Register

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.register_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.register_error_lbl, True)
            GUIBackend.set_label_text( self.register_error_lbl, txt)

    def show_success_msg(self, txt):
        #diologbox = GUIComponents.confirmMessageBox('congratulations', txt, buttons=['ok'])
        #diologbox.render()
        GUIBackend.set_wgt_visible( self.register_success_box, True)
        GUIBackend.set_label_text( self.register_success_lbl, txt)
        GUIComponents.single_timer_runner(3000, self.hide_success_msg)


    def hide_success_msg(self):
        GUIBackend.set_wgt_visible(self.register_success_box, False)
        #hide massage affter 300 msec
        







class AllUserTabUI(commonUI):

    def __init__(self, ui, edit_user_ui) -> None:
        self.ui = ui
        self.edit_user_ui = edit_user_ui

        self.users_table = self.ui.userpage_all_users_table
        self.__table_external_event_function__ = None

        self.edit_box_fields = {
            'username': self.edit_user_ui.username_input, 
            'password': self.edit_user_ui.password_input,
            'role': self.edit_user_ui.role_combobox,
        }

        self.users_table_headers = ['id', 'username', 'password', 'role', 'edit', 'delete']
        GUIBackend.set_table_dim(self.users_table, row=10, col=len(self.users_table_headers))
        GUIBackend.set_table_cheaders(self.users_table, self.users_table_headers)
        GUIBackend.set_win_frameless(self.edit_user_ui)
        GUIBackend.button_connector(self.edit_user_ui.cancel_btn, self.close_edit_user_box)
        

    def edit_user_save_button_connector(self, func):
        GUIBackend.button_connector(self.edit_user_ui.save_btn, func)


    def table_external_event_connector(self, func):
        """connect edit and delete button of each record in users tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, user info dic, 'edit' or 'delete' flag, button )
        """
        self.__table_external_event_function__ = func
    

    def set_users_table(self,users:list[dict]):
        """insert users info into table
        Args:
            datas (list[list]): list of users info
        """
        
        assert self.__table_external_event_function__ is not None, "ERROR: First determine an event Function for edit and delete button by 'AllUserTab.__table_event_connector__' method "
        
        #set row count
        users_count = len(users)
        GUIBackend.set_table_dim(self.users_table, row=users_count, col=None)

        if users_count == 0:
            return
        
        info_count = len(users[0])

        for row, user in enumerate(users):
            for info_name in user.keys():
                col = self.users_table_headers.index(info_name)
                value = user[info_name]
                if info_name == 'password':
                    value = '•'*8
                GUIBackend.set_table_cell_value(self.users_table, (row, col), value=value)

            #define edit and delete button
            edit_btn = GUIComponents.editButton()
            del_btn = GUIComponents.deleteButton()

            #connect buttons to event function 
            GUIBackend.button_connector_argument_pass( edit_btn, self.__table_external_event_function__, args=(row, user, 'edit',  edit_btn) )
            GUIBackend.button_connector_argument_pass( del_btn, self.__table_external_event_function__, args = (row, user, 'delete',  del_btn ) )

            #insert buttons into table
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count), edit_btn)
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count+1), del_btn)

    


    def show_edit_user_box(self, user):
        self.set_edit_user_box_inputs(user)
        self.write_edit_user_error(None)
        GUIBackend.show_window(self.edit_user_ui, True)

    def set_edit_user_box_inputs(self, user):
        for field_name, field in self.edit_box_fields.items():
            GUIBackend.set_input( field, user[field_name])

    def get_edit_user_box_inputs(self):
        user_info = {}
        for field_name, field in self.edit_box_fields.items():
            user_info[field_name] = GUIBackend.get_input( field, )
        return user_info


    


    def set_edit_user_roles(self, roles):
        GUIBackend.set_combobox_items(self.edit_user_ui.role_combobox, roles)

    def close_edit_user_box(self,):
        GUIBackend.close_window(self.edit_user_ui)
        for field_name, field in self.edit_box_fields.items():
            GUIBackend.set_input( field, "")




    def write_edit_user_error(self, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.edit_user_ui.error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.edit_user_ui.error_lbl, True)
            GUIBackend.set_label_text(self.edit_user_ui.error_lbl, txt)






class EditUserTabUI:

    def __init__(self, ui) -> None:
        self.ui = ui
        

        self.update_profile_btn = self.ui.userpage_editprofile_update_btn
        self.cancel_edit_profile_btn = self.ui.userpage_editprofile_cancel_btn
        self.change_password_btn = self.ui.userpage_editprofile_change_password_btn
        self.change_password_error_lbl = self.ui.userpage_editprofile_changepass_error_lbl
        self.edit_profile_error_lbl = self.ui.userpage_editprofile_edit_error_lbl
        self.success_msg_frame = self.ui.userspage_editprofile_success_frame
        self.success_msg_lbl = self.ui.userspage_editprofile_success_lbl

        self.change_password_fields = {
            'old_password': self.ui.userpage_editprofile_old_password_inpt,
            'new_password': self.ui.userpage_editprofile_new_password_inpt,
            'confirm_new_password': self.ui.userpage_editprofile_confirm_new_password_inpt,
        }

        self.edit_profile_fields = {
            'username': self.ui.userpage_editprofile_username_inpt,
            'role': self.ui.userpage_editprofile_user_role_combobox,
        }

        
        for name in ['old_password', 'new_password', 'confirm_new_password']:
            GUIBackend.set_input_password(self.change_password_fields[name])
        

        self.write_change_password_error(None)
        self.write_edit_profile_error(None)
        self.hide_success_msg()


    def update_profile_button_connector(self, func):
        GUIBackend.button_connector(self.update_profile_btn, func)

    def cancel_edit_profile_button_connector(self, func):
        GUIBackend.button_connector(self.cancel_edit_profile_btn, func)

    def change_password_button_connector(self, func):
        GUIBackend.button_connector(self.change_password_btn, func)

    def set_user_roles_items(self, items: list[str]):
        GUIBackend.set_combobox_items(self.edit_profile_fields['role'], items)

    
    def get_change_password_fields(self,):
        data = {}
        for name, filed in self.change_password_fields.items():
            data[name] = GUIBackend.get_input(filed)

        return data
    
    def clear_change_password_fields(self,):
        for name, filed in self.change_password_fields.items():
            GUIBackend.set_input(filed, "")

    def get_edit_profile_fields(self,):
        data = {}
        for name, field in self.edit_profile_fields.items():
            data[name] = GUIBackend.get_input(field)
        
        data['username'] = data['username'].lower() 
        return data


    def set_edit_profile_fields(self, data):
        if data == {}:
            for name, field in self.edit_profile_fields.items():
                GUIBackend.set_input(field, "")
        else:
            for name, field in self.edit_profile_fields.items():
                GUIBackend.set_input(field, data[name])
        

    
    

    def write_change_password_error(self, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.change_password_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.change_password_error_lbl, True)
            GUIBackend.set_label_text( self.change_password_error_lbl, txt)

    
    def write_edit_profile_error(self, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.edit_profile_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.edit_profile_error_lbl, True)
            GUIBackend.set_label_text( self.edit_profile_error_lbl, txt)


    def show_success_msg(self, txt):
        #diologbox = GUIComponents.confirmMessageBox('congratulations', txt, buttons=['ok'])
        #diologbox.render()
        GUIBackend.set_wgt_visible( self.success_msg_frame, True)
        GUIBackend.set_label_text( self.success_msg_lbl, txt)
        GUIComponents.single_timer_runner(3000, self.hide_success_msg)


    def hide_success_msg(self):
        GUIBackend.set_wgt_visible(self.success_msg_frame, False)