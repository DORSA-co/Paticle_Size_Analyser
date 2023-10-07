import datetime

class datetimeFormat:
    DATE_STR_FORMAT = "%Y/%m/%d"
    TIME_STR_FORMAT = "%H:%M:%S"

    @staticmethod
    def date_to_str( datetime:datetime.date):
        return datetime.strftime(datetimeFormat.DATE_STR_FORMAT)

    
    @staticmethod
    def time_to_str( datetime:datetime.time):
        return datetime.strftime(datetimeFormat.TIME_STR_FORMAT)

    
    @staticmethod
    def str_to_time( time:str):
        return datetime.datetime.strptime(time, datetimeFormat.TIME_STR_FORMAT).time()
    
    @staticmethod
    def str_to_date( date:str):
        return datetime.datetime.strptime(date, datetimeFormat.DATE_STR_FORMAT).date()
    
    @staticmethod
    def combine(date:datetime.date, time:datetime.time):
        return datetime.datetime.combine(date, time)
    




class timerCounter:
    

    def __init__(self, hour=0, minute=0, second=0) -> None:
        self.time = datetime.datetime(1997,5,15, hour=0, minute=0, second=0) #amirhossein malekzadeh birthday
        self.count(hour, minute, second)
    


    def count(self, hour=0,  minute=0, second=0):
        #self.t += (second + minute * 60 + hour * 3600)
        minute = minute + second // 60
        second = second - second // 60
        
        hour = hour + minute // 60
        minute = minute - minute // 60
        
        self.time = self.time + datetime.timedelta(hours=hour, minutes=minute, seconds=second)
    
    def get_fstr(self, format='%H:%M:%S'):
        format = format.upper()
        return self.time.strftime(format)
        

    


