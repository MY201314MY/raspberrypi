import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

hostname = '183.230.40.39'  
port = 6002  
clientid = '509109399'  
username = '179383'  
password = ''  
topic1 = 'ESP32' 
topic2 = 'raspberrypi'
topic3 = 'cmd_light '
topic4 = 'iPhone'


def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # 连接完成之后订阅主题
    client.subscribe(topic1, 0)  #参数二为QoS级别，默认QoS=0
    client.subscribe(topic2)
    client.subscribe(topic3)
    client.subscribe(topic4)
    client.subscribe("cmd_light")

# 消息推送回调函数
def on_message(client, userdata, msg):
    print('[topic:]'+msg.topic + '  ' + '[payload:]'+str(msg.payload))
    if msg.topic == 'upload': # 如果收到upload主题，就将数据类型3（json数据2）内容上传给OneNET平台
        dp_load = '{"a":1,"c":3,"b":2,"d":4}'
        dp_type = 3
        dp_len = len(dp_load)
        dp=bytearray()
        dp.append(dp_type)
        dp.append((dp_len >> 8) & 0xFF)
        dp.append(dp_len & 0xFF)
        dp = dp + dp_load
        print (repr(dp))
        (rc, final_mid) = client.publish('$dp', str(dp), 2, True)
    if 'pi' in msg.topic: # 如果收到OneNET下发的主题，然后将信息转发给test主题，其他设备将会收到
        (rc, final_mid) = client.publish('test', str(msg.payload), 2, True)

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
