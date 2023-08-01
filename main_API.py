import cv2

from Camera import dorsaPylon, PylonFlags
from Camera.dorsaPylon import Collector, Camera
from Camera.cameraThread import cameraThread
from Database.mainDatabase import mainDatabase
#Import Pages Ui---------------------------------------------
from settingPageAPI import settingPageAPI
from usersPageAPI import usersPageAPI
from mainPageAPI import mainPageAPI
# from settingUI import settingUI
import CONSTANTS

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
        self.gradingAPI = mainPageAPI(ui= self.ui.mainPage, cameras = self.cameras, database = self.db)

        self.ui.change_page_connector(self.page_change)
        self.usersAPI.set_login_event(self.login_user_event)

        #this functions should run when each page load
        self.pages_api_dict = {
            'main': None,
            'report': None,
            'calibration': None,
            'settings': self.settingAPI,
            'user': None,
            'help': None,
        }

        #TEMP
        self.login_user_event()
        
    
    def page_change(self, pagename, idx):
        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()

        #call startup method of API of corespond page
        if self.pages_api_dict[pagename] is not None:
            self.pages_api_dict[pagename].startup()

    def grabbed_image_interrupt(self,):
        current_page,_ = self.ui.get_current_page()
        
        if current_page == 'main':
            self.gradingAPI.process_image()
        elif current_page == 'settings':
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



    def login_user_event(self,):
        role = self.usersAPI.data_passer.get_logined_user_role()
        self.set_access(role)
    
    def set_access(self, role):
        self.ui.set_access_pages( CONSTANTS.ACCESS[role]['pages'],)
        self.ui.set_access_tabs( CONSTANTS.ACCESS[role]['tabs'])

