import time

from PySide6.QtCore import QObject, Signal


class timerThread(QObject):
    finish_signal = Signal()
    counter_signal = Signal(int)

    def __init__(self, t:int, sleep_time=1, name='') -> None:
        super().__init__()
        self.time = t
        self.sleep_time = sleep_time
        self.name = name
    

    def run_single(self,):
        start_time = time.time()
        pass_time = 0
        while  pass_time < self.time:
            time.sleep(self.sleep_time)
            pass_time = time.time() - start_time
            pass_time*=5
            self.counter_signal.emit( pass_time )
            print(pass_time, self.name)

        self.finish_signal.emit()

    
    def run_loop(self,):
        while True:
            start_time = time.time()
            t = start_time
            
            while  t - start_time < self.time:
                time.sleep(self.sleep_time)
                t = time.time()

            self.finish_signal.emit()




class timoutTimerWorker(QObject):
    timeout_signal = Signal()

    def __init__(self, timout, sleep_time = 0.1) -> None:
        super().__init__()
        self.__timeout = timout
        self.running = True
        self.sleep_time = sleep_time

    def stop(self,):
        self.running = False
        
    def run(self,):
        start_time = time.time()
        pass_time = 0
        while  self.running:
            if pass_time > self.__timeout:
                self.timeout_signal.emit()
                break
            
            time.sleep(self.sleep_time)
            pass_time = (time.time() - start_time) * 1000
            

        