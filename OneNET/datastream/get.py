import json
import requests

device='47975479'
apikey='r6VsaTGQVMeYmOujP4xkHFVCXvo='

url='http://api.heclouds.com/devices/%s/datastreams' % device

print(url)

headers={
    "api-key":apikey,
    "Connection":"close"
    }

r=requests.get(url,headers=headers)
print(r.content)
res=json.loads(r.content)

for i in range(0,len(res['data'])):
    if res['data'][i]['id']=='temperature':
        print("Temperature data received.")
        print(res['data'][i]['current_value'])
    elif res['data'][i]['id']=='humidty':
        print("Humidity data received.")
        print(res['data'][i]['current_value'])
    else:
        {}