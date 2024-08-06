import datetime
import pytz

def getTime():

    #getting current US Central time
    dt_utcnow  = datetime.datetime.now(tz=pytz.UTC)
    dt_central = dt_utcnow.astimezone(pytz.timezone('US/Central'))
    
    return dt_central