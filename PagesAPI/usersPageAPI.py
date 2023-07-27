from dorsaPylon import Collector

from PagesUI.usersPageUI import usersPageUI, RegisterUserTabUI, AllUserTabUI, LoginUserBoxUI, EditUserTabUI
from Database.usersDB import usersDB
from backend.UserManager.userLoginRegister import passwordManager, regiterUtils
import CONSTANTS


class usersPageAPI:

    def __init__(self, ui:usersPageUI,database:usersDB):
        self.ui = ui
        self.database = database

        self.login_flag = False
        self.logined_user = {}

        self.registerUser = RegisterUserTabAPI(ui.registerTab, database)
        self.allUser = AllUserTabAPI(ui.allUserTab, database)
        self.loginUser = LoginBoxAPI(self.ui.loginUserBox, self.database)
        self.editUser = EditUserTabAPI(self.ui.editUserTab, self.database)

        self.registerUser.set_register_event(self.new_user_register_event)
        self.loginUser.set_login_event_func(self.user_login_event)
        self.editUser.set_user_edit_event_func(self.user_edited_event)

    def startup(self,):
        pass
    
    def new_user_register_event(self,):
        self.allUser.load_users()
    
    def user_login_event(self,):
        self.login_flag = self.loginUser.login_flag
        self.logined_user = self.loginUser.logined_user

        self.editUser.set_logined_user(self.logined_user, self.login_flag)
    
    def user_edited_event(self):
        edited_user = self.editUser.get_edited_user()
        self.logined_user = edited_user
        self.loginUser.update_logedin_user(edited_user)
        self.allUser.load_users()


class LoginBoxAPI:

    def __init__(self, ui:LoginUserBoxUI, database:usersDB) -> None:
        self.ui = ui
        self.database = database

        self.login_flag = False
        self.logined_user = {}
        self.login_event_func = None

        #this button is login button on top of software
        self.ui.profile_login_logout_button_connector(self.login_logout)
        #this button is login button on login dialog box
        self.ui.login_button_connector(self.login)

    def set_login_event_func(self, func):
        self.login_event_func = func
    
    def login_logout(self):
        """this function called when loging_logout button in top of wofrware pressed
        """
        if not self.login_flag:
            self.ui.show_login()
        
        else :
            flag = self.ui.show_logout(self.logined_user['username'])
            if flag:
                self.logout()


    def login(self):
        """this function call when login button on dialogbox pressed
        """
        input_user = self.ui.get_login_inputs()
        username = input_user['username']
        password = input_user['password']

        if len(password) == 0 or len(username) == 0:
            self.ui.write_login_error('Please enter all fields')
            return
        
        if not self.database.is_exist(username):
            self.ui.write_login_error("Username dosen't exist")
            return
        
        user_db = self.database.load(username)
        if not passwordManager.check_password(password, user_db['password']):
            self.ui.write_login_error("Password is wrong")
            return
        #this flag shows a user is login or not
        self.login_flag = True
        #store logedin user
        self.logined_user = user_db
        #show logedin username on top of sofrware
        self.ui.set_logedin_username(user_db['username'])
        #clear username and password from input fields
        self.ui.clear_login_inputs()
        self.ui.close_window()
        self.ui.set_toolbar_login_button_icon('logout')

        if self.login_event_func is not None:
            self.login_event_func()



    def logout(self):
        #this flag shows a user is login or not
        self.login_flag = False
        #clear logedin user info
        self.logined_user = {}
        #clear logedin username on top of sofrware
        self.ui.set_logedin_username("")
        self.ui.set_toolbar_login_button_icon('login')

        if self.login_event_func is not None:
            self.login_event_func()

    

    def update_logedin_user(self, user) :
        self.logined_user = user
        self.ui.set_logedin_username(user['username'])






class RegisterUserTabAPI:

    def __init__(self, ui:RegisterUserTabUI ,database: usersDB):
        self.ui = ui
        self.database = database
        self.register_event_func = None
        self.ui.register_button_connector(self.register)
    
    def register(self,):
        user_inputs = self.ui.get_register_fields()

        if len(user_inputs['username']) < CONSTANTS.MIN_USERNAME_LENGHT:
            self.ui.write_register_error('Username is Should be at least 3 character')
            return
        
        if self.database.is_exist(user_inputs['username']):
            self.ui.write_register_error('Username is already exist!')
            return
        
        if not regiterUtils.is_pass_lenght_ok(user_inputs['password']):
            self.ui.write_register_error("Password should be at least {}".format(CONSTANTS.MIN_PASS_LENGHT))
            return

        if not user_inputs['password'] == user_inputs['password_confirm']:
            self.ui.write_register_error("Password and password confirm aren't same")
            return
        
        #make password hash
        user_inputs['password'] = passwordManager.hash_password(user_inputs['password'])
        #remove password_confirm for save in database
        user_inputs.pop('password_confirm')
        #save in database
        self.database.save(user_inputs)
        self.ui.reset()

        if self.register_event_func is not None:
            self.register_event_func()


    def set_register_event(self, func):
        self.register_event_func = func



class AllUserTabAPI:

    def __init__(self, ui:AllUserTabUI ,database: usersDB):
        self.ui = ui
        self.database = database

        self.ui.table_external_event_connector(self.modify_users)

        self.load_users()

    

    def load_users(self,):
        users = self.database.load_all()
        self.ui.set_users_table(users)



    def modify_users(self,idx, user, flag, btn):
        if flag == 'delete':
            response = self.ui.show_confirm_box("Delete User",
                                                "Are you shoure to delete '{}' ?".format(user['username']),
                                                  buttons=['yes', 'cancel'])
            if response == 'cancel':
                return
            
            self.database.remove(user['username'])
            self.load_users()

        if flag == 'edit':
            print('edit', user)
       




class EditUserTabAPI:

    def __init__(self, ui:EditUserTabUI ,database: usersDB):
        self.ui = ui
        self.database = database
        self.logined_user = {}
        self.login_flag = False
        self.user_edit_event_func = None

        self.ui.update_profile_button_connector(self.update_profile)
        self.ui.change_password_button_connector(self.change_password)


    def set_user_edit_event_func(self, func):
        self.user_edit_event_func = func

    def set_logined_user(self, user, flag):
        self.logined_user = user
        self.login_flag = flag
        self.ui.set_edit_profile_fields(user)

    def update_profile(self):
        if not self.login_flag:
            self.ui.write_edit_profile_error("Please login first")
            return

        new_info = self.ui.get_edit_profile_fields()

        if len(new_info['username']) < CONSTANTS.MIN_USERNAME_LENGHT:
            self.ui.write_edit_profile_error("Username should be at least 3 character!")
            return

        if new_info['username'] != self.logined_user['username']:
            if self.database.is_exist(new_info['username']):
                self.ui.write_edit_profile_error("This Username is already exist!")
                return

        self.database.remove(self.logined_user['username'])    

        for key , value in new_info.items():
            self.logined_user[key] = value

        self.database.save(self.logined_user)

        if self.user_edit_event_func is not None:
            self.user_edit_event_func()
    
    def get_edited_user(self):
        return self.logined_user
    

    def change_password(self):
        info = self.ui.get_change_password_fields()

        if not passwordManager.check_password(info['old_password'], self.logined_user['password']):
            self.ui.write_change_password_error('Old password is Incorect')
            return
        
        if len(info['new_password']) < CONSTANTS.MIN_PASS_LENGHT:
            self.ui.write_change_password_error("Password should be at least {} character".format(CONSTANTS.MIN_PASS_LENGHT))
            return

        
        if info['new_password'] != info['confirm_new_password']:
            self.ui.write_change_password_error("New password and it's confirm aren't same")
            return
        
        
        new_password = info['new_password']
        hashed_new_password = passwordManager.hash_password(new_password)
        self.logined_user['password'] = hashed_new_password
        self.database.save(self.logined_user)
        
        self.ui.write_change_password_error(None)
        self.ui.clear_change_password_fields()

        if self.user_edit_event_func is not None:
            self.user_edit_event_func()

        
        

        


        
        
    

        