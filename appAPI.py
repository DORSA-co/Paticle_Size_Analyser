import cv2
from PySide6.QtCore import QThread, QObject
import threading
from datetime import datetime
import time

from backend.Camera import dorsaPylon, PylonFlags
from backend.Camera.dorsaPylon import Collector, Camera
from backend.Camera.cameraThread import cameraWorker, DeviceCheckerWorker
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
from appUI import mainUI
from backend.PLC.PLCHandler import PLCHandler
#------------------------------------------------------------
#from main_UI import mainUI
#------------------------------------------------------------
from backend.Processing.Report import Report
from backend.Processing.Compare import Compare
#------------------------------------------------------------
from backend.miniApps.storageCleaner import storageCleaner
import Constants.CONSTANTS as CONSTANTS
from Mediator.mainMediator import Mediator
#from appUI import mainUI
from uiUtils import GUIComponents
from subPrograms.dbInit.dbInitAPI import dbInitAPI
from backend.Serial.armSerial import armSerial
from backend.ConfigManager.configManager import configManager
#cameras_serial_number = {'standard': '23804186'}
class main_API(QObject):
    DEBUG_PROCESS_THREAD = False
    def __init__(self, uiHandeler:mainUI) -> None:
        self.tflag = False
        self.uiHandeler = uiHandeler
        self.db = mainDatabase()
        db_status = self.db.connect()
        if not db_status:
            db_init = dbInitAPI()
            db_init.ui.show()
            return
            
        else:
            self.db.build()

        self.mediator = Mediator()
        self.mediator.set_main_api(self)

        self.configManager = configManager()

        self.checked_device_time = 0
        #------------------------------------------------------------------------------------------
        self.camera_device_info = {}
        self.cameras: dict[str, Camera] = {}
        self.camera_workers:dict[str, cameraWorker] = {}
        self.camera_threads:dict[str, threading.Thread]= {}
        #------------------------------------------------------------------------------------------
        plc_setting = self.db.setting_db.plc_db.load()
        self.plc = PLCHandler(plc_setting['ip'])
        self.plc.set_connected_event(self.plc_connect_event)
        self.plc.set_disconnected_event(self.plc_disconnected_event)
        self.define_nodes()
        # self.plc.nodesHandler.set_change_value_event(self.node_change_value_event)
        # self.plc.connect_request()
        

        self.collector = Collector()
        self.collector.enable_camera_emulation(1)
        self.camera_device_info = self.db.setting_db.camera_db.get_camera_devices()
        for cam_device_info in self.camera_device_info:
            self.creat_camera(cam_device_info)
            self.run_camera_grabbing(cam_device_info['application'])
        #-----------------------------------------------------------------------------------------
        

        self.is_during_checking_device = False
        self.device_checker_timer = GUIComponents.timerBuilder(1000, self.check_camera_devices_event)
        self.device_checker_timer.start()

        #micro serial---------------------------------
        self.serial_micro = armSerial()
        #apps-----------------------------------------
        self.storageCleanerApp = storageCleaner( settings= self.db.setting_db.storage_db.load(),
                                                reports_db= self.db.reports_db
                                                )
        self.storageCleanerApp.run()
        print(f'{self.storageCleanerApp.removed_counter} samples removed')

        #Pages_api------------------------------------
        #self.mainPageAPI = None
        self.mainPageAPI = mainPageAPI(uiHandeler= self.uiHandeler.mainPage, cameras = self.cameras, database = self.db)
        self.gradingRangesPageAPI = standardsPageAPI(ui = self.uiHandeler.gradingRange, database = self.db.standards_db)
        self.settingPageAPI = settingPageAPI( ui = self.uiHandeler.settingPage, cameras = self.cameras, database = self.db.setting_db , serial_micro=self.serial_micro)
        self.usersPageAPI = usersPageAPI(ui= self.uiHandeler.usersPage, database = self.db.users_db)
        self.reportPageAPI = reportPageAPI(uiHandeler = self.uiHandeler.reportPage, database=self.db)
        self.reportsPageAPI = reportsPageAPI(uiHandeler=self.uiHandeler.reportsPage, database=self.db)
        self.comparePageAPI = comparePageAPI(ui=self.uiHandeler.comparePage, database=self.db)
        self.validationPageAPI = validationPageAPI(ui=self.uiHandeler.validationPage, database=self.db, cameras=self.cameras)

        #for cam_device_info in cameras_serial_numbers:
            #self.creat_camera(cam_device_info)
            #self.run_camera_grabbing(cam_device_info['application'])

        #events----------------------------------------------
        self.uiHandeler.change_page_connector(self.page_change_event)
        self.usersPageAPI.set_login_event(self.login_user_event)
        self.mainPageAPI.set_report_button_event_func(self.show_report_event)
        self.reportsPageAPI.set_see_report_event_func(self.show_report_event)
        self.reportPageAPI.set_back_event_func(self.change_page)
        self.comparePageAPI.set_back_event_func(self.change_page)
        self.reportsPageAPI.set_compare_event_func(self.show_compare_event)
        self.gradingRangesPageAPI.set_new_standard_event_func( self.standard_event )
        self.gradingRangesPageAPI.set_remove_standard_event_func( self.standard_event )
        self.settingPageAPI.cameraSetting.set_camera_device_change_event(self.change_camera_device_event)
        self.settingPageAPI.plcSetting.set_external_plc_change_event(self.plc_setting_change_event)


        

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
        self.uiHandeler.show()
        self.uiHandeler.usersPage.loginUserBox.show_login()

        self.config_ui()
        print('__init__ appAPI finised')

    def define_nodes(self,):
        nodes_settings = self.db.setting_db.plc_nodes_db.load_all()
        for node_stng in nodes_settings:
            address = {'ns': node_stng['ns'],
                       'i': node_stng['i']
            }
            try:
                self.plc.nodesHandler.define_node(node_stng['name'], address=address)
            except Exception as e:
                print('Error define Node', address, e)


    def config_ui(self,):
        if not self.configManager.Config.can_start_manual():
            self.mainPageAPI.uiHandeler.hide_start_manual(True)
            
        
        if not self.configManager.Config.can_stop_manual():
            self.mainPageAPI.uiHandeler.hide_stop_manual(True)

        if not self.configManager.Config.has_plc():
            self.uiHandeler.hide_tab('plc_setting')
            

        

    def creat_camera(self, camera_device_info)-> Camera:
        cam_application = camera_device_info['application']
        serial_number = camera_device_info['serial_number']
        
        cameras_serial_number = self.collector.get_all_serials()
        
        if serial_number in cameras_serial_number:
            try:
                camera = self.collector.get_camera_by_serial(serial_number)
                camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)
                self.cameras[cam_application] = camera
            except:
                print('Camera serial number is not avaiable')
                # self.mainPageAPI.set_system_status('camera_connection', False)
        else:
            print('Camera serial number is not avaiable')
            # self.mainPageAPI.set_system_status('camera_connection', False)


    def run_camera_grabbing(self,camera_application): 
        if self.cameras.get(camera_application) is not None:
            self.cameras[camera_application].Operations.open()

            self.camera_workers[camera_application] = cameraWorker( self.cameras[camera_application] )
            self.camera_threads[camera_application] = threading.Thread(target=self.camera_workers[camera_application].grabber, daemon=True)
            self.camera_workers[camera_application].success_grab_signal.connect(self.grabbed_image_event)
            self.camera_workers[camera_application].grabb_image_error.connect(self.error_grab_image_event)

            self.camera_threads[camera_application].start()


    #_________________________________________________________________________________________________________________________
    #
    #
    #_________________________________________________________________________________________________________________________
    def change_camera_device_event(self, camera_device_info: dict):
        self.uiHandeler.change_cursure('wait')
        cam_application = camera_device_info['application']
        if self.cameras.get(cam_application) is not None:
            self.cameras[cam_application].Operations.close()
            time.sleep(0.5)
        
        #self.camera_device_info = self.c
        self.creat_camera(camera_device_info)
        self.settingPageAPI.cameraSetting.update_camera_event(self.cameras)

        if self.camera_workers.get(cam_application) is not None:
            self.camera_workers[cam_application].change_camera( self.cameras[cam_application] )
        else:
            self.run_camera_grabbing(cam_application)
        #self.camera_workers[cam_application].camera  = self.cameras[cam_application]
        self.uiHandeler.change_cursure(None)

    def check_camera_devices_event(self,):
        if not self.is_during_checking_device:
            self.checked_device_time = time.time()
            
            self.is_during_checking_device = True

            
            self.device_checker_worker = DeviceCheckerWorker(self.collector)
            self.device_checker_thread = threading.Thread(target= self.device_checker_worker.serial_number_finder)
            self.device_checker_worker.serials_ready.connect(self.refresh_camera_devices_event)
            self.device_checker_worker.finished.connect(self.finished_camera_devices_checking)
            if self.DEBUG_PROCESS_THREAD:
                print('Device Checker on Debug mode')
                self.device_checker_worker.serial_number_finder()
            else:
                self.device_checker_thread.start()

        else:
            if time.time() - self.checked_device_time  > CONSTANTS.TimeOut.TIMEOUT_CHECKING_DEVICE:
                self.is_during_checking_device = False
    
    
    def finished_camera_devices_checking(self,):
        self.is_during_checking_device = False


    def refresh_camera_devices_event(self):
        cameras_sn = self.device_checker_worker.get_available_serials()
        self.settingPageAPI.cameraSetting.set_devices(cameras_sn)
        if len(self.cameras) == 0:
            self.mainPageAPI.set_system_status('camera_connection', False)

        for device_info in self.camera_device_info:
            application = device_info['application']
            sn = device_info['serial_number']
            if self.cameras.get(application) is None:
                if sn in cameras_sn:
                    self.creat_camera(device_info)

        for cam_aplication, camera in self.cameras.items():
            if camera.Infos.get_serialnumber() not in cameras_sn:
                self.mainPageAPI.set_system_status('camera_connection', status=False)
                #self.camera_disconnect_event()
                
            else:
                self.mainPageAPI.set_system_status('camera_connection',status=True)


    def plc_connect_event(self,):
        pass
                
    def plc_disconnected_event(self,):
        pass

    # def node_change_value_event(self, data:dict):


    def page_change_event(self, current_page_name, new_page_name):

        if new_page_name in ['report']:
            self.uiHandeler.popupLoading.show()
        #call startup method of API of corespond page
        change_Page_permition = True
        if self.pages_endup[current_page_name] is not None:
            #call endup function of each page for do some stuff and check permition for change page
            change_Page_permition = self.pages_endup[current_page_name].endup()

        #check that previous page accepts changing page
        if change_Page_permition:
            if self.pages_startups[new_page_name] is not None:
                self.pages_startups[new_page_name].startup()
        
            self.uiHandeler.go_to_page(new_page_name)
        
        #if new_page_name in ['report']:
        self.uiHandeler.popupLoading.close()
        


    def grabbed_image_event(self, img):
        self.mainPageAPI.uiHandeler.set_warning_buttons_status('camera_grabbing', True)
        current_page,_ = self.uiHandeler.get_current_page()
        
        if current_page == 'main':
            self.mainPageAPI.process_image(img)

        elif current_page == 'settings':
            self.settingPageAPI.cameraSetting.show_live_image()
        
        elif current_page == 'calibration':
            self.validationPageAPI.calibrationTab.camera_image_event()
    
    def error_grab_image_event(self,):
        self.mainPageAPI.set_system_status('camera_grabbing', False)


    def login_user_event(self,):
        role = self.usersPageAPI.data_passer.get_logined_user_role()
        username = self.usersPageAPI.data_passer.logined_user.get('username', '')
        self.set_access(role)
        self.mainPageAPI.set_logined_user(username)
        self.reportsPageAPI.set_user_login(username)


    def standards_changed_event(self,):
        pass

    def plc_setting_change_event(self,):
        self.settingPageAPI.configSetting.load_singlas()
        
    
    def set_access(self, role):
        self.uiHandeler.set_access_pages( CONSTANTS.ACCESS[role]['pages'],)
        self.uiHandeler.set_access_tabs( CONSTANTS.ACCESS[role]['tabs'])


    def show_report_event(self, report:Report, master_page:str ):
        """open Report Page and Pass Report to its API

        Args:
            report (Report): _description_
        """
        self.reportPageAPI.set_master_page(master_page)
        self.reportPageAPI.set_report(report)
        self.uiHandeler.go_to_page('report')


    def change_page(self, page_name):
        self.uiHandeler.go_to_page(page_name)

    def show_compare_event(self, compare:Compare):
        """this event happend when compare button in reports page clicked

        Args:
            compare (Compare): _description_
        """
        #compare = __load_obj__('test')
        self.uiHandeler.go_to_page('compare')
        self.comparePageAPI.set_compare_data(compare)

    def standard_event(self,): 
        """this event happend when a new standard define or remove
        """
        standars = self.db.standards_db.load_all()
        standars_name = list(map( lambda x:x['name'], standars))
        self.settingPageAPI.sampleSetting.set_standards_event(standars_name)

