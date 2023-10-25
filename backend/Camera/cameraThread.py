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
        super().__init__()
        self.camera:Camera = camera
        #self.func = None
        #self.thread = None
        self.grabbing = True
        self.new_camera = None

    # def change_camera(self,camera):
    #     self.new_camera = camera
    
    def stop(self,):
        self.grabbing = False
    
    def grabber(self,):
        print('grabb start in wordker')
        t=0
        #while not self.stop_flag:
        while self.grabbing:

            if t%500 == 0:
                print('while') 
            t+=1
            # if t>1000:
            #     self.grabbing = False
            #print('camera while')
            time.sleep(0.002)
            
            # if self.stop_flag:
            #     print('stop grabbing')
            #     break
            # if self.new_camera is not None:
            #     self.camera = self.new_camera
            #     self.new_camera = None
            #print('while is running')
            
            try:
                if self.camera.Status.is_grabbing():
                    img = self.camera.getPictures(img_when_error=None)
                    if img is not None:
                        self.success_grab_signal.emit()
                
                

            except Exception as e:
                print('camera Error happend in thread while !', e)
        print('end of While')
        self.finished.emit()