class settingDB:
    
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
        self.camera_db = settingCamera(self.db_manager)
        


class settingCamera:
    TABLE_NAME = 'camera_setting'
    TABLE_COLS = [ {'col_name': 'id',           'type':'VARCHAR', 'len':20},
                   {'col_name': 'gain',         'type':'INT', },
                   {'col_name': 'exposure',     'type':'INT', },
                   {'col_name': 'width',        'type':'INT', },
                   {'col_name': 'height',       'type':'INT', },
                   {'col_name': 'fps',          'type':'INT', },
                   {'col_name': 'is_default',   'type':'BOOL', },

                ]
    
    DEFAULTS = {
        'gain':'Null',
        'gain':0,
        'exposure':0,
        'width':0,
        'height':0,
        'fps':0,
    }


    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        self.db_manager.create_table(self.TABLE_NAME)
        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME , **col)
        
        
    
    def __set_default__(self):
        for is_default in [0,1]:
            self.DEFAULTS['is_default'] = is_default
            self.db_manager.add_record(self.TABLE_NAME, self.DEFAULTS)
        
        

    def save(self, datas):
        for data,value in datas.items():
            self.db_manager.update_record(self.TABLE_NAME,data,value,'is_default', 0)


    
