import json

class settingDB:
    
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
        self.camera_db = settingCameraDB(self.db_manager)
        self.grading_db = settingGradingDB(self.db_manager)
        


class settingCameraDB:
    TABLE_NAME = 'camera_setting'
    TABLE_NAME_DEFAULT = 'camera_setting' + '_default'
    TABLE_COLS = [ {'col_name': 'serial_number',    'type':'VARCHAR(255)', 'len':20},
                   {'col_name': 'gain',             'type':'INT', },
                   {'col_name': 'exposure',         'type':'INT', },
                   {'col_name': 'width',            'type':'INT', },
                   {'col_name': 'height',           'type':'INT', },
                   {'col_name': 'fps',              'type':'INT', },
                   {'col_name': 'application',      'type':'VARCHAR(255)', 'len':20},
                   #{'col_name': 'is_default',       'type':'BOOL',},

                ]
    PRIMERY_KEY_COL_NAME = 'application'


    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        self.db_manager.create_table(self.TABLE_NAME)
        self.db_manager.create_table(self.TABLE_NAME_DEFAULT)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)
            self.db_manager.add_column( self.TABLE_NAME_DEFAULT, **col)
        
        
    
    # def __set_default__(self):
    #     for is_default in [0,1]:
    #         self.DEFAULTS['is_default'] = is_default
    #         self.db_manager.add_record(self.TABLE_NAME, self.DEFAULTS)

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

    







class settingGradingDB:
    TABLE_NAME = 'grading_setting'
    TABLE_COLS = [ {'col_name': 'name',    'type':'VARCHAR(255)', 'len':100},
                   {'col_name': 'ranges',  'type':'VARCHAR(255)', 'len':500},
                   #{'col_name': 'is_default',       'type':'BOOL',},

                ]
    
    PRIMERY_KEY_COL_NAME = 'name'
    


    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        self.db_manager.create_table(self.TABLE_NAME)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)
    

    def is_exist(self, name):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, name)
        if len(founded_records)>0:
            return True
        return False

    def save(self, data):
        #convert list to str
        
        data = data.copy()
        data['ranges'] = json.dumps(data['ranges'])

        if not self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
        else:
            self.db_manager.update_record_dict(self.TABLE_NAME, data, id_name=self.PRIMERY_KEY_COL_NAME, id_value = data[self.PRIMERY_KEY_COL_NAME])
    

    def load(self, name):
        record = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, name)
        if len(record):
            #convert str to list
            record['ranges'] = json.loads(record['ranges'])
        return record 

    

    def load_all(self,):
        records = self.db_manager.get_all_content( self.TABLE_NAME)

        #convert str into list
        for i in range(len(records)):
            records[i]['ranges'] = json.loads(records[i]['ranges'])
        
        return records
    

    def remove(self, name):
        self.db_manager.remove_record(self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, name)