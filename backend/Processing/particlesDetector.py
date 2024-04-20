import cv2
import numpy as np
import pandas as pd
from backend.Processing.Particel import Particle
from backend.Processing.particlesBuffer import particlesBuffer, sieveParticlesBuffer
from backend.Processing.Report import Report
import time

class particlesDetector:

    def __init__(self, thresh:int, px2mm_ratio:float, detection_border:int=10, min_size=0.15 ) -> None:
        self.thresh = thresh
        self.detection_border = detection_border
        self.px2mm_ratio = px2mm_ratio
        self.particle_id = 0
        self.img_id = 0
        self.min_size = min_size



    def ــisـinsideـareaــ(self, cnt, border: int , img_shape: tuple) -> bool:
        """ checks a particle is in inter a image by considering border. 

        Args:
            cnt (_type_): particle conture
            border (int): border of acceptable space
            img_shape (tuple): img_height, img_width

        Returns:
            bool: return True if partice be in inter area
        """
        min_x, min_y = np.min(cnt, axis=(0,1))
        max_x, max_y = np.max(cnt, axis=(0,1))
        
        img_h, img_w = img_shape
        
        if min_x >= border and min_y >= border:
            if max_x <= img_w - border and max_y <= img_h - border:
                return True
        
        return False




    def detect(self, img, report:Report) -> list[Particle]:
        """returns list of paricles in the given image

        Args:
            img (_type_): input image

        Returns:
            list[Particle]: founded particles
        """
        #convert image to gray scale if it is a color image
        
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, mask = cv2.threshold(img, self.thresh, 255, cv2.THRESH_BINARY_INV)

        mask = cv2.erode(mask, np.ones((2,2)), iterations=1)
        mask = cv2.dilate(mask, np.ones((2,2)), iterations=1)
        #mask = cv2.erode(mask, np.ones((3,3)), iterations=1)

        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #filter pellets that are in defeinded image area
        filter_inter_area = lambda x: self.ــisـinsideـareaــ(x, border=self.detection_border, img_shape= img.shape )
        cnts = list(filter( filter_inter_area, cnts ))

        #particles = list(map( lambda cnt: Particle(cnt, self.px2mm_ratio), cnts ))

        
        # particles = particlesBuffer()
        particles = []
        for cnt in cnts:
                particle = Particle(cnt, self.px2mm_ratio, self.particle_id)
                if particle.avg_diameter < self.min_size:
                    continue
                if report is not None:
                    report.append_particle(particle)
                particles.append(particle)
                self.particle_id+=1
                

        self.img_id+=1
        return particles









def draw_particles(img, particles: list[Particle], color:tuple=(40, 40, 200), thickness:int=5):
    """draw particles conture on image

    Args:
        img (_type_): input image
        particles (list[Particle]): list of partiles
        color (tuple, optional): color of drawing . Defaults to (200,0,0).
        thickness (int, optional): thickness of drawing. Defaults to 2.

    Returns:
        _type_: drawed image
    """
    #t = time.time()
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    cnts = list( map( lambda x:x.cnt, particles))
    res = cv2.drawContours(img, cnts, -1, color, thickness=thickness)
    #print(time.time() - t)
    return res

def draw_particles_size(img, particles: list[Particle], color:tuple=(40, 40, 200), thickness:int=5, font_scale=4):
    """draw particles conture on image

    Args:
        img (_type_): input image
        particles (list[Particle]): list of partiles
        color (tuple, optional): color of drawing . Defaults to (200,0,0).
        thickness (int, optional): thickness of drawing. Defaults to 2.

    Returns:
        _type_: drawed image
    """
    #t = time.time()
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for particle in particles:
        center = particle.center
        diameter = particle.avg_radius * 2
        diameter = np.round(diameter, 2)
        text = str(diameter) + ' mm'
        res = cv2.putText(  img, 
                            text=text, 
                            org=(int(center[0]), int(center[1]) ),
                            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            fontScale=font_scale,
                            color=color,
                            thickness=thickness
                        )


    return res








