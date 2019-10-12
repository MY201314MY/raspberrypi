#!/usr/bin/python
import time
import paho.mqtt.client as mqtt

host = '39.96.169.217'
port = 1883
keepalive = 60
topic = 'pi'

client = mqtt.Client()
client.connect(host,port,keepalive)
client.publish(topic,'Hello,world.')
client.disconnect()
print("Now,let's turn on the LED.")

