from backend.UserManager.userLoginRegister import passwordManager



class calibDB:
    TABLE_NAME = 'calib'
    TABLE_COLS = [ {'col_name': 'date',      'type':'VARCHAR(255)', 'len':50},
                   {'col_name': 'px2mm',     'type':'FLOAT', },

                ]
    
    #DEFAULT_USERS = [{'date':'', 'px2mm':0]
    
    PRIMERY_KEY_COL_NAME = 'id'
    
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
        self.__create_table__()


    def __create_table__(self,) -> None:
        if not self.db_manager.table_exits(self.TABLE_NAME):
            self.db_manager.create_table(self.TABLE_NAME)
            
            for col in self.TABLE_COLS:
                self.db_manager.add_column( self.TABLE_NAME, **col)
        



    def is_exist(self,) -> bool:
        """returns True a username if exist

        Args:
            username (str): 

        Returns:
            bool : return True if exist
        """
        _id = 1
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, _id)
        if len(founded_records)>0:
            return True
        return False

    def save(self, data: dict):
        _id = 1
        data[self.PRIMERY_KEY_COL_NAME] = _id
        if not self.is_exist():
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
        else:
            self.db_manager.update_record_dict(self.TABLE_NAME, data, id_name=self.PRIMERY_KEY_COL_NAME, id_value = data[self.PRIMERY_KEY_COL_NAME])

        
    def load(self, ) -> list[dict]:
        _id = 1
        return self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, _id)[0]
    
    def get_px2mm(self,):
        if self.is_exist():
            return self.load()['px2mm']
        return 0

