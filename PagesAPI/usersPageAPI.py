from dorsaPylon import Collector

from PagesUI.usersPageUI import usersPageUI, RegisterUserTabUI, AllUserTabUI
from Database.usersDB import usersDB
from backend.UserManager.userLoginRegister import passwordManager, regiterUtils
import CONSTANTS


class usersPageAPI:

    def __init__(self, ui:usersPageUI ,database:usersDB):
        self.ui = ui
        self.database = database

        self.registerUser = RegisterUserTabAPI(ui.registerTab, database)
        self.allUser = AllUserTabAPI(ui.allUserTab, database)

    def startup(self,):
        pass






class RegisterUserTabAPI:

    def __init__(self, ui:RegisterUserTabUI ,database: usersDB):
        self.ui = ui
        self.database = database

        self.ui.register_button_connector(self.register)
    
    def register(self,):
        user_inputs = self.ui.get_register_fields()

        if len(user_inputs['username']) <3:
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
       