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
        self.calc_min_radius()

        self.max_diameter = self.max_radius * 2
        self.avg_diameter = self.avg_radius * 2
    

    def calc_cirvularity(self,):
        self.circularity = self.area / (np.pi * self.max_radius **2) 

    def calc_area(self):
        """calculate area of a particle
        """
        self.area = cv2.contourArea(self.cnt)
        self.area = self.area * ( self.px2mm ** 2 )

    def calc_min_radius(self):
        """calculate min radius of the particle
        """
        _, (w, h), _ = cv2.minAreaRect(self.cnt)
        self.min_diameter = min(w, h)
        self.min_diameter = self.min_diameter * self.px2mm
        self.min_raduis = self.min_diameter / 2
        
    
    def calc_max_radius(self):
        """calculate max radius of the particle
        """
        self.center, self.max_radius_px = cv2.minEnclosingCircle(self.cnt)
        self.max_radius = self.max_radius_px * self.px2mm
        self.max_radius_px = int(self.max_radius_px)

    def calc_avrage_radius(self):
        """calculates avrage radius of a particle
        """
        self.avg_radius = np.sqrt(self.area / np.pi)  #area = pi*r^2
    
    def calc_avrage_valoum(self):
        """calc volume of the particle by its avg_radius
        """
        self.avg_volume = 4/3 * np.pi * (self.avg_radius ** 3)

    
    def get_roi(self, border=20) -> tuple:
        """returns a bounding box that is a crop of orginal image that particle is in it

        Args:
            border (int, optional): border of crop image. Defaults to 10.

        Returns:
            tuple:  (min_x, min_y), (max_x, max_y)
        """
        cx, cy = self.center
        cx , cy = int(cx), int(cy)
        dist = self.max_radius_px
        dist += border
        
        min_x = cx - dist
        min_y = cy - dist
        max_x = cx + dist
        max_y = cy + dist
       
        
        # else:
        #     min_x, min_y = np.min(self.cnt, axis=(0,1)) - border
        #     max_x, max_y = np.max(self.cnt, axis=(0,1)) + border

        min_x = max(min_x, 0)
        min_y = max(min_y, 0)
        return (min_x, min_y), (max_x, max_y)
    

    def get_roi_image(self, image, border = 20):
        (x1,y1),(x2,y2) = self.get_roi(border)
        return image[y1:y2, x1:x2]

    

    def get_info(self):
        info = {}
        info['max_diameter'] = np.round(self.max_diameter, CONSTANTS.DECIMAL_ROUND )
        info['avg_diameter'] = np.round(self.avg_diameter, CONSTANTS.DECIMAL_ROUND )
        info['min_diameter'] = np.round(self.min_diameter, CONSTANTS.DECIMAL_ROUND )
        info['max_radius'] =  np.round(self.max_radius, CONSTANTS.DECIMAL_ROUND )
        info['avg_radius'] =  np.round(self.avg_radius, CONSTANTS.DECIMAL_ROUND )
        info['min_dradius'] = np.round(self.min_raduis, CONSTANTS.DECIMAL_ROUND )
        info['area'] = np.round(self.area, CONSTANTS.DECIMAL_ROUND ** 2 )
        info['volume'] = np.round(self.avg_volume, CONSTANTS.DECIMAL_ROUND ** 3 )
        info['circularity'] = np.round(self.circularity, CONSTANTS.DECIMAL_ROUND )
        
        return info


    def get_enclosing_circle(self, transorm_to_single_img=False, to_int=True):
        center = self.center
        radius = self.max_radius_px
        if transorm_to_single_img:
            x,y = center
            (x1,y1), _ = self.get_roi()
            x = max(x - x1,0)
            y = max(y - y1,0)
            center = x,y
        
        if to_int:
            center = int(center[0]), int(center[1])
            radius = int(radius)
        return center, radius
    
    def get_contour(self, transorm_to_single_img=False):
        cnt = self.cnt.copy()
        if transorm_to_single_img:
            (x1,y1), _ = self.get_roi()
            cnt[:,0,0] = cnt[:,0,0] - x1
            cnt[:,0,1] = cnt[:,0,1] - y1
        
        return cnt


    def get_id(self):
        return self.img_id

