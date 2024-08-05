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
        self.__start_time = 0
        self.__running_flag = True

    
    def stop(self,):
        self.__running_flag = False


    

    def run_single(self,):
        self.__running_flag = True
        self.__start_time = time.time()
        pass_time = 0
        while  pass_time < self.time:
            time.sleep(self.sleep_time)
            pass_time = time.time() - self.__start_time
            pass_time*=5
            self.counter_signal.emit( pass_time )
            if not self.__running_flag:
                break
        
        if self.__running_flag:
            self.finish_signal.emit()

    
    def run_loop(self,):
        while True:
            self.__running_flag = True
            self.__start_time = time.time()
            pass_time = 0
            while  pass_time < self.time:
                time.sleep(self.sleep_time)
                pass_time = time.time() - self.__start_time
                pass_time*=5
                self.counter_signal.emit( pass_time )
                if not self.__running_flag:
                    break
        
            if self.__running_flag:
                self.finish_signal.emit()


    def reset(self,):
        self.__start_time = time.time()



class recurringThreadTimer(QObject):
    finish_signal = Signal()
    counter_signal = Signal(int)

    def __init__(self,recurring_timer , limit_timer=0, sleep_time=1, name='') -> None:
        assert limit_timer > recurring_timer or limit_timer==0, "limit timer should be greater than recurring_timer"
        super().__init__()
        
        self.name = name
        self.recurring_timer = recurring_timer
        self.limit_timer = limit_timer
        self.sleep_time = sleep_time
        self.__start_time = 0
        self.__running_flag = True


    def run_single(self,):
        self.__start_time = time.time()
        pass_time = 0
        total_pass_time = 0
        self.__running_flag = True
        self.__start_time_fix = self.__start_time

        while  pass_time < self.recurring_timer:
            print(pass_time, total_pass_time)
            time.sleep(self.sleep_time)
            t = time.time()
            total_pass_time = t - self.__start_time_fix
            pass_time = t - self.__start_time

            self.counter_signal.emit( total_pass_time )
            if not self.__running_flag:
                #break and no emit signal
                break

            if self.limit_timer!=0 and total_pass_time > self.limit_timer:
                #break and emit signal
                break
        
        if self.__running_flag:
            self.finish_signal.emit()

    def stop(self,):
        self.__running_flag = False


    def recurring(self,):
        self.__start_time = time.time()


# class timoutTimerWorker(QObject):
#     timeout_signal = Signal()

#     def __init__(self, timout, sleep_time = 0.1) -> None:
#         super().__init__()
#         self.__timeout = timout
#         self.running = True
#         self.sleep_time = sleep_time

#     def stop(self,):
#         self.running = False
        
#     def run(self,):
#         start_time = time.time()
#         pass_time = 0
#         while  self.running:
#             if pass_time > self.__timeout:
#                 self.timeout_signal.emit()
#                 break
            
#             time.sleep(self.sleep_time)
#             pass_time = (time.time() - start_time) * 1000
            

        