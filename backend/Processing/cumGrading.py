import numpy as np
from backend.Processing import utiltsCython
import CONSTANTS
from backend.Processing.particlesBuffer import particlesBuffer

class cumGrading:
    step = 0.25
    def __init__(self, full_range) -> None:
        
        #save weighted histogram corespond to self.sift_ranges
        self.sift_ranges = self.generate_ranges(full_range)
        self.clear()

    def clear(self,):
        self.ranges_hist = np.zeros( (len(self.sift_ranges)) )

    def generate_ranges(self, full_range):
        n_ranges = (full_range[1] - full_range[0]) // self.step + 1
        n_ranges = int(n_ranges)

        sift_ranges = []
        lower_limit = full_range[0]
        for i in range(n_ranges):
            sift_ranges.append( [lower_limit, lower_limit + self.step] )
            lower_limit+= self.step
        
        return np.array(sift_ranges)

        

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

        
        
    def get_data(self, )-> np.ndarray:
        """return histogram percentage

        Returns:
            np.ndarray: 1d array of percentage in each range
        """
        percentage_hist = self.ranges_hist / np.sum(self.ranges_hist) * 100.
        xs = np.mean(self.sift_ranges, axis=1)
        ys = np.cumsum(percentage_hist)
        return xs, ys
    


  