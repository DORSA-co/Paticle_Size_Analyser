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