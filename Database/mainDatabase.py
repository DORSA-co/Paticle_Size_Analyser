if __name__ == '__main__':
    from databaseManager import databaseManager
    from settingDB import settingDB
else:
    from Database.databaseManager import databaseManager
    from Database.settingDB import settingDB

class mainDatabase:
    username = 'root'
    password = 'dorsa-co'
    password = ''
    HOST = 'localhost'
    DATABASE_NAME = 'dorsa_psa'

    def __init__(self,):
        self.dbManager = None
        self.__connect__()

        self.setting_db = settingDB(self.dbManager)
    
    def __connect__(self,):
        self.dbManager = databaseManager(self.username, self.password, self.HOST, self.DATABASE_NAME)
        





# if __name__ == "__main__":
#     mdb = mainDatabase()