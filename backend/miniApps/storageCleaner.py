from datetime import datetime

from Database.reportsDB import reportsDB, reportFileHandler

class storageCleaner:

    def __init__(self, settings, reports_db:reportsDB) -> None:
        self.settings = settings
        self.reports_db = reports_db
        self.removed_counter = 0

    def run(self):
        """delete samples that have more lifetime than determinded value in setting, only of auto clean is active
        """
        if self.settings['auto_clean']:
            today = datetime.today().date()
            life_time = self.settings['life_time']
            #load all samples from db
            samples = self.reports_db.load_all()
            #samples[0]['date'] = datetime(2019,1,1).date()

            for sample in samples:
                delta = today - sample['date']
                if delta.days > life_time:
                    self.remove_sample(sample)
                    self.removed_counter+=1
                else:
                    break

    def remove_sample(self, sample:dict):
        date_time = datetime.combine(sample['date'], sample['time'])
        rfh = reportFileHandler(main_path=sample['path'], sample_name=sample['name'], date_time=date_time)
        rfh.remove()
        self.reports_db.remove(sample)