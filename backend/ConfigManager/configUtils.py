from backend.ConfigManager import configFlags

class configUtils:

    @staticmethod
    def check_signals(self, conds:list[dict], values:dict ) -> bool:
        #{'name': 'r1', 'condition': 'true', 'value': 0.0},
        final_res = True
        log = []

        for signal_cond in conds:

            name = signal_cond['name']
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
                     'value': value}
                )
        
        
        return final_res, log
    



    def get_write_signal_dict(self, signals:list[dict]) -> dict:
        res = {}
        for signal in signals:
            name = signal['name']
            value = signal['value']
            stype = signal['type']
            if stype == 'bool':
                if value =='true':
                    value = True
                else:
                    value = False
            else:
                value = float(value)

            res[name] = value
        return res