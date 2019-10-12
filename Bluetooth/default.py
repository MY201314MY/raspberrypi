import sys
from bluepy.btle import DefaultDelegate
from bluepy.btle import UUID, Peripheral

service = UUID("4fafc201-1fb5-459e-8fcc-c5c9c331914b")
cha = UUID("beb5483e-36e1-4688-b7f5-ea07361b26a8")
mac = "30:ae:a4:12:cb:56"
bluetooth = Peripheral(mac,"public").withDelegate(NotifyDelegate())
time.sleep(1)

Service=bluetooth.getServiceByUUID(service)

message = "Hello,world."
try:
    character = Service.getCharacteristics(uuid=cha)
    character.write(struct.pack('<B', 0x00));
    print ("Led2 on")
    time.sleep(1)
    character.write(struct.pack('<B', 0x01));
    print ("Led2 off")
    time.sleep(1)
except:
    print("Communication failed.")
 
finally:
    print("Execulate successfully.")
    bluetooth.disconnect()
