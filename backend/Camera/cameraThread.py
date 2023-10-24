#from PySide6.QtCore import QObject
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal, QMutex, QObject
from backend.Camera.dorsaPylon import Camera
import cv2
import time

class cameraWorker(QObject):
    success_grab_signal = Signal()
    finished = Signal()

    def __init__(self, camera):
        super(cameraWorker,self).__init__()
        self.camera:Camera = camera
        #self.func = None
        #self.thread = None
        self.stop_flag = False
    
    def stop(self,):
        self.stop_flag = True
    
    def grabber(self,):
        while True:
            if self.stop_flag:
                break
            #print('while is running')
            try:
                print(self.camera.Infos.get_model())
                if self.camera.Status.is_grabbing():
                    img = self.camera.getPictures(img_when_error=None)
                    if img is not None:
                        self.success_grab_signal.emit()
                time.sleep(0.1)
                

            except Exception as e:
                print('camera Error happend in thread while !', e)
        
        self.finished.emit()