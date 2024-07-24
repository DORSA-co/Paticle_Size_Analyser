import time
import os

from PySide6.QtCore import QThread
from PySide6.QtCore import Signal, QMutex, QObject
import cv2
import numpy as np

from backend.Camera.dorsaPylon import Camera, Collector
import Constants.CONSTANTS as CONSTANTS



def DemoImageLoaderMemory(path):
        files = []
        if os.path.exists(path):
            files = sorted(os.listdir(path))
        files.reverse()
        total_count = len(files)
        start_idx = 70
        while True:
            total_range = list(range(start_idx, total_count)) + list(range(0,start_idx))
            for i in total_range:
                fpath = os.path.join(path, files[i])
                t = time.time()
                yield cv2.imread(fpath,0)
                print(time.time() - t)


def DemoImageLoaderRAM(path):
        files = []
        if os.path.exists(path):
            files = sorted(os.listdir(path))
        files.reverse()
        total_count = len(files)
        start_idx = 0
        imgs = []

        total_range = list(range(start_idx, total_count)) + list(range(0,start_idx))
        for i in total_range:
            fpath = os.path.join(path, files[i])
            imgs.append(cv2.imread(fpath,0))

        while True:
            for i in range(len(imgs)):
                yield imgs[i]



class cameraWorker(QObject):
    success_grab_signal = Signal(np.ndarray)
    grabb_image_error = Signal()
    finished = Signal()

    


    def __init__(self, camera:Camera, timeout = 2000):
        super().__init__()
        self.camera:Camera = camera
        self.grabbing = True
        self.new_camera = None
        self.timeout = timeout

        self.handle_simulation_camera(camera)


    def handle_simulation_camera(self,camera:Camera):
        if camera.Infos.is_Simulation():
            self.simulation = True
            self.demoImageLoader = DemoImageLoaderRAM(CONSTANTS.Files.DEMO_IMGS_DIR)
        else:
            self.simulation = False
            self.demoImageLoader = None


    def change_camera(self, new_camera):
        self.new_camera = new_camera

    # def stop(self,):
    #     self.grabbing = False
    
    def grabber(self,):
        # t = 0
        self.time = time.time()
        while self.grabbing:

            try:
                if self.new_camera:
                    self.camera = self.new_camera
                    self.new_camera = None
                    self.handle_simulation_camera(self.camera)

                if (time.time() - self.time) * 1000 > self.timeout:
                    self.grabb_image_error.emit()
                    self.time = time.time()

                if self.camera.Status.is_grabbing():
                    flag, img, status = self.camera.getPictures()
                    if self.simulation:
                        img = next(self.demoImageLoader)
                    if img is not None:
                        self.success_grab_signal.emit(img)
                        self.time = time.time()
                
                else:
                    self.time = time.time()

                
                
                

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
            try:
                self.available_serials = self.collector.get_all_serials()
                self.serials_ready.emit()
            except:
                self.available_serials = []
        self.finished.emit()

    def get_available_serials(self):
        return self.available_serials