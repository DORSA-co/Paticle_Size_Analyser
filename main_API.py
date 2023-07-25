import cv2

from Camera import dorsaPylon, PylonFlags
from Camera.dorsaPylon import Collector, Camera
from Camera.cameraThread import cameraThread
from Database.mainDatabase import mainDatabase
#Import Pages Ui---------------------------------------------
from settingPageAPI import settingPageAPI
# from settingUI import settingUI

serial_number = '23804186'
class main_API:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.db = mainDatabase()
        self.camera = None
        self.creat_camera()
        self.run_camera_grabbing()

        #Pages_api------------------------------------
        self.settingAPI = settingPageAPI( ui = self.ui.settingPage, camera = self.camera, database = None )
        self.ui.__global_setting__.change_page_connector(self.page_change)

        #this functions should run when each page load
        self.pages_api_dict = {
            'main': None,
            'report': None,
            'calibration': None,
            'settings': self.settingAPI,
            'user': None,
            'help': None,
            

        }


        #------pages_API--------
        # self.setting_api = settingAPI( settingUI  )
    
    def page_change(self, pagename, idx):
        print(pagename, idx)
        #stop camera
        self.camera.Operations.stop_grabbing()
        #call startup method of API of corespond page
        if self.pages_api_dict[pagename] is not None:
            self.pages_api_dict[pagename].startup()

    def grabbed_image_interrupt(self,):
        img = self.camera.image
        #color_imgage = cv2.cvtColor(img , cv2.COLOR_GRAY2RGB )

        self.settingAPI.cameraSetting.show_live_image(img)

    def creat_camera(self)-> Camera:
        collector = Collector()
        self.camera = collector.get_camera_by_serial(serial_number)
        if self.camera is None:
            collector.enable_camera_emulation(1)
            self.camera = collector.get_all_cameras(camera_class=PylonFlags.CamersClass.emulation)[0]
        
        self.camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)

    def run_camera_grabbing(self,):
        self.camera.Operations.open()
        #self.camera.Operations.start_grabbing()
        self.camera_thread = cameraThread( self.camera )
        self.camera_thread.connect_success_grab_to_function(self.grabbed_image_interrupt)
        self.camera_thread.start_thread()


