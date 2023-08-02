if __name__ == '__main__':
    from databaseManager import databaseManager
    from settingDB import settingDB
else:
    from Database.databaseManager import databaseManager
    from Database.settingDB import settingDB
    from Database.usersDB import usersDB
    from Database.gradingRangesDB import gradingRangesDB

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
        self.users_db = usersDB(self.dbManager)
        self.grading_ranges_db = gradingRangesDB(self.dbManager)
    
    def __connect__(self,):
        self.dbManager = databaseManager(self.username, self.password, self.HOST, self.DATABASE_NAME, log_level=1)
        





# if __name__ == "__main__":
#     mdb = mainDatabase()