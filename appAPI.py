import cv2
from PySide6.QtCore import QThread, QObject
from datetime import datetime

from backend.Camera import dorsaPylon, PylonFlags
from backend.Camera.dorsaPylon import Collector, Camera
from backend.Camera.cameraThread import cameraWorker
from Database.mainDatabase import mainDatabase
#Import Pages Ui---------------------------------------------
from PagesAPI.settingPageAPI import settingPageAPI
from PagesAPI.usersPageAPI import usersPageAPI
from PagesAPI.mainPageAPI import mainPageAPI
from PagesAPI.standardsPageAPI import standardsPageAPI
from PagesAPI.reportPageAPI import reportPageAPI
from PagesAPI.reportsPageAPI import reportsPageAPI
from PagesAPI.comparePageAPI import comparePageAPI
from PagesAPI.validationPageAPI import validationPageAPI
#------------------------------------------------------------
#from main_UI import mainUI
#------------------------------------------------------------
from backend.Processing.Report import Report
from backend.Processing.Compare import Compare
#------------------------------------------------------------
from backend.miniApps.storageCleaner import storageCleaner
import CONSTANTS
from PagesUI.PageUI import commonUI
from appUI import mainUI
#from PySide6.QtCore import QTimer

cameras_serial_number = {'standard': '23804186'}
class main_API(QObject):
    def __init__(self, ui:mainUI) -> None:
        self.ui = ui
        self.db = mainDatabase()

        #handle database Error
        if not self.db.dbManager.check_connection():
            self.ui.show_confirm_box('Error', 'database connection error', buttons=['ok'])
            self.ui.close(True)
        

        self.cameras = {}
        self.creat_camera()
        self.run_camera_grabbing()
        self.db.build()

        #apps-----------------------------------------
        self.storageCleanerApp = storageCleaner( settings= self.db.setting_db.storage_db.load(),
                                                reports_db= self.db.reports_db
                                                )
        self.storageCleanerApp.run()
        print(f'{self.storageCleanerApp.removed_counter} samples removed')

        #Pages_api------------------------------------
        self.mainPageAPI = mainPageAPI(ui= self.ui.mainPage, cameras = self.cameras, database = self.db)
        self.gradingRangesPageAPI = standardsPageAPI(ui = self.ui.gradingRange, database = self.db.standards_db)
        self.settingPageAPI = settingPageAPI( ui = self.ui.settingPage, cameras = self.cameras, database = self.db.setting_db )
        self.usersPageAPI = usersPageAPI(ui= self.ui.usersPage, database = self.db.users_db)
        self.reportPageAPI = reportPageAPI(ui = self.ui.reportPage, database=self.db)
        self.reportsPageAPI = reportsPageAPI(ui=self.ui.reportsPage, database=self.db)
        self.comparePageAPI = comparePageAPI(ui=self.ui.comparePage, database=self.db)
        self.validationPageAPI = validationPageAPI(ui=self.ui.validationPage, database=self.db)

        #events----------------------------------------------
        self.ui.change_page_connector(self.page_change_event)
        self.usersPageAPI.set_login_event(self.login_user_event)
        self.mainPageAPI.set_report_button_event_func(self.show_report_event)
        self.reportsPageAPI.set_see_report_event_func(self.show_report_event)
        self.reportPageAPI.set_back_event_func(self.change_page)
        self.comparePageAPI.set_back_event_func(self.change_page)
        self.reportsPageAPI.set_compare_event_func(self.show_compare_event)
        self.gradingRangesPageAPI.set_new_standard_event_func( self.standard_event )
        self.gradingRangesPageAPI.set_remove_standard_event_func( self.standard_event )




        #this functions should run when each page load
        self.pages_startups = {
            'main': self.mainPageAPI,
            'reports': self.reportsPageAPI,
            'grading_ranges': None,
            'calibration': self.validationPageAPI,
            'settings': self.settingPageAPI,
            'user': None,
            'help': None,
            'report': None,
            'compare': None,
        }


        self.pages_endup = {
            'main': self.mainPageAPI,
            'reports': None,
            'grading_ranges': self.gradingRangesPageAPI,
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

        

    def creat_camera(self)-> Camera:

        for camera_application, serial_number in cameras_serial_number.items():
            collector = Collector()
            camera = collector.get_camera_by_serial(serial_number)
        
            if camera is None:
                #self.mainPageAPI
                collector.enable_camera_emulation(1)
                camera = collector.get_all_cameras(camera_class=PylonFlags.CamersClass.emulation)[0]
        
            camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)
            
            self.cameras[camera_application] = camera


    def run_camera_grabbing(self,):

        self.camera_workers = {}
        self.cam_threads = {}
        for camera_name, camera in self.cameras.items():
            camera.Operations.open()

            self.camera_workers[camera_name] = cameraWorker( camera )
            self.cam_threads[camera_name] = QThread()
            self.camera_workers[camera_name].moveToThread( self.cam_threads[camera_name] )
            self.cam_threads[camera_name].started.connect( self.camera_workers[camera_name].grabber )
            self.camera_workers[camera_name].success_grab_signal.connect(self.grabbed_image_event)
            self.cam_threads[camera_name].start()


    #_________________________________________________________________________________________________________________________
    #
    #
    #_________________________________________________________________________________________________________________________

    def page_change_event(self, current_page_name, new_page_name):

        #call startup method of API of corespond page
        change_Page_permition = True
        if self.pages_endup[current_page_name] is not None:
            #call endup function of each page for do some stuff and check permition for change page
            change_Page_permition = self.pages_endup[current_page_name].endup()

        #check that previous page accepts changing page
        if change_Page_permition:
            if self.pages_startups[new_page_name] is not None:
                self.pages_startups[new_page_name].startup()
        
            self.ui.go_to_page(new_page_name)
        


    def grabbed_image_event(self,):
        current_page,_ = self.ui.get_current_page()
        
        if current_page == 'main':
            self.mainPageAPI.process_image()
        elif current_page == 'settings':
            self.settingPageAPI.cameraSetting.show_live_image()
        


    def login_user_event(self,):
        role = self.usersPageAPI.data_passer.get_logined_user_role()
        username = self.usersPageAPI.data_passer.logined_user.get('username', '')
        self.set_access(role)
        self.mainPageAPI.set_logined_user(username)
        self.reportsPageAPI.set_user_login(username)


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

    def show_compare_event(self, compare:Compare):
        """this event happend when compare button in reports page clicked

        Args:
            compare (Compare): _description_
        """
        #compare = __load_obj__('test')
        self.ui.go_to_page('compare')
        self.comparePageAPI.set_compare_data(compare)

    def standard_event(self,): 
        """this event happend when a new standard define or remove
        """
        standars = self.db.standards_db.load_all()
        standars_name = list(map( lambda x:x['name'], standars))
        self.settingPageAPI.sampleSetting.set_standards_event(standars_name)

