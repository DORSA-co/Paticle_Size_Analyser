import numpy as np
#from backend.Processing import utiltsCython
from Constants import CONSTANTS
from backend.Processing.particlesBuffer import particlesBuffer
from backend.Processing.Particel import Particle
from backend.Processing import gradingUtils 



class gradingABstract:

    def __init__(self, ranges) -> None:
        self.sieve_ranges = self.generate_ranges(ranges)
        self.ranges_hist = np.zeros( (len(self.sieve_ranges)) )
    
    def generate_ranges(self, ranges):
        return np.array(ranges, dtype=np.float64 )

    def clear(self,):
        self.ranges_hist = np.zeros( (len(self.sieve_ranges)) )

    
    def __get_sift_idx(self, x , ranges):
        for i, (low, high) in enumerate(ranges):
            if low<= x < high:
                return i
        return -1


    
    def append_particle(self, particle:Particle):
        diameter = particle.max_diameter
        sieve_idx = self.__get_sift_idx(diameter, ranges=self.sieve_ranges)
        if sieve_idx>=0:
            self.ranges_hist[sieve_idx] += particle.avg_volume
        return sieve_idx
    

    def sieve_all(self, diameters:np.ndarray, volumes:np.ndarray) -> list[np.ndarray]:
        sieve_partices_membership = []
        for i,(low, high) in enumerate(self.sieve_ranges):
            membership = np.bitwise_and( diameters>=low , diameters<high )
            sieve_partices_membership.append(membership)
            
            if membership.shape[0] !=0:
                self.ranges_hist[i] = np.sum( volumes[membership] )
            else:
                self.ranges_hist[i] = 0

        return sieve_partices_membership

    



class Grading(gradingABstract):
    def __init__(self, sieve_ranges) -> None:
        super().__init__(sieve_ranges)
        

    # def append(self, particles:particlesBuffer):
    #     """append new particels and calculate 

    #     Args:
    #         particles (particlesBuffer): _description_
    #     """
    
    #     #extract informations
    #     max_radiuses = particles.get_feature('max_radius')
    #     avg_volumes = particles.get_feature('avg_volume')
        
    #     #res = utiltsCython.histogram(max_radiuses, self.sieve_ranges, avg_volumes)
        

    #     particels_range_idx, hist = utiltsCython.sieve(max_radiuses, self.sieve_ranges,avg_volumes)
    #     self.ranges_hist += hist

    #     return particels_range_idx

    
        
        
    def get_hist(self, )-> np.ndarray:
        """return histogram percentage

        Returns:
            np.ndarray: 1d array of percentage in each range
        """
        sum_bins = np.sum(self.ranges_hist) 
        if sum_bins != 0:
            percentage_hist = self.ranges_hist / sum_bins * 100.
            return np.round(percentage_hist, 1 )

        return self.ranges_hist #all are zero
    


    def get_hist_str(self, )-> []:
        """return histogram percentage

        Returns:
            np.ndarray: 1d array of percentage in each range
        """
        res = []
        for p in self.get_hist():
            res.append( str(p) + ' %' )
            
        return res
    








class cumGrading(gradingABstract):
    step = 0.25
    def __init__(self, full_range) -> None:
        super().__init__(full_range)

    def generate_ranges(self, full_range):
        n_ranges = (full_range[1] - full_range[0]) // self.step + 1
        n_ranges = int(n_ranges)

        sieve_ranges = []
        lower_limit = full_range[0]
        for i in range(n_ranges):
            sieve_ranges.append( [lower_limit, lower_limit + self.step] )
            lower_limit+= self.step
        
        return np.array(sieve_ranges)

    def get_data(self, )-> np.ndarray:
        """return histogram percentage

        Returns:
            np.ndarray: 1d array of percentage in each range
        """
        sum_ranges =  np.sum(self.ranges_hist)
        if sum_ranges!=0:
            percentage_hist = self.ranges_hist / np.sum(self.ranges_hist) * 100.
            xs = np.mean(self.sieve_ranges, axis=1)
            ys = np.cumsum(percentage_hist)
            #ys[-1] = 100
            return xs, ys   
        else:
            return [],[]
    


  