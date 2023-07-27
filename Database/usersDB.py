class usersDB:
    TABLE_NAME = 'users'
    TABLE_COLS = [ {'col_name': 'username',    'type':'VARCHAR(255)', 'len':50},
                   {'col_name': 'password',    'type':'VARCHAR(255)', 'len':100},
                   {'col_name': 'role',        'type':'VARCHAR(255)', 'len':50},
                ]
    
    PRIMERY_KEY_COL_NAME = 'username'
    
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
        self.__create_table__()


    def __create_table__(self,) -> None:
        self.db_manager.create_table(self.TABLE_NAME)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)
    


    def is_exist(self, username:str) -> bool:
        """returns True a username if exist

        Args:
            username (str): 

        Returns:
            bool : return True if exist
        """
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, username)
        if len(founded_records)>0:
            return True
        return False

    def save(self, data: dict):
        if not self.is_exist( data[self.PRIMERY_KEY_COL_NAME] ):
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
        else:
            self.db_manager.update_record_dict(self.TABLE_NAME, data, id_name=self.PRIMERY_KEY_COL_NAME, id_value = data[self.PRIMERY_KEY_COL_NAME])

        
    def load(self, username:str) -> list[dict]:
        return self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, username)[0]
    

    def load_all(self,) -> list[dict]:
        return self.db_manager.get_all_content( self.TABLE_NAME)
    
    def remove(self, username):
        self.db_manager.remove_record(self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, username)

