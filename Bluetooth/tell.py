import sys
from bluepy.btle import UUID, Peripheral
 
#uuid = UUID("beb5483e-36e1-4688-b7f5-ea07361b26a8")
uuid = [
        "00002a00-0000-1000-8000-00805f9b34fb",\
        "beb5483e-36e1-4688-b7f5-ea07361b26a8"] 

mac = "30:ae:a4:12:cb:56"
bluetooth = Peripheral(mac,"public")
system="Where is a will, there's a way."
msg = str(system)

try:
    '''
    name = bluetooth.getCharacteristics(uuid=uuid[0])[0]
    if (name.supportsRead()):
            print(name.read().decode())
    '''        
    message = bluetooth.getCharacteristics(uuid=uuid[1])[0]
    if (message.supportsRead()):
            print(message.read().decode())
    message.write(msg.encode('utf-8'), withResponse=True)
    
 
finally:
    bluetooth.disconnect()
