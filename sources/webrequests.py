#Importing requests
import requests

def doGet(URL, params = ""):
    webresult = requests.get(URL, params)

    if webresult.status_code >= 200 and webresult.status_code < 300:
        data = webresult.content.title()
        print(data)

        return data
    return None
