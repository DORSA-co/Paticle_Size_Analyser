import pickle
import os
import shutil


class objectSaver:


    @staticmethod
    def save(obj:object, path:str):
        """save a python object in given path

        Args:
            obj (object): python object 
            path (str): path
        """
        if os.path.exists(path):
            os.remove(path)
        dbfile = open(path, 'ab')
        pickle.dump(obj, dbfile)


    @staticmethod
    def load( path:str, defalut=None) -> object:
        """load a python object

        Args:
            path (str): path of saved object

        Returns:
            object: return loaded python object
        """
        if os.path.exists(path):
            dbfile = open(path, 'rb')
            return pickle.load( dbfile)

        return defalut
    



class storageManager:

    @staticmethod
    def build_dir( path:str):
        """make a path dir if not exist
        Args:
            path (str): path
        """

        base_path = os.path.dirname(path)
        if (not os.path.isdir(base_path)) and base_path != '':
            storageManager.build_dir(base_path)

        if (not os.path.isdir(path)) and path !='' :
            os.mkdir(path)

    
    def remove(path:str):
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            
            if os.path.isfile(path):
                os.remove(path)