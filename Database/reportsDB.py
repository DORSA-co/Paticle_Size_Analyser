
from Database.databaseManager import databaseManager
from backend.Processing.Report import Report
from backend.Utils.datetimeUtils import datetimeFormat
from datetime import datetime
import numpy as np
import os
import cv2
import pickle
import shutil




class reportsDB:
    TABLE_NAME = 'reports'
    TABLE_COLS = [ {'col_name': 'name',        'type':'VARCHAR(255)', 'len':50},
                   {'col_name': 'standard',    'type':'VARCHAR(255)', 'len':50},
                   {'col_name': 'date',        'type':'VARCHAR(255)', 'len':50},
                   {'col_name': 'time',        'type':'VARCHAR(255)', 'len':50},
                   {'col_name': 'username',    'type':'VARCHAR(255)', 'len':50},
                   {'col_name': 'path',        'type':'VARCHAR(255)', 'len':200},
                   {'col_name': 'grading_result',     'type':'VARCHAR(255)', 'len':200},
                ]

    # DATE_STR_FORMAT = "%Y/%m/%d"
    # TIME_STR_FORMAT = "%H:%M:%S"
    #PRIMERY_KEY_COL_NAME = 'application'


    def __init__(self,db_manager:databaseManager):
        self.db_manager = db_manager
        self.__create_table__()
        

    def __create_table__(self,):
        self.db_manager.create_table(self.TABLE_NAME)

        for col in self.TABLE_COLS:
            self.db_manager.add_column( self.TABLE_NAME, **col)

    def __pre_process_to_save__(self, data):
        data['date'] = datetimeFormat.date_to_str(data['date'])
        data['time'] = datetimeFormat.time_to_str(data['time'])

        #convert list to cvs
        grading_result = data['grading_result']
        grading_result = list(map( lambda x:str(x), grading_result))
        grading_result = ','.join(grading_result)
        data['grading_result'] = grading_result
        return data
    
    def __pre_process_to_load__(self, record):
        record['date'] = datetimeFormat.str_to_date(record['date'] )
        record['time'] = datetimeFormat.str_to_time(record['time'] )

        #convert csv to list
        grading_result = record['grading_result']
        grading_result = grading_result.split(',')
        grading_result = list(map( lambda x:float(x), grading_result))
        
        record['grading_result'] = grading_result
        return record

    def save(self, data):
        
        data = self.__pre_process_to_save__(data)
        self.db_manager.add_record_dict(self.TABLE_NAME, data)
    

    def load_all(self,):
        records =  self.db_manager.get_all_content(self.TABLE_NAME)
        for record in records:
            record = self.__pre_process_to_load__(record)
        return records
    
    def load_by_ids(self, ids):
        res = []
        for id in ids:
            record = self.db_manager.search(self.TABLE_NAME, 'id', id)
            if len(record):
                record = self.__pre_process_to_load__(record)
                res.append(record[0])
        return res
        
    
    def remove(self, data):
        self.db_manager.remove_record(self.TABLE_NAME, 'id', str(data['id']))





    

class reportFileHandler:
    """this class saves report object file and sample images
    """
    REPORT_NAME = 'report'
    IMG_FOLDER = 'images'
    IMG_FILE_FORMAT = '.png'

    def __init__(self, main_path:str, sample_name:str, date_time:datetime) -> None:
        self.main_path = main_path
        self.sample_name = sample_name
        self.date_time = date_time

        self.__build_dir__( self.get_image_foler_dir() )

    def __build_dir__(self, path:str):
        """make a path dir if not exist
        Args:
            path (str): path
        """

        base_path = os.path.dirname(path)
        if (not os.path.isdir(base_path)) and base_path != '':
            self.__build_dir__(base_path)

        if (not os.path.isdir(path)) and path !='' :
            os.mkdir(path)

    def __save_obj__(self, obj:object, path:str):
        """save a python object in given path

        Args:
            obj (object): python object 
            path (str): path
        """
        dbfile = open(path, 'ab')
        pickle.dump(obj, dbfile)


    def __load_obj__(self, path:str) -> object:
        """load a python object

        Args:
            path (str): path of saved object

        Returns:
            object: return loaded python object
        """
        dbfile = open(path, 'rb')
        return pickle.load( dbfile)
    
    

    
    def get_report_folder_path(self,) -> str:
        """Returns main folder path of a report

        Returns:
            str: path
        """
        dt_str = self.date_time.strftime("%Y%m%d_%H%M%S")
        folder_name = '{}_{}'.format(self.sample_name, dt_str)
        return os.path.join(self.main_path, folder_name)    
    

    def get_report_file_path(self,) -> str:
        """returns path of report object file

        Returns:
            str: path
        """
        return os.path.join( self.get_report_folder_path(), self.REPORT_NAME )
    
    
    def get_image_foler_dir(self,)-> str:
        """returns folder's path of a sample's images

        Returns:
            str: path
        """
        return os.path.join(self.main_path, self.get_report_folder_path(), self.IMG_FOLDER )
    
    
    def get_image_path(self, img_id):
        """returns image file's path

        Args:
            img_id (_type_): an img_id for save image. it could be frame index

        Returns:
            str: path
        """
        img_name = '{}{}'.format(img_id, self.IMG_FILE_FORMAT)
        return os.path.join(self.main_path, self.get_report_folder_path(), self.IMG_FOLDER, img_name )



    def save_report(self,report: Report):
        """saves report object

        Args:
            report (Report): report object
        """
        path = self.get_report_file_path()
        self.__save_obj__(report, path)

    def load_report(self,) -> Report:
        """load report Object

        Returns:
            Report: loaded report object
        """
        report_path = self.get_report_file_path()
        if os.path.exists(report_path):
            return self.__load_obj__(report_path)
        return None
    

    def remove(self,) -> Report:
        """load report Object

        Returns:
            Report: loaded report object
        """
        path = self.get_report_folder_path()
        if os.path.exists(path):
            shutil.rmtree(path)
            return True

    def save_image(self, img:np.ndarray ,  img_id:str):
        """saves an image file

        Args:
            img (np.ndarray): numpy image array
            img_id (str): id of image, it is frame idx
        """
        path = self.get_image_path(img_id)
        #cv2.imwrite(path, img)
        cv2.imwrite(path ,img, [int(cv2.IMWRITE_JPEG_QUALITY), 50] )

    def load_image(self, img_id):
        path = self.get_image_path(img_id)
        return cv2.imread(path, 0)
        
        

