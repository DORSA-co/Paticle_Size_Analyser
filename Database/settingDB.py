
class settingDB:
    
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
        self.camera_db = settingCameraDB(self.db_manager)
        self.algorithm_db = settingAlgorithmDB(self.db_manager)
        self.storage_db = settingStorageDB(self.db_manager)
        self.sample_db = settingSampleDB(self.db_manager)
        


class settingCameraDB:
    TABLE_NAME = 'camera_setting'
    TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ {'col_name': 'serial_number',    'type':'VARCHAR(255)', 'len':20},
                   {'col_name': 'gain',             'type':'INT', },
                   {'col_name': 'exposure',         'type':'INT', },
                   {'col_name': 'width',            'type':'INT', },
                   {'col_name': 'height',           'type':'INT', },
                   {'col_name': 'fps',              'type':'INT', },
                   {'col_name': 'application',      'type':'VARCHAR(255)', 'len':20},
                ]
    
    TABLE_DEFAULT= {
                   'serial_number': '',
                   'gain': 50,           
                   'exposure': 50,       
                   'width':  2000,          
                   'height': 1800,         
                   'fps': 15,            
                   'application': 'standard',   

                }
    PRIMERY_KEY_COL_NAME = 'application'


    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        self.db_manager.create_table(self.TABLE_NAME)
        #self.db_manager.create_table(self.TABLE_NAME_DEFAULT)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)
            #self.db_manager.add_column( self.TABLE_NAME_DEFAULT, **col)
        


    def is_exist(self, application):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, application)
        if len(founded_records)>0:
            return True
        return False



    def save(self, data):
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(self.TABLE_NAME,data, self.PRIMERY_KEY_COL_NAME, data[self.PRIMERY_KEY_COL_NAME])
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
    

    def load(self, camera_number):

        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, camera_number)
        if len(record)>0:
            return record[0]
        return {}
    
    def restor_default(self, camera_number):
        default_data = self.db_manager.search( self.TABLE_NAME_DEFAULT, self.PRIMERY_KEY_COL_NAME, camera_number)[0]
        self.db_manager.update_record_dict(self.TABLE_NAME, default_data, id_name = self.PRIMERY_KEY_COL_NAME, id_value = camera_number)
        return default_data






class settingSampleDB:
    TABLE_NAME = 'sample_setting'

    TABLE_COLS = [ {'col_name': 'autoname_enable',      'type':'INT', },
                   {'col_name': 'autoname_struct',      'type':'VARCHAR(255)', 'len':300},
                   {'col_name': 'default_standard',     'type':'VARCHAR(255)', 'len':300},
                   {'col_name': 'text1',     'type':'VARCHAR(255)', 'len':300},
                   {'col_name': 'save_image',    'type':'INT', },
                ]
    
    TABLE_DEFAULT= [ {'autoname_enable': 0},
                     {'autoname_struct': '%Y%M%D'},
                     {'default_standard': ''},
                     {'text1': ''},
                     {'save_image': 1},
                ]
    
    PRIMERY_KEY_COL_NAME = 'id'
    BOOL_COLS = [ 'save_image', 'autoname_enable']

    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        self.db_manager.create_table(self.TABLE_NAME)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)
        
        
    def is_exist(self, id):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(founded_records)>0:
            return True
        return False


    def save(self, data):
        data['id'] = 1
        for col in self.BOOL_COLS:
            data[col] = int(data[col])
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(self.TABLE_NAME,data, self.PRIMERY_KEY_COL_NAME, data[self.PRIMERY_KEY_COL_NAME])
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
    

    def load(self):
        id = 1
        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            for col in self.BOOL_COLS:
                record[col] = bool(record[col])
            return record
        return {}
    
    

    



    



class settingAlgorithmDB:
    TABLE_NAME = 'algorithm_setting'
    TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ 
                   {'col_name': 'threshold',    'type':'INT'},
                   {'col_name': 'border',       'type':'INT', },
                ]
    
    TABLE_DEFAULTS = {
                        'threshold' : 20,
                        'border': 10
                    }
    PRIMERY_KEY_COL_NAME = 'id'


    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        self.db_manager.create_table(self.TABLE_NAME)
        self.db_manager.create_table(self.TABLE_NAME_DEFAULT)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)
            self.db_manager.add_column( self.TABLE_NAME_DEFAULT, **col)
        
        
    def is_exist(self, id):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(founded_records)>0:
            return True
        return False


    def save(self, data):
        data['id'] = 1
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(self.TABLE_NAME,data, self.PRIMERY_KEY_COL_NAME, data[self.PRIMERY_KEY_COL_NAME])
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
    

    def load(self):
        id = 1
        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            return record
        return {}
    
    def restor_default(self,):
        id = 1
        default_data = self.db_manager.search( self.TABLE_NAME_DEFAULT, self.PRIMERY_KEY_COL_NAME, id)[0]
        self.db_manager.update_record_dict(self.TABLE_NAME, default_data, id_name = self.PRIMERY_KEY_COL_NAME, id_value = id)
        return default_data

    






class settingStorageDB:
    TABLE_NAME = 'storage_setting'
    TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ {'col_name': 'path',          'type':'VARCHAR(255)', 'len':1000},
                   {'col_name': 'auto_clean',    'type':'INT', },
                   {'col_name': 'life_time',     'type':'INT', },
                   
                ]
    
    TABLE_DEFAULTS = {
                        'path': '',
                        'auto_clean' : 1,
                        'life_time': 90
                    }
    
    PRIMERY_KEY_COL_NAME = 'id'
    BOOL_COLS = ['auto_clean', ]


    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        #print(self.db_manager.table_exits(self.TABLE_NAME))
        self.db_manager.create_table(self.TABLE_NAME)
        self.db_manager.create_table(self.TABLE_NAME_DEFAULT)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)
            self.db_manager.add_column( self.TABLE_NAME_DEFAULT, **col)
        
        
    def is_exist(self, id):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(founded_records)>0:
            return True
        return False


    def save(self, data):
        data['id'] = 1
        #conver boolean to int for save in database
        for col in self.BOOL_COLS:
            data[col] = int(data[col])
        data['path'] = data['path'].replace('\\','/')
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(self.TABLE_NAME,data, self.PRIMERY_KEY_COL_NAME, data[self.PRIMERY_KEY_COL_NAME])
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
    

    def load(self):
        id = 1
        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            #conver int 0 or 1 into boolean
            for col in self.BOOL_COLS:
                record[col] = bool(record[col])
            return record
        return {}
    
    def restor_default(self,):
        id = 1
        default_data = self.db_manager.search( self.TABLE_NAME_DEFAULT, self.PRIMERY_KEY_COL_NAME, id)[0]
        self.db_manager.update_record_dict(self.TABLE_NAME, default_data, id_name = self.PRIMERY_KEY_COL_NAME, id_value = id)
        return default_data

    


