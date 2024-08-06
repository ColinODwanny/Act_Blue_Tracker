
import requests

def getNumber():
#getting content from URL and extracting number we want from it
    url          = "https://secure.actblue.com/metrics/bignumber"
    response     = requests.get(url)
    content      = response.content
    content      = content.decode()
    splitContent = content.split('"')
    bigNumber    = splitContent[3]
    bigNumber    = bigNumber.replace(",", "")
    bigNumber    = int(bigNumber)

    return bigNumber

    
 