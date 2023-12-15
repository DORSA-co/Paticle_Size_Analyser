import time

import numpy as np
from PySide6 import QtCore

from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from backend.Utils.datetimeUtils import datetimeFormat
from Constants import CONSTANTS

import threading

class Point2D:
    ui_path = 'uiFiles\\point2d.ui'
    

    def __init__(self, parent=None) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path, parent)

        self.close_timer = threadTimer()

        self.title_labels = {
            'x': self.ui.x_title,
            'y': self.ui.y_title,
        }

        self.value_labels = {
            'x': self.ui.x_value,
            'y': self.ui.y_value,
        }
        
        GUIBackend.set_win_frameless(self.ui)
        
        
    def set_titles(self, x_title, y_title):
        GUIBackend.set_label_text(self.title_labels['x'], x_title)
        GUIBackend.set_label_text(self.title_labels['y'], y_title)

    def set_value(self, name:str, value, after:str=None, befor:str=None):
        value = np.round(value, CONSTANTS.DECIMAL_ROUND)
        value = str(value)
        if befor is not None:
            value = befor + ' ' + value

        if after is not None:
            value = value + ' ' + after
        GUIBackend.set_label_text(self.value_labels[name], value)


    def show(self, timeup):
        GUIBackend.show_window(self.ui, True)
        self.close_timer.set_timeup(timeup)
        if self.close_timer.is_running:
            self.close_timer.reset()
        
        else:
            thread = threading.Thread(target=self.close_timer.run)
            self.close_timer.finished.connect(self.close)
            thread.start()
            

    
    def close(self):
        GUIBackend.close_window(self.ui)

    def hide(self,):
        GUIBackend.hide_window(self.ui)




    
class threadTimer(QtCore.QObject):
    finished = QtCore.Signal()

    def __init__(self,timeup=2000) -> None:
        super(threadTimer, self).__init__()
        self.start_time = 0
        self.timeup = timeup
        self.is_running = False
    
    def set_timeup(self, timeup):
        self.timeup = timeup
    
    def run(self,):
        self.start_time = time.time()
        while True:
            self.is_running = False
            duration_ms = (time.time() - self.start_time) * 1000
            #delay 100ms more to have time for reset timer
            if duration_ms > (self.timeup + 100):
                self.is_running = False
                break

            time.sleep(0.05)
        
        
        self.finished.emit()

    def reset(self,):
        self.start_time = time.time()
