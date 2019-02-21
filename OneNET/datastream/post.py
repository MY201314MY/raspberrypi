import json
import requests
import datetime

device = '47975479'
humidity = 12
temperature =28
APIKEY = 'r6VsaTGQVMeYmOujP4xkHFVCXvo='
url = 'http://api.heclouds.com/devices/%s/datapoints'%(device)

time = datetime.datetime.now()
dict = {
    "datastreams":[
        {
            "id":"temperature",
            "datapoints":[{"at":time.isoformat(),"value":humidity}]
            },
        {
            "id":"humidty",
            "datapoints":[{"at":time.isoformat(),"value":humidity}]
            }
        ]
}

dict['datastreams'][0]['datapoints'][0]['value'] = humidity
dict['datastreams'][1]['datapoints'][0]['value'] = temperature
print (dict)
s = json.dumps(dict)
headers = {
                "api-key":APIKEY,
                "Connection":"close"
 
           }
r=requests.post(url,headers=headers,data=s)
 
print(r.headers)
 
print(r.text)