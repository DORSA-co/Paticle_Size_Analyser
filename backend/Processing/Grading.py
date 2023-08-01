import numpy as np
from backend.Processing import utiltsCython
import CONSTANTS


class Grading:
    def __init__(self, sift_ranges) -> None:
        self.sift_ranges = np.array(sift_ranges, dtype=np.float64 )
        #save weighted histogram corespond to self.sift_ranges
        self.ranges_hist = np.zeros( (len(self.sift_ranges)) )
        
        self.xs = []
        self.weights = []
        #self.sorted = False


    def append(self, xs, weights):
        """append new datas and calculating histogram xs base on weights

        Args:
            xs (_type_): array of 
            weights (_type_): _description_
        """
        #new_datas =  np.vstack((xs, weights)).T
        res = utiltsCython.histogram(xs, self.sift_ranges, weights)
        self.ranges_hist += res
        
        if len(self.xs) == 0:
            self.xs = xs
            self.weights = weights
        else:
            self.xs = np.hstack((self.xs, xs))
            self.weights = np.hstack((self.weights, weights))

        #this flag show the self.datas aren't sort beacuse of new_data appended at the end without sorting after that
        #self.sorted = False

    def get_hist(self, )-> np.ndarray:
        """return histogram percentage

        Returns:
            np.ndarray: 1d array of percentage in each range
        """
        percentage_hist = self.ranges_hist / np.sum(self.ranges_hist) * 100.
        return percentage_hist
    
    def get_statistics(self,):
        data = {}
        data['avrage'] = np.round(self.xs.mean(), CONSTANTS.DECIMAL_ROUND )
        data['std'] = np.round(self.xs.std(), CONSTANTS.DECIMAL_ROUND )
        return data
    
    def update_sift_ranges(self, new_ranges):
        """change sift ranges

        Args:
            new_ranges (_type_): list of ranges like [[0,2], [2,4]]
        """
        self.sift_ranges = np.array(new_ranges, dtype=np.float64 )
        self.cumulative_results = np.zeros( (len(self.sift_ranges)) )
        self.ranges_hist = utiltsCython.hist(self.xs, self.sift_ranges, self.weights)
        