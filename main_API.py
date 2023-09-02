import cv2

from Camera import dorsaPylon, PylonFlags
from Camera.dorsaPylon import Collector, Camera
from Camera.cameraThread import cameraThread
from Database.mainDatabase import mainDatabase
#Import Pages Ui---------------------------------------------
from PagesAPI.settingPageAPI import settingPageAPI
from PagesAPI.usersPageAPI import usersPageAPI
from PagesAPI.mainPageAPI import mainPageAPI
from PagesAPI.gradingRangesPageAPI import gradingRangesPageAPI
from PagesAPI.reportPageAPI import reportPageAPI
from PagesAPI.reportsPageAPI import reportsPageAPI
from PagesAPI.comparePageAPI import comparePageAPI
#------------------------------------------------------------
#from main_UI import mainUI
#------------------------------------------------------------
from backend.Processing.Report import Report
from backend.Processing.Compare import Compare
# from settingUI import settingUI
import CONSTANTS
import pickle

cameras_serial_number = {'standard': '23804186'}
class main_API:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.db = mainDatabase()
        self.cameras = {}
        self.creat_camera()
        self.run_camera_grabbing()

        #Pages_api------------------------------------
        self.mainPageAPI = mainPageAPI(ui= self.ui.mainPage, cameras = self.cameras, database = self.db)
        self.gradingRangesPageAPI = gradingRangesPageAPI(ui = self.ui.gradingRange, database = self.db.grading_ranges_db)
        self.settingPageAPI = settingPageAPI( ui = self.ui.settingPage, camera = self.cameras, database = self.db.setting_db )
        self.usersPageAPI = usersPageAPI(ui= self.ui.usersPage, database = self.db.users_db)
        self.reportPageAPI = reportPageAPI(ui = self.ui.reportPage)
        self.reportsPageAPI = reportsPageAPI(ui=self.ui.reportsPage, database=self.db)
        self.comparePageAPI = comparePageAPI(ui=self.ui.comparePage, database=self.db)

        self.ui.change_page_connector(self.page_change)
        self.usersPageAPI.set_login_event(self.login_user_event)
        self.mainPageAPI.set_report_button_event_func(self.show_report_event)
        self.reportsPageAPI.set_see_report_event_func(self.show_report_event)
        self.reportPageAPI.set_back_event_func(self.change_page)
        self.comparePageAPI.set_back_event_func(self.change_page)
        self.reportsPageAPI.set_compare_event_func(self.show_compare)
        self.gradingRangesPageAPI.set_new_standard_event_func( self.standard_event )
        self.gradingRangesPageAPI.set_remove_standard_event_func( self.standard_event )

        #this functions should run when each page load
        self.pages_api_dict = {
            'main': None,
            'reports': self.reportsPageAPI,
            'grading_ranges': None,
            'calibration': None,
            'settings': self.settingPageAPI,
            'user': None,
            'help': None,
            'report': None,
            'compare': None,
        }

        #TEMP
        self.login_user_event()
        self.standard_event()
        #---------------------------------------------------
        #report = load_obj('test_report')
        #self.show_report(report, 'main')
        #self.show_compare(None)
        
    
    def page_change(self, pagename, idx):
        for camera in self.cameras.values():
            camera.Operations.stop_grabbing()

        #call startup method of API of corespond page
        if self.pages_api_dict[pagename] is not None:
            self.pages_api_dict[pagename].startup()

    def grabbed_image_interrupt(self,):
        current_page,_ = self.ui.get_current_page()
        
        if current_page == 'main':
            self.mainPageAPI.process_image()
        elif current_page == 'settings':
            self.settingPageAPI.cameraSetting.show_live_image()
        

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
        role = self.usersPageAPI.data_passer.get_logined_user_role()
        username = self.usersPageAPI.data_passer.logined_user.get('username', '')
        self.set_access(role)
        self.mainPageAPI.set_logined_user(username)


    def standards_changed_event(self,):
        pass
    
    def set_access(self, role):
        self.ui.set_access_pages( CONSTANTS.ACCESS[role]['pages'],)
        self.ui.set_access_tabs( CONSTANTS.ACCESS[role]['tabs'])


    def show_report_event(self, report:Report, master_page:str ):
        """open Report Page and Pass Report to its API

        Args:
            report (Report): _description_
        """
        self.reportPageAPI.set_master_page(master_page)
        self.reportPageAPI.set_report(report)
        self.ui.go_to_page('report')


    def change_page(self, page_name):
        self.ui.go_to_page(page_name)

    def show_compare(self, compare:Compare):
        #compare = __load_obj__('test')
        self.ui.go_to_page('compare')
        self.comparePageAPI.set_compare_data(compare)

    def standard_event(self,): 
        """this event happend when a new standard define or remove
        """
        standars = self.db.grading_ranges_db.load_all()
        standars_name = list(map( lambda x:x['name'], standars))
        self.settingPageAPI.sampleSetting.set_standards(standars_name)

