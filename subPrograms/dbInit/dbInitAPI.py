
from subPrograms.dbInit.dbInitUI import dbInitUI
from backend.Utils import masterPassword
from Constants import CONSTANTS
from Database.mainDatabase import mainDatabase
from Database.metaDatabase import metaDatabase
class dbInitAPI:

    def __init__(self,) -> None:
        self.ui = dbInitUI()
        self.ui.next_button_connector(self.next)
        self.password_confirm = False


    
    def next(self,):
        #for more security
        page_idx = self.ui.get_page()
        if page_idx!=0 and self.password_confirm == False:
            self.ui.set_page(0)

        if page_idx == 0:
            self.check_master_password()
        
        elif page_idx == 1:
            self.check_connection()

        elif page_idx == 2:
            self.ui.close()

    
    def check_master_password(self,):
        password = self.ui.get_maser_password()
        if password == '':
            self.ui.write_error('please input your master password')
        if password != masterPassword.get_master_password():
            self.ui.write_error('master password is incorect')
        
        else:
            self.ui.go_next_page()
            self.ui.set_maser_password('')
            self.password_confirm = True

    
    def check_connection(self,):
        meta_db = self.ui.get_db_meta()
        # for value in meta_db.values():
        #     if value == '':
        #         self.ui.write_error('Please fill all fields')
        #         return
            
        metaDatabase.save(meta_db)
        db = mainDatabase()
        status = db.connect()

        if not status:
            self.ui.write_error('Connection Failed. please sure the connection exist in workBench')
        else:
            self.ui.go_next_page()


