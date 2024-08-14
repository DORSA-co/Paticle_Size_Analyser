import cv2
import numpy as np

from backend.Processing.particlesDetector import particlesDetector
from backend.Processing.Particel import Particle
from Constants import CONSTANTS
WHILE_IN_CALIBRATION = 1

class CalibrationParent:

    def __init__(self, thresh=30, border=20, circularity=0.7, min_diameter_mm=0.8) -> None:
        self.circularity = circularity
        self.min_diameter_mm = min_diameter_mm
        self.accuracy = [] #deghat
        self.precision = [] #tekrar paziri

        # real diameters on calibration target
        self.real_diameters = CONSTANTS.Calibration.PARTICLES_DIAMETERS_MM
        self.real_diameters.sort()
        self.real_diameters = np.array(self.real_diameters)
        self.count = len(self.real_diameters)
        
        # -------------------------------
        self.thresh = thresh
        self.border = border
        # -------------------------------
    
    def find_particles(self, detector:particlesDetector, img:np.ndarray):
        particles = detector.detect(img, None)
        particles:list[Particle] = list(filter( self.__filter_particles, particles))
        particles.sort(key= lambda x:x.avg_diameter)

        return particles




    #-------------------------------------------------------
    
    

    def __filter_particles(self, p:Particle):
        return p.circularity >= self.circularity and (p.max_radius * 2) >= self.min_diameter_mm

    def check(self, img:np.ndarray):
        detector = self.build_particle_detector_obj()
        particles = detector.detect(img, None)
        particles = list(filter( self.__filter_particles, particles))
        p_count = len(particles)
        return  p_count== self.count, p_count, self.count, particles
    
    def get_result(self,):
        accuracy = np.array(self.accuracy).mean()
        
        
        return {
            'accuracy':accuracy,
        }
    
    def reset(self,):
        self.frames_diameters = []
        self.accuracy = []
        self.precision = 0


    def calculate_particle_diameters(self, particles:list[Particle])->list[float]:
        diameters = list( map( lambda x: x.avg_diameter, particles ))
        diameters = np.array(diameters)
        return diameters

    


class TelecentricCalibration(CalibrationParent):

    def __init__(self, thresh=30, border=20, circularity=0.7, min_diameter_mm=0.8, px2mm=1) -> None:
        super().__init__(thresh=30, border=20, circularity=0.7, min_diameter_mm=0.8)
        self.px2mm = px2mm

    # ------------------------------------------------------------------------------------
    def build_particle_detector_obj(self,):
        detector = particlesDetector(thresh=self.thresh, px2mm_ratio=self.px2mm, detection_border=self.border)
        return detector   

    def calibration(self, img):

        detector = self.build_particle_detector_obj()
        
        particles = self.find_particles(detector, img)

        
        #if find more particles, remove aditional small particles
        if len(particles) > self.count:
            return None
            particles = particles[-1: -self.count -1 : -1]
            particles.reverse()

        if len(particles) < self.count:
            return None

        diameters = self.calculate_particle_diameters(particles)
        self.accuracy.append(abs(diameters - self.real_diameters).mean())

        return particles, self.px2mm
    


class StandardCalibration(CalibrationParent):

    def __init__(self, thresh=30, border=20, circularity=0.7, min_diameter_mm=0.8) -> None:
        super().__init__(thresh, border, circularity, min_diameter_mm)

    def build_particle_detector_obj(self,):
        detector = particlesDetector(thresh=self.thresh, px2mm_ratio=1, detection_border=self.border)
        return detector   

    def calibration(self, img):
        detector = self.build_particle_detector_obj()
        particles = self.find_particles(detector=detector, img=img)
        
        #if find more particles, remove aditional small particles
        if len(particles) > self.count:
            return None
            # particles = particles[-1: -self.count -1 : -1]
            # particles.reverse()

        if len(particles) < self.count:
            return None
        
        px2mm = self.calculate_px2mm(particles)

        changed_particles = []
        for particle in particles:
            new_particle = particle.change_px2mm(px2mm=px2mm)
            changed_particles.append(new_particle)

        # ----- calculate accuracy
        diameters = self.calculate_particle_diameters(changed_particles)
        self.accuracy.append(abs(diameters - self.real_diameters).mean())

        return changed_particles, px2mm
    
    #------------------------------------------------------------------------------
    def calculate_px2mm(self, particles):
        circle_pxvalues = []
        for index, particle in enumerate(particles):
            circle_pxvalues.append(self.single_circle_px2mm(index, particle))
        return np.mean(circle_pxvalues)
    # -----------------------------------------------------------------------------
    def single_circle_px2mm(self, index, particle:Particle) ->float:
        return CONSTANTS.Calibration.PARTICLES_DIAMETERS_MM[index]/particle.min_diameter



class CalibrateIterator:
    def __init__(self, calibrator:TelecentricCalibration|StandardCalibration):
        
        self.px2mmList = []
        self.frames_diameters = []
        self.resultList :dict[str, list]= {}
        self.calibator = calibrator




    def calibration(self, img:np.ndarray):
        
        particles, px2mm = self.calibator.calibration(img=img)
        diameters = self.calibator.calculate_particle_diameters(particles)

        
        self.frames_diameters.append(diameters)
        self.px2mmList.append(px2mm)

        result = self.calibator.get_result()
        for key in result.keys():
            if key not in self.resultList.keys():
                self.resultList[key] = []
            self.resultList[key].append(result[key])


        return particles, px2mm


    def reset(self):
        self.px2mmList = []
        self.resultList :dict[str, list]= {}

    def get_px2mm(self):
        return np.mean(self.px2mmList)
    
    def get_result(self)->dict:
        precision = np.array(self.frames_diameters).std(axis=0).mean()

        result = {}
        for key in self.resultList.keys():
            result[key] = np.mean(self.resultList[key])

        result['precision'] = precision

        return result
        