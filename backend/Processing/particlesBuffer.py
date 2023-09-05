from backend.Processing.Particel import Particle
from backend.Utils import dataUtils
import numpy as np

class particlesBuffer:
    """stores particles in two format list[Particle] and numpy.ndarray
    """
    COLS_IDX = {
        'area':0,
        'max_radius':1,
        'avg_radius':2,
        'avg_volume':3,
    }

    def __init__(self,) -> None:
        self.particels = []
        self.data = []

    def append(self, particel:Particle):
        """add a single particle into buffer

        Args:
            particel (Particle)
        """

        #store some data like max_radius in np.ndarray for fast access to a specific information for all particles
        pdata = [0,] * len(self.COLS_IDX)
        pdata[self.COLS_IDX['area']] = particel.area
        pdata[self.COLS_IDX['max_radius']] = particel.max_radius
        pdata[self.COLS_IDX['avg_radius']] = particel.avg_radius
        pdata[self.COLS_IDX['avg_volume']] = particel.avg_volume
        pdata = np.array( pdata )

        #store particles in list[Particle] format for better and easy access
        self.particels.append( particel )


        if len(self.data) != 0:
            self.data = np.vstack((self.data, pdata))
        else:
            self.data = pdata
    
    def extend(self, particels_buffer:'particlesBuffer'):
        """extend another buffer into this buffer

        Args:
            particels_buffer (particlesBuffer): 
        """
        self.particels = self.particels + particels_buffer.particels

        if len(self.data) !=0:    
            self.data = np.vstack((self.data , particels_buffer.data))
        else:
            self.data = particels_buffer.data

    
    def get_particels(self) -> list[Particle]:
        """returns list of particles

        Returns:
            list[Particle]: list of Particle Objects
        """
        return self.particels
    
    def get_particel(self, idx) -> Particle:
        """returns list of particles

        Returns:
            list[Particle]: list of Particle Objects
        """
        return self.particels[idx]
    
    def get_feature(self, name: str, decimals=2) -> np.ndarray:
        """returns a 1d numpy array that shows a specific feature for all particles

        Args:
            name (str): name of the desired feature that can be one of the [ 'area', 'max_radius', 'avg_radius', 'avg_volume' ]

        Returns:
            np.ndarray: _description_
        """
        return np.round(self.data[:, self.COLS_IDX[name]], decimals=decimals)
    



    