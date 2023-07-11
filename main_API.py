import sys, os
sys.path.append( os.getcwd() + "/backend" )
sys.path.append( os.getcwd() + "/PagesAPI" )
sys.path.append( os.getcwd() + "/PagesUI" )
import cv2

import dorsaPylon
from dorsaPylon import Collector, Camera
from cameraThread import cameraThread
# from setting_API import settingAPI
# from settingUI import settingUI

serial_number = '23804186'
class main_API:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.camera = None
        self.creat_camera()
        self.run_camera_grabbing()
        


        #------pages_API--------
        # self.setting_api = settingAPI( settingUI  )

    def grabbed_image_interrupt(self,):
        img = self.camera.image
        cv2.imshow('img', cv2.resize(img, None, fx=0.25, fy=0.25))

    def creat_camera(self)-> Camera:
        collector = Collector()
        self.camera = collector.get_camera_by_serial(serial_number)
        self.camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)

    def run_camera_grabbing(self,):
        self.camera.Operations.start_grabbing()
        self.camera_thread = cameraThread( self.camera )
        self.camera_thread.connect_success_grab_to_function(self.grabbed_image_interrupt)
        self.camera_thread.start_thread()


