import sys
import os
sys.path.append(os.getcwd())

import numpy as np

from Database import mainDatabase
from Database.reportsDB import reportFileHandler, reportsDB
from backend.Processing.Report import Report
from backend.Processing.Particel import Particle

class updateReports:

    def __init__(self, database:mainDatabase.mainDatabase) -> None:
        self.database = database

    def update(self,):
        samples = self.database.reports_db.load_all()
        for i in range(len(samples)):
            rfh = reportFileHandler(samples[i])
            old_report = rfh.load_report()
            new_report = Report(old_report.name, 
                                old_report.standard,
                                old_report.username,
                                old_report.main_path, 
                                old_report.settings,
                                old_report.description)
            for old_particel in old_report.Buffer.total_buffer.get_particels():
                new_particle = Particle(old_particel.cnt, old_particel.px2mm, old_particel.img_id)
                new_report.append_particle(new_particle)
            
            percent = np.round(i/ len(samples) * 100,2)
            print(f'{percent}%')
            rfh.save_report(new_report)



if __name__ == '__main__':
    db = mainDatabase.mainDatabase()
    db_status = db.connect()
    if db_status:
        db.build()
        ur = updateReports(db)
        ur.update()
    
    else:
        print('DATABASE CONNECTION ERROR')
