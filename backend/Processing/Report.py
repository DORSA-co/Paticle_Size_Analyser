from backend.Processing.particlesBuffer import particlesBuffer
from backend.Processing.Grading import Grading
from backend.Processing.cumGrading import cumGrading
from backend.Processing import gradingUtils
import numpy as np
from datetime import datetime
import Constants.CONSTANTS as CONSTANTS
import time





class Report:
    """store all information of a sample
    """
    def __init__(self, name = '', standard = None, username = '', main_path ='', settings={}, description='') -> None:
        
        
        self.name = name
        self.standard = standard
        self.username = username
        self.main_path = main_path
        self.date_time = datetime.now()
        self.date = self.date_time.date()
        self.time = self.date_time.time()
        self.Buffer = particlesBuffer()
        self.sieved_particles = []
        self.settings = settings
        self.description = description
        self.name_id = self.generate_uniq_id()

        if self.standard is not None:
            self.ranges_string = reportUtils.ranges2str(self.standard['ranges'])
        
        if standard is not None:
            self.Grading = Grading(self.standard['ranges'])
            self.cumGrading = cumGrading(self.get_full_range())
        else:
            assert True, "not developed yet"

    def generate_uniq_id(self,):
        date_time_str = self.date_time.strftime('%Y-%m-%d_%H-%M-%S_%f')
        return self.name + '_' + self.username + '_' + date_time_str

    def set_operator_username(self, username):
        self.username = username


    def append(self, buffer:particlesBuffer):
        """append a buffer of particles into this sample

        Args:
            buffer (particlesBuffer): _description_
        """
        #append new particle for histogram calculation 
        self.Grading.append(buffer)
        self.cumGrading.append(buffer)
        self.Buffer.extend(buffer)
   


    def clear(self,):
        self.Buffer = particlesBuffer()



    def get_global_statistics(self):
        info = {}
        info['avrage'] = np.round( self.Buffer.get_feature('max_radius').mean(), CONSTANTS.DECIMAL_ROUND )
        info['std'] = np.round( self.Buffer.get_feature('max_radius').std(), CONSTANTS.DECIMAL_ROUND )
        return info
    

    def render(self, ):
        radiuses = self.Buffer.get_feature('max_radius')
        self.sieved_particles = gradingUtils.sift(radiuses, self.standard['ranges'])


    def get_ranges_statistics(self,):
        res = []
        hist = self.Grading.get_hist()
        for i,range_name in enumerate(self.ranges_string):
            data = {}
            if len(self.sieved_particles[i]) > 0:
                data['range'] = range_name
                data['std'] = np.round( self.sieved_particles[i].std(), CONSTANTS.DECIMAL_ROUND )
                data['avrage'] = np.round( self.sieved_particles[i].mean(), CONSTANTS.DECIMAL_ROUND )
                data['count'] = len( self.sieved_particles[i] )
                data['percent'] = hist[i]
            else:
                data['range'] = range_name
                data['std'] = '-'
                data['avrage'] = '-'
                data['count'] = '-'
                data['percent'] = 0
            res.append(data)

        return res
    

    def get_database_record(self,):
        db_data = {
            'name_id' : self.name_id,
            'name': self.name,
            'path': self.main_path,
            'standard': self.standard['name'],
            'date': self.date_time.date(),
            'time': self.date_time.time(),
            'username': self.username,
            'grading_result': self.Grading.get_hist(),
            'max_radiuses': self.Buffer.get_feature('max_radius')
        }

        return db_data


    def get_date_str(self,):
        return self.date_time.strftime("%Y/%m/%d")
    

    def change_standard(self, standard:dict, ):
        #t = time.time()
        if standard['ranges'] != self.standard['ranges'] :
            self.standard = standard
            self.Grading = Grading(self.standard['ranges'])
            self.cumGrading = cumGrading(self.get_full_range())
            self.Grading.append( self.Buffer )
            self.cumGrading.append(self.Buffer)
            self.ranges_string = reportUtils.ranges2str(self.standard['ranges'])

        
        self.standard = standard.copy()

    
    def get_standard_ranges(self,):
        return self.standard['ranges']


    def get_standard_name(self,):
        return self.standard['name']
    
    def get_full_range(self,):
        ranges = np.array(self.standard['ranges'])
        return ranges.min(), ranges.max()
    

    def get_gaussian_data(self,step=1):
        radiuses = self.Buffer.get_feature('max_radius')
        volumes = self.Buffer.get_feature('avg_volume')
        #return np.vstack((radiuses, volumes)).T
        volumes_percent = volumes
        r_min, r_max = self.get_full_range()
        bins = np.arange(r_min, r_max, step)

        ys, _ = np.histogram(radiuses, bins, weights=volumes_percent)
        ys = ys / np.sum(ys) * 100
        
        center_xs = []
        for i in range(len(bins)-1):
            center = ( bins[i] + bins[i+1]  ) / 2
            center_xs.append( center  )

        return center_xs, ys
    
    def get_particles_count(self,):
        return len(self.Buffer.particels)
    
    def get_accumulative_grading(self, ):
        # radiuses = self.Buffer.get_feature('max_radius')
        # volumes = self.Buffer.get_feature('avg_volume')

        # data = np.vstack((radiuses, volumes)).T
        # data = data.tolist()

        # data.sort(key = lambda x:x[0])
        # data = np.array(data)
        # radiuses, volumes = data[:,0], data[:,1]

        # cum_volumes = np.cumsum(volumes)
        # cum_volumes = cum_volumes / cum_volumes[-1] * 100
        
        # return radiuses, cum_volumes
        
        pass


    
    

        














class reportUtils:

    @staticmethod
    def ranges2str(ranges):
        res = []
        for _range in ranges:
            range_str = f"{_range[0]}mm - {_range[1]}mm"
            res.append(range_str)
        return res
