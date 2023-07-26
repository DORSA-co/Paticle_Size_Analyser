import cv2
import numpy as np
import pandas as pd


class Particle:
    def __init__(self, cnt, px2mm) -> None:
        self.cnt = cnt
        self.px2mm = px2mm
        self.calc_area()
        self.calc_max_radius()
        self.calc_avrage_radius()
        self.calc_avrage_valoum()

    def calc_area(self):
        self.area = cv2.contourArea(self.cnt)
        self.area = self.area * ( self.px2mm ** 2 )
    
    def calc_max_radius(self):
        self.center, self.max_radius = cv2.minEnclosingCircle(self.cnt)
        self.max_radius = self.max_radius * self.px2mm

    def calc_avrage_radius(self):
        self.avg_radius = np.sqrt(self.area / np.pi)  #area = pi*r^2
    
    def calc_avrage_valoum(self):
        self.avg_volume = 4/3 * np.pi * (self.avg_radius ** 3)

    
    def get_roi(self, border=10):
        min_x, min_y = np.min(self.cnt, axis=(0,1)) - border
        max_x, max_y = np.min(self.cnt, axis=(0,1)) + border
    
        return (min_x, min_y), (max_x, max_y)


class telecentricPx2mm:

    def __init__(self, camera_pixel_size:float, lens_mag:float) -> None:
        """calculate diffrent kind of size like radius and volume in mm

        Args:
            camera_pixel_size (float): size of camera pixel on sensor in mm
            lens_mag (float): magnification of telesentric lens
        """
        self.camera_pixel_size = camera_pixel_size
        self.lens_mag = lens_mag

        #ratio to convert size in px to mm in power of 1
        self.ratio = self.camera_pixel_size/self.lens_mag


    def px2mm(self, x:int, power:int) -> float:
        """convert a pixel size into mm size in power of 'power' argument

        Args:
            x (int): input pixel size
            power (int): relation power

        Returns:
            float: size in mm
        """
        return x * (self.ratio ** power)


        
  
        



class particlesDetector:

    def __init__(self, thresh:int, px2mm_ratio:float, detection_border:int=10, ) -> None:
        self.thresh = thresh
        self.detection_border = detection_border
        self.px2mm_ratio = px2mm_ratio



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




    def detect(self, img, return_particls=True, return_dataframe=True) -> list[Particle]:
        """returns list of paricles in the given image

        Args:
            img (_type_): input image

        Returns:
            list[Particle]: founded particles
        """

        #conver image to gray scale if it is a color image
        assert return_dataframe or return_particls, "couldnt be False both return_particls and return_dataframe"
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, mask = cv2.threshold(img, self.thresh, 255, cv2.THRESH_BINARY_INV)

        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #filter pellets that are in defeinded image area
        filter_inter_area = lambda x: self.ــisـinsideـareaــ(x, border=self.detection_border, img_shape= img.shape )
        cnts = list(filter( filter_inter_area, cnts ))

        #particles = list(map( lambda cnt: Particle(cnt, self.px2mm_ratio), cnts ))

        data = {
            "max_radius": [],
            "avg_radius": [],
            "area": [],
            "avg_volume": []
            }
        
        particles = []
        for cnt in cnts:
            if return_particls:
                particles.append(Particle(cnt, self.px2mm_ratio))

            if return_dataframe:
                data['area'].append(particles[-1].area)
                data['max_radius'].append(particles[-1].max_radius)
                data['avg_radius'].append(particles[-1].avg_radius)
                data['avg_volume'].append(particles[-1].avg_radius)

        if return_dataframe and particles:
            return particles, pd.DataFrame(data)

        elif particles:
            return particles
        
        elif return_dataframe:
            pd.DataFrame(data)




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
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    cnts = list( map( lambda x:x.cnt, particles))
    return cv2.drawContours(img, cnts, -1, color, thickness=thickness)








if __name__ == '__main__':
    import time
    from Grading import Grading

    img = cv2.imread('backend\Processing/test.png')
    px2mm = telecentricPx2mm(3.45/1000, 0.095)
    detector = particlesDetector(100, px2mm_ratio=px2mm.ratio, detection_border=10)
    
    all_ps = []
    t = time.time()
    ps = detector.detect(img, return_dataframe=False)
    

    
    gr = Grading( sift_ranges=[[0,2], [2,4],[4,6]])
    
    data = np.array( list( map( lambda x:(x.max_radius, x.avg_volume), ps )))
    gr.append(data[:,0], data[:,1])

    #gr.append(df['max_radius'].to_numpy(), df['avg_volume'].to_numpy())
    

    t = time.time()-t
    print(t)

    res = draw_particles(img, ps)

    

    # cv2.imshow('res', res)
    # cv2.waitKey(0)
    # pass