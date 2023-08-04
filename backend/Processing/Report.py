from backend.Processing.particlesBuffer import particlesBuffer
from backend.Processing.Grading import Grading
from backend.Processing import gradingUtils
import numpy as np
from datetime import datetime
import CONSTANTS






class Report:
    """store all information of a sample
    """
    def __init__(self, name = None, standard = None, username = '', main_path ='') -> None:
        
        self.name = name
        self.standard = standard
        self.username = username
        self.main_path = main_path
        self.date = datetime.now()
        self.Buffer = particlesBuffer()
        self.sieved_particles = []

        if self.standard is not None:
            self.ranges_string = reportUtils.ranges2str(self.standard['ranges'])
        
        if standard is not None:
            self.Grading = Grading(self.standard['ranges'])
        else:
            assert True, "not developed yet"


    def set_operator_username(self, username):
        self.username = username


    def append(self, buffer:particlesBuffer):
        """append a buffer of particles into this sample

        Args:
            buffer (particlesBuffer): _description_
        """
        #append new particle for histogram calculation 
        self.Grading.append(buffer)
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
        for i,range_name in enumerate(self.ranges_string):
            data = {}
            if len(self.sieved_particles[i]) > 0:
                data['range'] = range_name
                data['std'] = np.round( self.sieved_particles[i].std(), CONSTANTS.DECIMAL_ROUND )
                data['avrage'] = np.round( self.sieved_particles[i].mean(), CONSTANTS.DECIMAL_ROUND )
                data['count'] = len( self.sieved_particles[i] )
            else:
                data['range'] = '-'
                data['std'] = '-'
                data['avrage'] = '-'
                data['count'] = '-'
            res.append(data)

        return res


        














class reportUtils:

    @staticmethod
    def ranges2str(ranges):
        res = []
        for _range in ranges:
            range_str = f"{_range[0]}mm - {_range[1]}mm"
            res.append(range_str)
        return res
