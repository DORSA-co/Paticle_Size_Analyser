from backend.Processing.particlesBuffer import particlesBuffer, sieveParticlesBuffer
from backend.Processing.Grading import Grading
from backend.Processing.Grading import cumGrading
from backend.Processing import gradingUtils
import numpy as np
from datetime import datetime
import Constants.CONSTANTS as CONSTANTS
import time
from backend.Processing.Particel import Particle





class Report:
    """store all information of a sample
    """
    def __init__(self, 
                 name = '', 
                 standard = None, 
                 username = '', 
                 main_path ='', 
                 settings={}, 
                 description='', 
                 grading_parm='') -> None:
        
        
        self.name = name
        self.standard = standard
        self.username = username
        self.main_path = main_path
        self.date_time = datetime.now()
        self.date = self.date_time.date()
        self.time = self.date_time.time()
        self.settings = settings
        self.description = description
        self.name_id = self.generate_uniq_id()
        self.grading_parm = grading_parm

    
        self.ranges_string = reportUtils.ranges2str(self.standard['ranges'])
        self.Buffer = sieveParticlesBuffer(self.standard['ranges'])
        self.Grading = Grading(self.standard['ranges'])
        self.cumGrading = cumGrading(self.get_full_range())
        


    def generate_uniq_id(self,):
        date_time_str = self.date_time.strftime('%Y-%m-%d_%H-%M-%S_%f')
        return self.name + '_' + self.username + '_' + date_time_str

    def set_operator_username(self, username):
        self.username = username


    # def append(self, buffer:particlesBuffer):
    #     """append a buffer of particles into this sample

    #     Args:
    #         buffer (particlesBuffer): _description_
    #     """
    #     #append new particle for histogram calculation ad sieve particles
    #     sieve_idxs = self.Grading.append(buffer)
    #     self.cumGrading.append(buffer)
    #     self.Buffer.extend(buffer)
    
    def append_particle(self, particle:Particle):        
        sieve_idx = self.Grading.append_particle(particle, self.grading_parm)
        _ = self.cumGrading.append_particle(particle, self.grading_parm)
        self.Buffer.append_particle(particle, sieve_idx)

   
    def clear(self,):
        self.Buffer = sieveParticlesBuffer()



    def get_global_statistics(self):
        info = {}
        if self.get_particles_count() != 0:
            xs = self.Buffer.total_buffer.get_feature(self.grading_parm)
            info['avrage'] = np.round( xs.mean(), CONSTANTS.DECIMAL_ROUND )
            info['std'] = np.round( xs.std(), CONSTANTS.DECIMAL_ROUND )

            xs, ys = self.get_gaussian_data(step=0.5)
            info['mode'] = xs[np.argmax(ys)]


        else:
            info['avrage'] = 0
            info['std'] = 0
            info['mode'] = 0

        return info    

    def get_ranges_statistics(self,) -> list[dict]:
        res = []
        hist = self.Grading.get_hist()
        for i,range_name in enumerate(self.ranges_string):
            data = {}
            parms = self.Buffer.get_feature(self.grading_parm, sive_idx=i)
            circularites = self.Buffer.get_feature('circularity', sive_idx=i)
            count = len(parms)
            if count > 0:
                

                data['range'] = range_name
                data['std'] = np.round( parms.std(), CONSTANTS.DECIMAL_ROUND )
                data['avrage'] = np.round( parms.mean(), CONSTANTS.DECIMAL_ROUND )
                data['count'] = count
                data['percent'] = hist[i]
                data['circularity'] = np.round( circularites.mean(), CONSTANTS.DECIMAL_ROUND )
            else:
                data['range'] = range_name
                data['std'] = 0
                data['avrage'] = 0
                data['count'] = 0
                data['percent'] = 0
                data['circularity'] = 0
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
            'max_radiuses': self.Buffer.total_buffer.get_feature(self.grading_parm)
        }

        return db_data


    def get_date_str(self,):
        return self.date_time.strftime("%Y/%m/%d")
    
    def get_full_time_str(self):
        return self.date_time.strftime("%Y/%m/%d %H:%M:%S")
    

    def rebuild(self, new_standard:dict, new_grading_parm=None):
        grading_parm_is_changed = False
        if new_grading_parm is not None:
            if self.grading_parm != new_grading_parm:
                grading_parm_is_changed = True
                self.grading_parm = new_grading_parm

        #t = time.time()
        if new_standard['ranges'] != self.standard['ranges'] or grading_parm_is_changed :
            self.standard = new_standard
            standard_ranges = new_standard['ranges']
            self.ranges_string = reportUtils.ranges2str(standard_ranges)
            
            self.Grading = Grading(standard_ranges)
            self.cumGrading = cumGrading(self.get_full_range())
            self.Buffer.set_ranges(standard_ranges)

            xs = self.Buffer.total_buffer.get_feature(self.grading_parm)
            avg_volume = self.Buffer.total_buffer.get_feature('avg_volume')

            self.cumGrading.sieve_all(xs, avg_volume)
            sieve_partices_membership = self.Grading.sieve_all(xs, avg_volume)
            self.Buffer.set_sieve_memberships(sieve_partices_membership)

    
    def get_standard_ranges(self,):
        return self.standard['ranges']


    def get_standard_name(self,):
        return self.standard['name']
    
    def get_full_range(self,):
        ranges = np.array(self.standard['ranges'])
        return ranges.min(), ranges.max()
    

    def get_gaussian_data(self,step=1):
        diameters = self.Buffer.total_buffer.get_feature(self.grading_parm)
        if len(diameters) == 0:
            return [], []
        volumes = self.Buffer.total_buffer.get_feature('avg_volume')
        #return np.vstack((radiuses, volumes)).T
        volumes_percent = volumes
        low, high = self.get_full_range()
        bins = np.arange(low, high, step)

        ys, _ = np.histogram(diameters, bins, weights=volumes_percent)
        ys = ys / np.sum(ys) * 100
        
        center_xs = []
        for i in range(len(bins)-1):
            center = ( bins[i] + bins[i+1]  ) / 2
            center_xs.append( center  )

        return center_xs, ys
    
    def get_particles_count(self,):
        return len(self.Buffer.total_buffer.particels)
    

 

class reportUtils:

    @staticmethod
    def ranges2str(ranges):
        res = []
        for _range in ranges:
            range_str = f"{_range[0]}mm - {_range[1]}mm"
            res.append(range_str)
        return res
