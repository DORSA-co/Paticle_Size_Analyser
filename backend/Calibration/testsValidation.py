import numpy as np
from Constants import CONSTANTS

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
        self.ranges_middle_size = []
        for l,h in ranges:
            mean = (l + h) / 2
            self.ranges_middle_size.append( mean )
    