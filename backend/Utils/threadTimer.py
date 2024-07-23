import time

from PySide6.QtCore import QObject, Signal


class timerThread(QObject):
    finish_signal = Signal()
    def __init__(self, t:int, sleep_time=1) -> None:
        super().__init__()
        self.time = t
        self.sleep_time = sleep_time
        
    def run_single(self,):
        start_time = time.time()
        t = start_time
        while  t - start_time < self.time:
            time.sleep(self.sleep_time)
            t = time.time()

        self.finish_signal.emit()

    
    def run_loop(self,):
        while True:
            start_time = time.time()
            t = start_time
            
            while  t - start_time < self.time:
                time.sleep(self.sleep_time)
                t = time.time()

            self.finish_signal.emit()