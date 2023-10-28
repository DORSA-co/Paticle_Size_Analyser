#from PySide6.QtCore import QObject
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal, QMutex, QObject
from backend.Camera.dorsaPylon import Camera, Collector
import cv2
import time

class cameraWorker(QObject):
    success_grab_signal = Signal()
    finished = Signal()

    def __init__(self, camera):
        super().__init__()
        self.camera:Camera = camera
        self.grabbing = True
        self.new_camera = None

    
    def stop(self,):
        self.grabbing = False
    
    def grabber(self,):
        t = 0
        while self.grabbing:

            # if t%500 == 0:
            #     print('while')
            #     print(self.camera.Status.is_open())
            #     print(self.camera.Infos.get_model())
            # t+=1
            # time.sleep(0.002)

            try:
                if self.camera.Status.is_grabbing():
                    img = self.camera.getPictures(img_when_error=None)
                    if img is not None:
                        self.success_grab_signal.emit()
                
                

            except Exception as e:
                print('camera Error happend in thread while !', e)
        print('end of Camra Thread While')
        self.finished.emit()





class DeviceCheckerWorker(QObject):
    finished = Signal()

    serials_ready = Signal()
    def __init__(self, collector: Collector) -> None:
        self.collector = collector
        super().__init__()

    def serial_number_finder(self):
        for i in range(1):
            self.available_serials = self.collector.get_all_serials()
            # self.serials_ready.emit()
        self.finished.emit()

    def get_available_serials(self):
        return self.available_serials