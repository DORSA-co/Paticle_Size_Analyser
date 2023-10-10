if __name__ == '__main__':
    from databaseManager import databaseManager
    from settingDB import settingDB
else:
    from Database.databaseManager import databaseManager
    from Database.settingDB import settingDB
    from Database.usersDB import usersDB
    from Database.standardsDB import standardsDB
    from Database.reportsDB import reportsDB
    from Database.metaDatabase import metaDatabase

class mainDatabase:
    # username = 'root'
    # password = 'dorsa-co'
    # password = ''
    # host = 'localhost'
    DATABASE_NAME = 'dorsa_psa'

    def __init__(self,):
        self.dbManager = None
        

    def build(self,):
        self.setting_db = settingDB(self.dbManager)
        self.users_db = usersDB(self.dbManager)
        self.standards_db = standardsDB(self.dbManager)
        self.reports_db = reportsDB(self.dbManager)
    
    def connect(self,):
        mtb = metaDatabase()
        if mtb.is_exist():
            meta = mtb.load()
            self.dbManager = databaseManager(meta['database_username'],
                                             meta['database_password'],
                                             meta['database_host'], 
                                             self.DATABASE_NAME,
                                             log_level=1)
            return self.dbManager.check_connection()

      
        return False





# if __name__ == "__main__":
#     mdb = mainDatabase()