import datetime

class Log:
    '''
    A Log object contains a (string) event and a date time object
    '''
    def __init__(self, event):
        self._event = event
        self._date_time = datetime.datetime.now()
    
    # Getter methods
    ''' 
    Returns a string representation on the event described"
    '''
    def get_event(self):
        return self._event
    
    '''
    Returns a datetime object representing the date and time this event was logged.
    '''
    def get_date_time(self):
        return self._date_time
    
    '''
    Returns a text representation of the Log
    '''
    def __str__(self):
        date_time = self._date_time.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time + "\t" + self._event