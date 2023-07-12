import sys, os
sys.path.append( os.getcwd() + "/backend" )
sys.path.append( os.getcwd() + "/PagesAPI" )
sys.path.append( os.getcwd() + "/PagesUI" )
import cv2

import dorsaPylon
from dorsaPylon import Collector, Camera
from cameraThread import cameraThread

#Import Pages Ui---------------------------------------------
from settingPageAPI import settingPageAPI
# from settingUI import settingUI

serial_number = '23804186'
class main_API:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.camera = None
        self.creat_camera()
        self.run_camera_grabbing()

        #Pages_api------------------------------------
        self.settingAPI = settingPageAPI( ui = self.ui.settingPage, camera = self.camera, database = None )
        


        #------pages_API--------
        # self.setting_api = settingAPI( settingUI  )

    def grabbed_image_interrupt(self,):
        img = self.camera.image
        img = cv2.resize(img, None, fx=0.20, fy=0.20)
        #cv2.imshow('img', img)
        #cv2.waitKey(30)
        color_imgage = cv2.cvtColor(img , cv2.COLOR_GRAY2RGB )
        self.settingAPI.cameraSetting.show_live_image(color_imgage)

    def creat_camera(self)-> Camera:
        collector = Collector()
        self.camera = collector.get_camera_by_serial(serial_number)
        self.camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)

    def run_camera_grabbing(self,):
        self.camera.Operations.open()
        #self.camera.Operations.start_grabbing()
        self.camera_thread = cameraThread( self.camera )
        self.camera_thread.connect_success_grab_to_function(self.grabbed_image_interrupt)
        self.camera_thread.start_thread()


