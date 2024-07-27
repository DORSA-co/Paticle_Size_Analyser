import time

from PySide6.QtCore import QObject, Signal


class timerThread(QObject):
    finish_signal = Signal()
    counter_signal = Signal(int)

    def __init__(self, t:int, sleep_time=1) -> None:
        super().__init__()
        self.time = t
        self.sleep_time = sleep_time
        
    def run_single(self,):
        start_time = time.time()
        pass_time = 0
        while  pass_time < self.time:
            time.sleep(self.sleep_time)
            pass_time = time.time() - start_time
            pass_time*=10
            self.counter_signal.emit( pass_time )

        self.finish_signal.emit()

    
    def run_loop(self,):
        while True:
            start_time = time.time()
            t = start_time
            
            while  t - start_time < self.time:
                time.sleep(self.sleep_time)
                t = time.time()

            self.finish_signal.emit()