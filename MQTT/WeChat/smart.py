import json 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

hostname = '183.230.40.39'  
port = 6002  
clientid = '47975479'  
username = '179383'  
password = 'r6VsaTGQVMeYmOujP4xkHFVCXvo='  
topic = 'raspberrypi'

def esspressif(cmd):
    topic = 'pi'
    client = mqtt.Client()
    client.connect('127.0.0.1',1883,60)
    client.publish(topic,cmd)
    client.disconnect()
    print("success")
    
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe(topic, 0) 

def on_message(client, userdata, msg):
    print('[topic:]'+msg.topic + '  ' + '[payload:]'+str(msg.payload))
    if msg.topic == 'raspberrypi':
        print("data received")
        message=json.loads(msg.payload)
        if len(message['command'])==2:
            for i in range(len(message['command'])):
                if message['command'][i]['id']=='LED':
                    print("LED")
                    print(message['command'][i]['status'])
                    if message['command'][i]['status']==1:
                        esspressif("ON")
                    else:
                        esspressif("OFF")
                elif message['command'][i]['id']=='motor':
                    print("motor")
                    print(message['command'][i]['status'])
        else:
            print("slider")
            print(message['command'][0]['grade'])
     
def on_publish(mqttc, obj, mid):
    print("Publish mid: " + str(mid))
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print("Log:" + string)

if __name__ == '__main__':
    client = mqtt.Client(client_id=clientid, clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe
    client.on_log = on_log

    try:
        client.username_pw_set(username, password)
        client.connect(hostname, port, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()