import pandas as pd
import requests
import datetime
import pytz

def getData():
#getting content from URL and extracting number we want from it
    url          = "https://secure.actblue.com/metrics/bignumber"
    response     = requests.get(url)
    content      = response.content
    content      = content.decode()
    splitContent = content.split('"')
    bigNumber    = splitContent[3]
    bigNumber    = bigNumber.replace(",", "")
    bigNumber    = int(bigNumber)

    #getting current US Central time
    dt_utcnow  = datetime.datetime.now(tz=pytz.UTC)
    dt_central = dt_utcnow.astimezone(pytz.timezone('US/Central'))
    my_dict = {dt_central: bigNumber}

    return my_dict

    
 
