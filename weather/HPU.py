# -*- coding: utf-8 -*-
import requests
r=requests.get('http://www.weather.com.cn/data/sk/101181101.html')
r.encoding='utf-8'
print("City:"+ r.json()['weatherinfo']['city'])
print("ID:"+ r.json()['weatherinfo']['cityid'])
print("Pressure:"+ r.json()['weatherinfo']['AP'])
print("Temperature:"+r.json()['weatherinfo']['temp']+ " C")
print("Humidty:"+r.json()['weatherinfo']['SD']+"R")