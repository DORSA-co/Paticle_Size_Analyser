import numpy as np
import Constants.CONSTANTS as CONSTANTS
import cv2

class Particle:
    """store information of one particle
    """
    def __init__(self, cnt:np.ndarray, px2mm:float, img_id) -> None:
        """
        Args:
            cnt (np.ndarray): single opencv contoure
            px2mm (float): ratio to convert px size into mm size. (mm/px)
            img_id (_type_): An arbitrary value to indicate which image each particle belongs to
        """
        self.cnt = cnt
        self.px2mm = px2mm
        self.img_id = img_id
        self.area = None
        self.center = None
        self.max_radius = None
        self.calc_area()
        self.calc_max_radius()
        self.calc_avrage_radius()
        self.calc_avrage_valoum()
        self.calc_cirvularity()
    

    def calc_cirvularity(self,):
        self.circularity = self.area / (np.pi * self.max_radius **2) 

    def calc_area(self):
        """calculate area of a particle
        """
        self.area = cv2.contourArea(self.cnt)
        self.area = self.area * ( self.px2mm ** 2 )
    
    def calc_max_radius(self):
        """calculate max radius of the particle
        """
        self.center, self.max_radius = cv2.minEnclosingCircle(self.cnt)
        self.max_radius = self.max_radius * self.px2mm * 2

    def calc_avrage_radius(self):
        """calculates avrage radius of a particle
        """
        self.avg_radius = np.sqrt(self.area / np.pi) * 2  #area = pi*r^2
    
    def calc_avrage_valoum(self):
        """calc volume of the particle by its avg_radius
        """
        self.avg_volume = 4/3 * np.pi * (self.avg_radius ** 3)

    
    def get_roi(self, border=10) -> tuple:
        """returns a bounding box that is a crop of orginal image that particle is in it

        Args:
            border (int, optional): border of crop image. Defaults to 10.

        Returns:
            tuple:  (min_x, min_y), (max_x, max_y)
        """
        min_x, min_y = np.min(self.cnt, axis=(0,1)) - border
        max_x, max_y = np.max(self.cnt, axis=(0,1)) + border

        min_x = max(min_x, 0)
        min_y = max(min_y, 0)
        return (min_x, min_y), (max_x, max_y)
    

    def get_roi_image(self, image, border = 10):
        (x1,y1),(x2,y2) = self.get_roi()
        return image[y1:y2, x1:x2]
    

    def get_info(self):
        info = {}
        info['max_radius'] = np.round(self.max_radius, CONSTANTS.DECIMAL_ROUND )
        info['area'] = np.round(self.area, CONSTANTS.DECIMAL_ROUND )
        info['avrage_radius'] = np.round(self.avg_radius, CONSTANTS.DECIMAL_ROUND )
        info['volume'] = np.round(self.avg_volume, CONSTANTS.DECIMAL_ROUND )
        info['circularity'] = np.round(self.circularity, CONSTANTS.DECIMAL_ROUND )
        return info



    def get_id(self):
        return self.img_id

