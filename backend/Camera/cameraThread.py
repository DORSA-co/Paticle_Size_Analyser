#from PySide6.QtCore import QObject
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal, QMutex, QObject
import cv2
import time

class cameraWorker(QObject):
    success_grab_signal = Signal()
    finish = Signal()

    def __init__(self, camera):
        super(cameraWorker,self).__init__()
        self.camera = camera
        #self.func = None
        #self.thread = None
    
    def grabber(self,):
        while True:
            #print('while is running')
            try:
                if self.camera.Status.is_grabbing():
                    img = self.camera.getPictures(img_when_error=None)
                    if img is not None:
                        self.success_grab_signal.emit()
                time.sleep(0.1)
                

            except Exception as e:
                print('camera Error happend in thread while !', e)
