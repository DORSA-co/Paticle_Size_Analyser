class settingDB:
    pass


class settingCamera:
    TABLE_NAME = 'camera_setting'
    TABLE_COLS = ['id','gain', 'exposure', 'width', 'height', 'fps']
    def __init__(self,db_cntrl):
        self.db_cntrl = db_cntrl
        self.__create_table__

    def __create_table__(self,):
        self.db_cntrl.creat_table(self.TABEL_NAME)
    
