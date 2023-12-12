import numpy as np
from Constants import CONSTANTS
from scipy import stats
from scipy.stats import t as t_table

class Validation:
    
    def __init__(self,) -> None:
        self.system_tests = []
        self.sieve_tests = []

    def add_test(self, system, sieve):
        self.system_tests.append(system)
        self.sieve_tests.append(sieve)
    
    def set_test(self, system_test, sieve_tests):
        self.system_tests = system_test
        self.sieve_tests = sieve_tests

    def preprocess(self):
        self.system_tests = np.array( self.system_tests )
        self.sieve_tests = np.array( self.sieve_tests )



class weightDifferenceValidation(Validation):

    def __init__(self) -> None:
        super().__init__()


    def calculate_weight_diffrenct(self,) -> np.ndarray:
        diff = np.abs(self.system_tests - self.sieve_tests)
        werror = np.sum( diff * self.sieve_tests , axis=1) / 100
        return werror
    


    def calculate(self,):
        self.preprocess()

        w_errors = self.calculate_weight_diffrenct()
        ranges_std_sieve = np.std(self.sieve_tests, axis=0)
        ranges_mean_sieve = np.mean(self.sieve_tests, axis=0)

        w_std_sieve = np.sum(ranges_mean_sieve * ranges_std_sieve) / 100
        w_error_system = np.mean(w_errors)

        w_std_sieve = np.round(w_std_sieve,CONSTANTS.DECIMAL_ROUND)
        w_error_system = np.round(w_error_system,CONSTANTS.DECIMAL_ROUND)
        status = w_error_system <= w_std_sieve

        infoes = {
                'sieve_std' : w_std_sieve,
                'error' : w_error_system,
        }
        return status, infoes




class tTestValidation(Validation):
    
    def __init__(self) -> None:
        super().__init__()


    def set_ranges(self, ranges:list[list[int]]):
        # self.ranges_middle_size = []
        # for l,h in ranges:
        #     mean = (l + h) / 2
        #     self.ranges_middle_size.append( mean )
        
        self.ranges_middle_size = np.array(ranges).mean(axis=1)
    

    def calculate_mean_sample(self,tests: np.ndarray) -> np.ndarray:
        """_summary_

        Args:
            tests (np.ndarray): 2d array thay each row is percents of a sample e.g [[10,80,10], [20,65,15]]

        Returns:
            np.ndarray: 1D array that each index is mean size of a sample
        """
        return np.sum(tests * self.ranges_middle_size , axis=1) / 100.
            



    def calculate(self, confidence=0.95):
        self.preprocess()

        system_test_mean = self.calculate_mean_sample(self.system_tests)
        sieve_tests_mean = self.calculate_mean_sample(self.sieve_tests)
        
        # n = (np.mean(system_test_mean) - np.mean(sieve_tests_mean))
        # d = np.sqrt(  np.std( system_test_mean)**2 /len(system_test_mean)  
        #             + np.std(sieve_tests_mean)**2 /  len(sieve_tests_mean)
        #               )
        # degree_of_freedom = len(system_test_mean) + len(sieve_tests_mean) - 2
        # t_value = n / ( d + 1e-5)
        res = stats.ttest_ind(system_test_mean, sieve_tests_mean)
        t_score, p_value, df = res.statistic, res.pvalue, res.df

        status = t_score < t_table.ppf(confidence, df)
        
        for best_confidence in [0.5, 0.75, 0.8, 0.85, 0.9, 0.95, 0.975, 0.99, 0.995, 0.999, 0.9995]:
            if t_score < t_table.ppf(best_confidence, df):
                break
        else:
            best_confidence = '-'


        infoes = {
                't_score' : np.round(t_score,3),
                'p_value': np.round(p_value,3),
                'df': df,
                'best_confidence': best_confidence
        }
        return status, infoes