#!/usr/bin/python
import time
import json
import datetime
import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 1883
keepalive = 1000
topic = 'server'
client = mqtt.Client()
client.connect(host,port,keepalive)
print("****************Hello,world****************")
print("The moment is: %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Thank you for choosing this software.")
print("You can turn the server from 0 to 180,press 'q' to quit.")
while True:
    message = input("The degree you want to turn(0~180):")
    if(message == 'q'):
        break
    if message<0 or message>180:
        print("Error date,please input again")
        continue
    angle = message
    message=0.005 + round(0.12*message/180,2)
    message=json.dumps({"topic":"server","angle":angle,"duty": message})
    client.publish(topic,message)
    print("Execute successfully.")
client.disconnect()
print("Thanks!")