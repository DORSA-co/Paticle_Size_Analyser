import numpy as np
from backend.Processing import utiltsCython
import CONSTANTS
from backend.Processing.particlesBuffer import particlesBuffer

class Grading:
    def __init__(self, sift_ranges) -> None:
        self.sift_ranges = np.array(sift_ranges, dtype=np.float64 )
        #save weighted histogram corespond to self.sift_ranges
        self.ranges_hist = np.zeros( (len(self.sift_ranges)) )


    def append(self, particles:particlesBuffer):
        """append new particels and calculate 

        Args:
            particles (particlesBuffer): _description_
        """
    
        #extract informations
        max_radiuses = particles.get_feature('max_radius')
        avg_volumes = particles.get_feature('avg_volume')
        
        
        res = utiltsCython.histogram(max_radiuses, self.sift_ranges, avg_volumes)
        self.ranges_hist += res

        
        
    def get_hist(self, )-> np.ndarray:
        """return histogram percentage

        Returns:
            np.ndarray: 1d array of percentage in each range
        """
        percentage_hist = self.ranges_hist / np.sum(self.ranges_hist) * 100.
        return np.round(percentage_hist, 1 )
    


    def get_hist_str(self, )-> []:
        """return histogram percentage

        Returns:
            np.ndarray: 1d array of percentage in each range
        """
        res = []
        for p in self.get_hist():
            res.append( str(p) + ' %' )
            
        return res
    