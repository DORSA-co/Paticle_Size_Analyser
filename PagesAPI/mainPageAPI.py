from dorsaPylon import Collector

from PagesUI.mainPageUI import mainPageUI
from Database.mainDatabase import mainDatabase
import CONSTANTS
#from main_UI import routerUI
from uiUtils import GUIComponents
from backend.Camera import dorsaPylon

class mainPageAPI:

    def __init__(self, ui:mainPageUI, cameras:dorsaPylon, database:mainDatabase, ):
        self.ui = ui
        self.database = database
        self.cameras = cameras
    
        self.warning_checker_timer = GUIComponents.timerBuilder(1000, self.check_warnings)
        self.warning_checker_timer.start()

        self.ui.player_buttons_connect('fast_start', self.fast_start)


    def check_warnings(self,):
        #print('checkwarning')
        pass

    def process_image(self):
        img = 0 
        print('s')

    
    def fast_start(self,):
        for camera in self.cameras.values():
            camera.Operations.start_grabbing()