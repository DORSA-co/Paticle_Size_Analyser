import cv2

from Camera import dorsaPylon, PylonFlags
from Camera.dorsaPylon import Collector, Camera
from Camera.cameraThread import cameraThread
from Database.mainDatabase import mainDatabase
#Import Pages Ui---------------------------------------------
from settingPageAPI import settingPageAPI
from usersPageAPI import usersPageAPI
# from settingUI import settingUI

cameras_serial_number = {'standard': '23804186'}
class main_API:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.db = mainDatabase()
        self.cameras = {}
        self.creat_camera()
        self.run_camera_grabbing()

        #Pages_api------------------------------------
        self.settingAPI = settingPageAPI( ui = self.ui.settingPage, camera = self.cameras, database = self.db.setting_db )
        self.usersAPI = usersPageAPI(ui= self.ui.usersPage, database = self.db.users_db)

        
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
        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()

        #call startup method of API of corespond page
        if self.pages_api_dict[pagename] is not None:
            self.pages_api_dict[pagename].startup()

    def grabbed_image_interrupt(self,):
        self.settingAPI.cameraSetting.show_live_image()

    def creat_camera(self)-> Camera:

        for camera_application, serial_number in cameras_serial_number.items():
            collector = Collector()
            camera = collector.get_camera_by_serial(serial_number)
        
            if camera is None:
                collector.enable_camera_emulation(1)
                camera = collector.get_all_cameras(camera_class=PylonFlags.CamersClass.emulation)[0]
        
            camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)
            
            self.cameras[camera_application] = camera

    def run_camera_grabbing(self,):
        
        for camera in self.cameras.values():
            camera.Operations.open()
        
            #self.camera.Operations.start_grabbing()
            self.camera_thread = cameraThread( camera )
            self.camera_thread.connect_success_grab_to_function(self.grabbed_image_interrupt)
            self.camera_thread.start_thread()


