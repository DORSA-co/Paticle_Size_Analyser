import os

from Database.databaseManager import databaseManager
from backend.Utils.StorageUtils import objectSaver

class parentSettingDB:
    TABLE_NAME = ""
    TABLE_COLS = []
    TABLE_DEFAULT_DATAS = []
    PRIMERY_KEY_COL_NAME = 'id'

    def __init__(self,db_manager):
        self.db_manager = db_manager

    
    def __create_table__(self,):
        if not self.db_manager.table_exits(self.TABLE_NAME):
            self.db_manager.create_table(self.TABLE_NAME)
            
            for col in self.TABLE_COLS:
                self.db_manager.add_column( self.TABLE_NAME, **col)
            
            self.restor_default()

    def restor_default(self):
        for default_data in self.TABLE_DEFAULT_DATAS:
            self.save(default_data)
        
    def save(self,data:dict):
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(self.TABLE_NAME,data, self.PRIMERY_KEY_COL_NAME, data[self.PRIMERY_KEY_COL_NAME])
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
        #Re Implement this method


    def is_exist(self, id):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(founded_records)>0:
            return True
        return False


class settingDB:
    
    def __init__(self, db_manager:databaseManager) -> None:
        self.db_manager = db_manager
        self.camera_db = settingCameraDB(self.db_manager)
        self.algorithm_db = settingAlgorithmDB(self.db_manager)
        self.storage_db = settingStorageDB(self.db_manager)
        self.sample_db = settingSampleDB(self.db_manager)
        self.export_db = settingExportDB(self.db_manager)
        self.plc_db = settingPLCDB(self.db_manager)
        self.plc_nodes_db = settingPLCNodesDB(self.db_manager)
        self.config_db = settingConfigDB()

        


class settingCameraDB(parentSettingDB):
    TABLE_NAME = 'camera_setting'
    #TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ {'col_name': 'serial_number',    'type':'VARCHAR(255)', 'len':20},
                   {'col_name': 'gain',             'type':'INT', },
                   {'col_name': 'exposure',         'type':'INT', },
                   {'col_name': 'width',            'type':'INT', },
                   {'col_name': 'height',           'type':'INT', },
                   {'col_name': 'fps',              'type':'INT', },
                   {'col_name': 'port',             'type':'VARCHAR(255)', 'len':20},
                   {'col_name': 'synchronize',      'type':'VARCHAR(255)', 'len':20},
                   {'col_name': 'application',      'type':'VARCHAR(255)', 'len':20},
                ]
    
    TABLE_DEFAULT_DATAS= [ {
                            #'serial_number': '0815-0000',
                            'serial_number': '',
                            'gain': 0,           
                            'exposure': 45,       
                            'width':  2440,          
                            'height': 2048,         
                            'fps': 19,
                            'port': 'COM5',  
                            'synchronize': 'hardware',     
                            'application': 'standard',   
                        }   
                    ]
    
    PRIMERY_KEY_COL_NAME = 'application'

    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()


    def save(self, data):
        super().save(data)
    

    def load(self, camera_application):

        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, camera_application)
        if len(record)>0:
            return record[0]
        return {}
    
    def get_camera_devices(self,) -> dict:
        records =  self.db_manager.get_all_content(self.TABLE_NAME)
        res = []
        for record in records:
            res.append(
                {'application': record['application'],
                  'serial_number': record['serial_number'] }
            )


        return res






class settingSampleDB(parentSettingDB):
    TABLE_NAME = 'sample_setting'

    TABLE_COLS = [ {'col_name': 'autoname_enable',      'type':'INT', },
                   {'col_name': 'autoname_struct',      'type':'VARCHAR(255)', 'len':300},
                   {'col_name': 'default_standard',     'type':'VARCHAR(255)', 'len':300},
                   {'col_name': 'default_grading_parm','type':'VARCHAR(255)', 'len':300},
                   {'col_name': 'application',          'type':'VARCHAR(255)', 'len':20},
                   {'col_name': 'text1',                'type':'VARCHAR(255)', 'len':300},
                   {'col_name': 'save_image',           'type':'INT', },
                ]
    
    TABLE_DEFAULT_DATAS= [{  
                            'autoname_enable': 0,
                            'autoname_struct': '%YEAR%%MONTH%%DAY%_%HOUR%%MINUTE%_%USERNAME%',
                            'default_standard': '',
                            'default_grading_parm': 'min_radius',
                            'text1': '',
                            'save_image': 1,
                            }
                        ]
    
            
    PRIMERY_KEY_COL_NAME = 'id'
    BOOL_COLS = [ 'save_image', 'autoname_enable']


    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()
        
        
    


    def save(self, data):
        data['id'] = 1
        for col in self.BOOL_COLS:
            data[col] = int(data[col])
        super().save(data)

    

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
    
    

    



    



class settingAlgorithmDB(parentSettingDB):
    TABLE_NAME = 'algorithm_setting'
    TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ 
                   {'col_name': 'threshold',    'type':'INT'},
                   {'col_name': 'border',       'type':'INT', },
                ]
    
    TABLE_DEFAULT_DATAS = [
                            {
                            'threshold' : 80,
                            'border': 10
                        }
                    ]
    
    PRIMERY_KEY_COL_NAME = 'id'


    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()
        


    def save(self, data):
        data['id'] = 1
        super().save(data)

    

    def load(self):
        id = 1
        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            return record
        return {}
    





class settingStorageDB(parentSettingDB):
    TABLE_NAME = 'storage_setting'
    TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ {'col_name': 'path',          'type':'VARCHAR(255)', 'len':1000},
                   {'col_name': 'auto_clean',    'type':'INT', },
                   {'col_name': 'life_time',     'type':'INT', },
                   
                ]
    
    TABLE_DEFAULT_DATAS = [ {
                                'path': '',
                                'auto_clean' : 1,
                                'life_time': 90
                        }
                    ]
    
    PRIMERY_KEY_COL_NAME = 'id'
    BOOL_COLS = ['auto_clean', ]


    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()
        


    def save(self, data):
        data['id'] = 1
        #conver boolean to int for save in database
        for col in self.BOOL_COLS:
            data[col] = int(data[col])
        data['path'] = data['path'].replace('\\','/')
        super().save(data)

    

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
    







class settingExportDB(parentSettingDB):
    TABLE_NAME = 'export_setting'

    TABLE_COLS = [ 
                   {'col_name': 'report_excel',      'type':'TEXT', 'len':300},
                   {'col_name': 'compare_excel',     'type':'TEXT', 'len':300},
                ]
    
    TABLE_DEFAULT_DATAS= [{  
                            'report_excel': 'files//export_formats//report_format.xlsx',
                            'compare_excel': 'files//export_formats//compare_format.xlsx',
                            }
                        ]
    
            
    PRIMERY_KEY_COL_NAME = 'id'


    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()
        



    def save(self, data):
        data['id'] = 1
        super().save(data)

    

    def load(self):
        id = 1
        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            return record
        return {}
    




class settingPLCDB(parentSettingDB):
    TABLE_NAME = 'plc_setting'
    TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ 
                   {'col_name': 'ip',                 'type':'VARCHAR(255)', 'len':200},
                   {'col_name':'check_connection_ns', 'type':'VARCHAR(255)', 'len':200},
                   {'col_name':'check_connection_i',  'type':'VARCHAR(255)', 'len':200},

                ]
    
    TABLE_DEFAULT_DATAS = [
                            {
                            'ip' : "0.0.0.0",
                            'check_connection_ns': 2,
                            'check_connection_i' : 1,

                        }
                    ]
    
    PRIMERY_KEY_COL_NAME = 'id'


    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()
        

    def save(self, data):
        data['id'] = 1
        super().save(data)

    

    def load(self):
        id = 1
        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            return record
        return {}
    


class settingPLCNodesDB(parentSettingDB):
    TABLE_NAME = 'plc_nodes_setting'
    TABLE_NAME_DEFAULT = TABLE_NAME + '_default'
    TABLE_COLS = [ 
                   {'col_name': 'name',    'type':'VARCHAR(255)', 'len':200},
                   {'col_name': 'type',    'type':'VARCHAR(255)', 'len':200},
                   {'col_name': 'ns',    'type':'VARCHAR(255)', 'len':200},
                   {'col_name': 'i',    'type':'VARCHAR(255)', 'len':200},



                ]
    
    TABLE_DEFAULT_DATAS = [
                    ]
    
    PRIMERY_KEY_COL_NAME = 'name'


    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()


    def save(self, data:dict):
        super().save(data)

    def save_all(self, datas:list[dict]):
        self.db_manager.clear_table(self.TABLE_NAME)
        for d in datas:
            self.save(d)

    

    def load(self, name):
        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, name)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            return record
        return {}
    
    def load_all(self,):
        records =  self.db_manager.get_all_content(self.TABLE_NAME)
        return  records




class settingConfigDB:
    path = 'config'
    def __init__(self) -> None:
        pass

    def save_config(self,config: dict):
        """saves report object

        Args:
            report (Report): report object
        """
        objectSaver.save(config, self.path)


    def load_config(self,) -> dict:
        """load report Object

        Returns:
            Report: loaded report object
        """
        
        if os.path.exists(self.path):
            return objectSaver.load(self.path)
        return None