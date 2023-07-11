sys.path.append( os.getcwd() + "/pages_UI" )
from setting_UI import settingUI

class settingAPI:

    def __init__(self, ui: settingUI ,db, camera):
        self.ui = ui
        self.db = db
        self.camera = camera


    def update_camera_setting():
        settings = self.ui.get_settings()
        self.camera.set_gain( settings['gain'] )