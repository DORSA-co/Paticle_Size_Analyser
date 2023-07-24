from Database.databaseConnector import databaseConnector


class mainDatabase:
    

    def __init__(aelf,):
        self.username = 'root'
        self.password = 'dorsa-co'
        self.HOST = 'localhost'
        self.DATABASE_NAME = 'dorsa_psa'
    
    def __connect__(self,):
        self.databaseConnector.connect()
    def __create_database__(self,):
        databaseConnector.create_schema(self.DATABASE_NAME)
