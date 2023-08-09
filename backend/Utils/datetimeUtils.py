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