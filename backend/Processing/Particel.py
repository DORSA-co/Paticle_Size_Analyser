import numpy as np
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
        self.calc_area()
        self.calc_max_radius()
        self.calc_avrage_radius()
        self.calc_avrage_valoum()

    def calc_area(self):
        """calculate area of a particle
        """
        self.area = cv2.contourArea(self.cnt)
        self.area = self.area * ( self.px2mm ** 2 )
    
    def calc_max_radius(self):
        """calculate max radius of the particle
        """
        self.center, self.max_radius = cv2.minEnclosingCircle(self.cnt)
        self.max_radius = self.max_radius * self.px2mm

    def calc_avrage_radius(self):
        """calculates avrage radius of a particle
        """
        self.avg_radius = np.sqrt(self.area / np.pi)  #area = pi*r^2
    
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
        max_x, max_y = np.min(self.cnt, axis=(0,1)) + border
    
        return (min_x, min_y), (max_x, max_y)


