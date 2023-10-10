import json
import os
from Constants import CONSTANTS
from backend.Utils.cryptoFile import cryptoFile


class metaDatabase:
    DB_META_PATH = CONSTANTS.databaseConstant.META_PATH
    KEY = CONSTANTS.databaseConstant.KEY


    @staticmethod
    def is_exist() -> bool:
        return os.path.exists(metaDatabase.DB_META_PATH)
    
    @staticmethod
    def load():
        cpf = cryptoFile(metaDatabase.KEY)
        file = cpf.decrypt_file(metaDatabase.DB_META_PATH)
        return json.loads(file)

    @staticmethod
    def save( data:dict):
        # if os.path.exists(path):
        #     os.remove(path)
        #     while os.path.exists(path): pass
        json_object = json.dumps(data, indent=4)
        with open(metaDatabase.DB_META_PATH, "w") as outfile:
            outfile.write(json_object)

        cpf = cryptoFile(metaDatabase.KEY)
        cpf.encrypt_file(metaDatabase.DB_META_PATH)
    

    



