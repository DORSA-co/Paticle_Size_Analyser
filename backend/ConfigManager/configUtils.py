import threading

from backend.ConfigManager import configFlags
from backend.Utils.threadTimer import timerThread


class configUtils:

    @staticmethod
    def check_signals( conds:list[dict], values:dict ) -> bool:
        #{'name': 'r1', 'condition': 'true', 'value': 0.0},
        final_res = True
        log = []

        for signal_cond in conds:

            name = signal_cond['name']
            _id = signal_cond['id']

            value = values.get(name)    
            res = True
            status = configFlags.signalStatus.ok


            if value is None:
                final_res = False
                res = False
                status = configFlags.signalStatus.none
                
                
            else:                    
                operator = signal_cond['condition']

                if operator == 'true':
                    if isinstance(value, bool):
                        if not value == True:
                            final_res = False
                            res = False
                            status = configFlags.signalStatus.not_pass_condition
                    else:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.wrong_type
                            
                    
                elif operator == 'false':
                    if isinstance(value, bool):
                        if not value == False:
                            final_res = False
                            res = False
                            status = configFlags.signalStatus.not_pass_condition
                    else:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.wrong_type
                            
                
                elif operator == '>':
                    if not value > signal_cond['value']:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.not_pass_condition
                        
                
                elif operator == '<':
                    if not value < signal_cond['value']:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.not_pass_condition
                        

                
                elif operator == '=':
                    if not value == signal_cond['value']:
                        final_res = False
                        res = False
                        status = configFlags.signalStatus.not_pass_condition
                        

            log.append(
                    {'name':name,
                     'result': res, 
                     'status':status,
                     'value': value,
                     'id': _id
                     }
                )
        
        
        return final_res, log
    



    def get_write_signal_dict( signals:list[dict]) -> dict:
        res = {}
        for signal in signals:
            name = signal['name']
            value = signal['value']
            stype = signal['dtype']
            if stype == 'bool':
                if value =='true':
                    value = True
                else:
                    value = False
            else:
                value = float(value)

            res[name] = value
        return res
    


    @staticmethod
    def print_function_name(func):
        def wrapper(*args, **kwargs):
            print(f"Function name: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    @staticmethod
    def callback_on_error(error_callback):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    print(f"Error occurred in pipeline: {e}.")
                    fallback_func = getattr(self, error_callback)
                    timer = timerThread(20)
                    timer.finish_signal.connect(fallback_func)
                    threading.Thread(target=timer.run_single).start()
                    
            return wrapper
        return decorator