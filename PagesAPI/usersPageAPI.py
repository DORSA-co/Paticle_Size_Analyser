from dorsaPylon import Collector

from PagesUI.usersPageUI import usersPageUI, RegisterUserTabUI, AllUserTabUI
from Database.usersDB import usersDB
from backend.UserManager.userLoginRegister import passwordManager

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
        
        if self.database.is_exist(user_inputs['username']):
            self.ui.write_register_error('Username is already exist!')
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



        
       