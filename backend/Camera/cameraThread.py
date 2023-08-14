from PySide6.QtCore import QObject
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal
import cv2
import time

class cameraThread(QObject):
    success_grab_signal = Signal()

    def __init__(self, camera):
        super(cameraThread,self).__init__()
        self.camera = camera
        self.func = None
        self.thread = None
    
    def __grabber__(self,):
        while True:
            #print('while is running')
            try:
                if self.camera.Status.is_grabbing():
                    img = self.camera.getPictures(img_when_error=None)
                    if img is not None:
                        self.success_grab_signal.emit()
                time.sleep(0.01)

            except:
                print('camera Error happend in thread while !')
            
    def connect_success_grab_to_function(self, func):
        self.func = func
    
    def start_thread(self,):
        self.thread = QThread()
        self.moveToThread( self.thread )
        self.thread.started.connect( self.__grabber__ )
        self.success_grab_signal.connect(self.func)
        self.thread.start()


# class cameraThreadHandler:

#     def __init__(self):


#     def start(self,):
#         cth = cameraThread(cam)
#         thread = QThread()
#         cth.moveToThread(thread)
#         cth.success_grab_signal.connect(test)
#         thread.start()