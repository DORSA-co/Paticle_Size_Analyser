from backend.Processing.particlesBuffer import particlesBuffer
from backend.Processing.Grading import Grading
import numpy as np
from datetime import datetime







class Report:
    """store all information of a sample
    """
    def __init__(self, name = None, standard = None ) -> None:
        self.Buffer = particlesBuffer()
        self.name = name
        self.standard = standard
        self.date = datetime.now()
        
        if standard is not None:
            self.Grading = Grading(self.standard['ranges'])
        else:
            assert True, "not developed yet"

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
        info['avrage'] = self.Buffer.get_feature('max_radius').mean()
        info['std'] = self.Buffer.get_feature('max_radius').std()

        return info
        