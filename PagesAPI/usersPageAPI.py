from dorsaPylon import Collector

from PagesUI.usersPageUI import usersPageUI, RegisterUserTabUI, AllUserTabUI, LoginUserBoxUI, EditUserTabUI
from Database.usersDB import usersDB
from backend.UserManager.userLoginRegister import passwordManager, regiterUtils
import CONSTANTS
#from main_UI import routerUI


class dataPasser:
    def __init__(self) -> None:
        self.login_flag = False
        self.logined_user = {}
        #self.logined_user = {'role':'admin'}

    def get_logined_user_role(self,):
        return self.logined_user.get('role', CONSTANTS.UNLOGIN_USER_ROLE)


class usersPageAPI:

    def __init__(self, ui:usersPageUI,database:usersDB, ):
        self.ui = ui
        self.database = database
        self.data_passer = dataPasser()
        #self.router = router
        
        
        self.external_login_func_event = None

        self.registerUser = RegisterUserTabAPI(ui.registerTab, database, self.data_passer)
        self.allUser = AllUserTabAPI(ui.allUserTab, database, self.data_passer)
        self.loginUser = LoginBoxAPI(self.ui.loginUserBox, self.database, self.data_passer)
        self.editUser = EditUserTabAPI(self.ui.editUserTab, self.database, self.data_passer)

        self.registerUser.set_register_event(self.new_user_register_event)
        self.loginUser.set_login_event_func(self.user_login_event)
        self.editUser.set_user_edit_event_func(self.user_edited_event)

    def startup(self,):
        pass

    def set_login_event(self, func):
        self.external_login_func_event = func
    
    def new_user_register_event(self,):
        self.allUser.load_users()
    
    def user_login_event(self,):
        self.editUser.update_logined_user()
        self.registerUser.set_available_user_roles()
        if self.external_login_func_event is not None:
            self.external_login_func_event()
    
    def user_edited_event(self):
        self.loginUser.update_logedin_user()
        self.registerUser.set_available_user_roles()
        self.allUser.load_users()


class LoginBoxAPI:

    def __init__(self, ui:LoginUserBoxUI, database:usersDB, data_passer:dataPasser) -> None:
        self.ui = ui
        self.database = database
        self.data_passer = data_passer

        #self.login_flag = False
        #self.logined_user = {}
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
        if not self.data_passer.login_flag:
            self.ui.show_login()
        
        else :
            flag = self.ui.show_logout(self.data_passer.logined_user['username'])
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
        self.data_passer.login_flag = True
        #store logedin user
        self.data_passer.logined_user = user_db
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
        self.data_passer.login_flag = False
        #clear logedin user info
        self.data_passer.logined_user = {}
        #clear logedin username on top of sofrware
        self.ui.set_logedin_username("")
        self.ui.set_toolbar_login_button_icon('login')

        if self.login_event_func is not None:
            self.login_event_func()

    

    def update_logedin_user(self) :
        self.ui.set_logedin_username(self.data_passer.logined_user['username'])






class RegisterUserTabAPI:

    def __init__(self, ui:RegisterUserTabUI ,database: usersDB, data_passer: dataPasser):
        self.ui = ui
        self.database = database
        self.data_passer = data_passer

        self.register_event_func = None
        self.ui.register_button_connector(self.register)
        self.set_available_user_roles()
        


    def set_available_user_roles(self):
        logined_user_role = self.data_passer.get_logined_user_role()
        self.ui.set_user_roles_items( CONSTANTS.USER_ROlES_ACCESS[logined_user_role] )
    
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
        self.ui.show_success_msg('Success Register')

        if self.register_event_func is not None:
            self.register_event_func()


    def set_register_event(self, func):
        self.register_event_func = func

    











class AllUserTabAPI:

    def __init__(self, ui:AllUserTabUI ,database: usersDB, data_passer:dataPasser):
        self.ui = ui
        self.database = database
        self.data_passer = data_passer

        self.ui.table_external_event_connector(self.modify_users)

        self.load_users()

        #all user tab is only accessable by admin, so the user role absolutly is admin
        self.ui.set_edit_user_roles(CONSTANTS.USER_ROlES_ACCESS['admin'])
        self.ui.edit_user_save_button_connector(self.save_edit_user) 

    

    def load_users(self,):
        users = self.database.load_all()
        self.ui.set_users_table(users)
        self.selected_user_for_edit = {}



    def modify_users(self,idx, user, flag, btn):
        if flag == 'delete':
            response = self.ui.show_confirm_box("Delete User",
                                                "Are you sure you want to delete '{}' ?".format(user['username']),
                                                  buttons=['yes', 'cancel'])
            if response == 'cancel':
                return
            
            self.database.remove(user['username'])
            self.load_users()

        if flag == 'edit':    
            self.selected_user_for_edit = user
            self.ui.show_edit_user_box(user)
    

    def save_edit_user(self,):
        new_info = self.ui.get_edit_user_box_inputs()
        #check if password change, hash new password
        if self.selected_user_for_edit['password'] != new_info['password']:
            #check new password has enough lengh
            if len(new_info['password']) < CONSTANTS.MIN_PASS_LENGHT:
                self.ui.write_change_password_error("Password should be at least {} character".format(CONSTANTS.MIN_PASS_LENGHT))
                return
            
            new_info['password'] = passwordManager.hash_password(new_info['password'])

        #check if username change, remove previous in database
        if self.selected_user_for_edit['username'] != new_info['username']:
            #check new username not taken befor bu another
            if self.database.is_exist(new_info['username']):
                self.ui.write_edit_user_error("This User name is already exist")
                return
        
        #remove previous record
        self.database.remove(self.selected_user_for_edit['username'])
        self.database.save(new_info)
        self.load_users()
        self.ui.close_edit_user_box()



class EditUserTabAPI:

    def __init__(self, ui:EditUserTabUI ,database: usersDB, data_passer:dataPasser):
        self.ui = ui
        self.database = database
        self.data_passer = data_passer

        self.user = {}

        self.user_edit_event_func = None

        self.ui.update_profile_button_connector(self.update_profile)
        self.ui.change_password_button_connector(self.change_password)
        self.set_available_user_roles()
        


    def set_available_user_roles(self):
        logined_user_role = self.data_passer.get_logined_user_role()
        self.ui.set_user_roles_items( CONSTANTS.USER_ROlES_ACCESS[logined_user_role] )

    def set_user_edit_event_func(self, func):
        self.user_edit_event_func = func

    def update_logined_user(self,):
        self.set_available_user_roles()
        self.ui.set_edit_profile_fields(self.data_passer.logined_user)

    def update_profile(self):
        login_flag = self.data_passer.login_flag
        logined_user = self.data_passer.logined_user

        if not login_flag:
            self.ui.write_edit_profile_error("Please login first")
            return

        new_info = self.ui.get_edit_profile_fields()

        if len(new_info['username']) < CONSTANTS.MIN_USERNAME_LENGHT:
            self.ui.write_edit_profile_error("Username should be at least 3 character!")
            return

        if new_info['username'] != logined_user['username']:
            if self.database.is_exist(new_info['username']):
                self.ui.write_edit_profile_error("This Username is already exist!")
                return 
            

        #remove old user information from database
        self.database.remove(logined_user['username'])    

        #update information
        for key , value in new_info.items():
            logined_user[key] = value
        
        #updated logined user information
        self.data_passer.logined_user = logined_user
        #save new logined user information into database
        self.database.save(logined_user)
        
        self.ui.show_success_msg("User Information Updated")
        if self.user_edit_event_func is not None:
            self.user_edit_event_func()
    

    def change_password(self):
        info = self.ui.get_change_password_fields()


        if len(info['old_password']) == 0 or len(info['new_password']) == 0 or len(info['confirm_new_password']) == 0:
            self.ui.write_change_password_error('Please Complete all fields')
            return

        if not passwordManager.check_password(info['old_password'], self.data_passer.logined_user['password']):
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
        self.data_passer.logined_user['password'] = hashed_new_password
        self.database.save(self.data_passer.logined_user)
        
        self.ui.write_change_password_error(None)
        self.ui.clear_change_password_fields()
        self.ui.show_success_msg("password changed")

        if self.user_edit_event_func is not None:
            self.user_edit_event_func()

        
        

        


        
        
    

        