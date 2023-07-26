from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents




class usersPageUI:
    def __init__(self, ui):
        self.registerTab = RegisterUserTabUI(ui)
        self.allUserTab = AllUserTabUI(ui)



class RegisterUserTabUI:

    def __init__(self, ui) -> None:
        self.ui = ui

        self.register_error_lbl = self.ui.userspage_register_error_lbl
        self.register_btn = self.ui.userspage_add_user_btn

        self.register_users_field = {
            'username' : self.ui.userpage_username_inpt,
            'password' : self.ui.userpage_password_inpt,
            'password_confirm': self.ui.userpage_confirm_password_inpt,
            'role': self.ui.userpage_user_role_combobox
        }
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



class AllUserTabUI:

    def __init__(self, ui) -> None:
        self.ui = ui
        self.users_table = self.ui.userpage_all_users_table
        self.__table_external_event_function__ = None

        self.users_table_headers = ['id', 'username', 'password', 'role', 'edit', 'delete']
        GUIBackend.set_table_dim(self.users_table, row=10, col=len(self.users_table_headers))
        GUIBackend.set_table_cheaders(self.users_table, self.users_table_headers)


    def table_external_event_connector(self, func):
        """connect edit and delete button of each record in users tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, user info dic, 'edit' or 'delete' flag, button )
        """
        self.__table_external_event_function__ = func
    
    def __table_event_connector__(self,idx, user_info, status, btn):
        """this function exec when edit or delete button clicked on defined ranges table

        Args:
            idx (_type_): row index that its button clicked
            user_info (_type_): user info dictionary in format {'username':****, 'password':****', 'role':****}
            status (_type_): be 'delete' when delete button clicked and 'edit' when edit button clicked
            btn (_type_): button object that clicked
        """
        def func():
            #
            # Write Internal Code Here
            #
            self.__table_external_event_function__(idx, user_info, status, btn)
        return func

    def set_users_table(self,users:list[dict]):
        """insert users info into table
        Args:
            datas (list[list]): list of users info
        """
        assert self.__table_external_event_function__ is not None, "ERROR: First determine an event Function for edit and delete button by 'AllUserTab.__table_event_connector__' method "
        
        #set row count
        users_count = len(users)
        GUIBackend.set_table_dim(self.users_table, row=users_count, col=None)
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
            GUIBackend.button_connector( edit_btn, self.__table_event_connector__(row, user, 'edit',  edit_btn) )
            GUIBackend.button_connector( del_btn, self.__table_event_connector__(row, user, 'delete',  del_btn ) )

            #insert buttons into table
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count), edit_btn)
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count+1), del_btn)

    def show_confirm_box(Self, title, massage, buttons):
        cmb = GUIComponents.confirmMessageBox(title, massage, buttons = buttons)
        return cmb.render()