import cv2
import numpy as np

from backend.Processing.particlesDetector import particlesDetector
from backend.Processing.Particel import Particle
from Constants import CONSTANTS



        

class Calibration:

    def __init__(self, thresh=30, border=20, circularity=0.7, min_diameter_mm=0.8) -> None:
        self.circularity = circularity
        self.min_diameter_mm = min_diameter_mm
        self.frames_diameters = []
        self.accuracy = [] #deghat
        self.precision = [] #tekrar paziri

        self.real_diamerers = CONSTANTS.Calibration.PARTICLES_DIAMETERS_MM
        self.real_diamerers.sort()
        self.real_diamerers = np.array(self.real_diamerers)
        self.count = len(self.real_diamerers)
        
        self.detector = particlesDetector(thresh=thresh, px2mm_ratio=CONSTANTS.Calibration.PX2MM, detection_border=border)
    

    def __filter_particles(self, p:Particle):
        return p.circularity >= self.circularity and (p.max_radius * 2) >= self.min_diameter_mm

    def check(self, img:np.ndarray):
        particles = self.detector.detect(img, None)
        particles = list(filter( self.__filter_particles, particles))
        p_count = len(particles)
        return  p_count== self.count, p_count, self.count, particles
        

    def calibration(self, img):
        particles = self.detector.detect(img, None)

        particles:list[Particle] = list(filter( self.__filter_particles, particles))
        particles.sort(key= lambda x:x.avg_diameter)
        
        #if find more particles, remove aditional small particles
        if len(particles) > self.count:
            return None
            particles = particles[-1: -self.count -1 : -1]
            particles.reverse()

        if len(particles) < self.count:
            return None

        diameters = list( map( lambda x: x.avg_diameter, particles ))
        diameters = np.array(diameters)
        self.frames_diameters.append(diameters)
        self.accuracy.append(abs(diameters - self.real_diamerers).mean())

        return particles
    
    def get_result(self,):
        accuracy = np.array(self.accuracy).mean()
        precision = np.array(self.frames_diameters).std(axis=0).mean()
        
        return {
            'accuracy':accuracy,
            'precision': precision
        }


        
    
    def reset(self,):
        self.frames_diameters = []
        self.accuracy = []
        self.precision = 0
