from backend.Processing.Report import Report


class RebuildReport:

    @staticmethod
    def rebuild( sample_record:dict, report:Report , new_standard:dict, grading_parm:str=None)-> tuple[dict, Report]:
        sample_record, report = RebuildReport.__change_standard__(sample_record, report, new_standard, grading_parm)
        return sample_record, report
        

    @staticmethod 
    def __change_standard__( sample_record:dict, report:Report, standard:dict , grading_parm:str=None) -> tuple[dict, Report]:
        report.rebuild(standard, grading_parm)
        sample_record['grading_result'] = report.Grading.get_hist()
        sample_record['standard'] = standard['name']

        return sample_record, report





class autoRebuildReport:

    def __init__(self, history:list[dict[dict]]) -> None:
        """
        Args:
            history (list[dict[dict]]): for exasmple [ {'old': {STANDARD DATABASE RECORD}, 'new':{STANDARD DATABASE RECORD} },  
                                                       {'old': {STANDARD DATABASE RECORD}, 'new':{STANDARD DATABASE RECORD} },
                                                        .
                                                        .
                                                        .
                                                        ]
        """
        self.__history__ = history
        self.__generate_converts__()
    

    def __generate_converts__(self,):
        
        self.converts = []
        while len(self.__history__):

            old = self.__history__[0]['old']
            new = self.__history__[0]['new']

            j = 1
            #check for sequance of related edit
            while j< len(self.__history__):
                
                #if name of a old standard in history is same as name if new standard 0th, they are related
                if self.__history__[j]['old']['name'] == new['name']:
                    new = self.__history__[j]['new']
                    self.__history__.pop(j)
                else:
                    j+=1
            
            self.converts.append({
                                'old': old,
                                'new': new
                            })

            self.__history__.pop(0)

    
    def is_need(self, all_samples)-> bool:
        """returns True if rebuiled needed
        """
        if len(self.converts)!=0:
            used_standards = list(map( lambda x:x['standard'], all_samples))
            for convert in self.converts:
                if convert['old']['name'] in used_standards:
                    return True
        return False



    def rebuild(self, sample_record:dict, report:Report )-> tuple[dict, Report]:
        
        convert_flag = False
        for convert in self.converts:
            old_standard = convert['old']
            new_standard = convert['new']

            if sample_record['standard'] == old_standard['name']:
                sample_record, report = RebuildReport.rebuild(sample_record, report, new_standard)
                convert_flag = True
                break
        
        if convert_flag:
            return sample_record, report
        
        else:
            return None, None
        


