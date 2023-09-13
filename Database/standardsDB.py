import json
import pickle




class standardsDB:
    TABLE_NAME = 'grading_standards'
    TABLE_COLS = [ {'col_name': 'name',    'type':'VARCHAR(255)', 'len':100},
                   {'col_name': 'ranges',  'type':'VARCHAR(255)', 'len':500},
                   #{'col_name': 'is_default',       'type':'BOOL',},

                ]
    
    PRIMERY_KEY_COL_NAME = 'name'
    


    def __init__(self,db_manager):
        self.db_manager = db_manager
        self.__create_table__()
        self.standardsHistoryTemp = standardsHistoryTemp()
        

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
            record = record[0]
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










class standardsHistoryTemp:
    PATH = 'standards_history.temp'
    

    def __init__(self):
        self.history = []


    def save_history(self):
        dbfile = open(self.PATH, 'ab')
        pickle.dump(self.history, dbfile)


    def load_history(self):
        dbfile = open(self.PATH, 'rb')
        self.history = pickle.load( dbfile)
        

    def append(self, old_standard, new_standard):
        self.history.append( {'old': old_standard,
                              'new': new_standard,
                              #'id' : 0,
                              }
                            )
        
        self.save_history()

    def get_history(self,):
        return self.history


