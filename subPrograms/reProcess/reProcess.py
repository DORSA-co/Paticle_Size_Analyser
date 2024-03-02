import sys
import os
sys.path.append(os.getcwd())

import cv2

from Database.mainDatabase import mainDatabase
from Database.reportsDB import reportFileHandler, reportsDB
from backend.Processing import particlesDetector
from Constants import CONSTANTS
from backend.Processing.Report import Report


class reProcessApp:

    def __init__(self, thresh=40) -> None:
        
        self.db = mainDatabase()
        db_status = self.db.connect()
        if not db_status:
            print('database connection error')
            return
        
        self.db.build()
        self.db = self.db.reports_db
        self.all_samples = self.db.load_all()

        self.detector = particlesDetector.particlesDetector(thresh, 
                                                            CONSTANTS.Calibration.PX2MM, 
                                                            5)
        self.thresh = thresh


    def load_report(self, name:str):
        sample_record = list(filter( lambda x:x['name']==name, self.all_samples))[0]
        self.report_filehandler = reportFileHandler(sample_record)
        self.report = self.report_filehandler.load_report()

    def gen_new_report(self):
        name = self.report.name + f'_gen{self.thresh}'
        new_report = Report( name,
                              self.report.standard,
                              self.report.username,
                              self.report.main_path,
                              settings=self.report.settings,
                              description=self.report.description ,
                              grading_parm = self.report.grading_parm
                              )
        return new_report
    
    def reprocess(self):
        new_report = self.gen_new_report()
        imgs_dir = self.report_filehandler.get_image_foler_dir()
        for fname in  os.listdir(imgs_dir):
            path = os.path.join(imgs_dir, fname)
            img = cv2.imread(path, 0)

            self.detector.detect(img, new_report)
        
        
        db_data = new_report.get_database_record()
        report_saver = reportFileHandler(db_data)
        report_saver.save_report(new_report)
        self.db.save(db_data)
        return new_report



if __name__=="__main__":

    rp = reProcessApp(thresh=80)
    rp.load_report('20240228_1520_admin')

    new_report = rp.reprocess()
    print(new_report.Grading.get_hist())
    print(new_report.get_ranges_statistics())
    print(rp.report)