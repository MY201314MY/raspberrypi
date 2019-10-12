import sys
import time
from bluepy.btle import UUID, Peripheral
print(len(sys.argv))
if len(sys.argv) != 2:
    system="Where is a will, there's a way."
else:
    system=sys.argv[1]

msg = str(system)

uuid = UUID("beb5483e-36e1-4688-b7f5-ea07361b26a8")
mac = "30:ae:a4:12:cb:56"
bluetooth = Peripheral(mac,"public")

try:        
    message = bluetooth.getCharacteristics(uuid=uuid)[0]
    if (message.supportsRead()):
            print("message from the mongoose Bluetooth:")
            print(message.read().decode())
    message.write(msg.encode('utf-8'), withResponse=True)
    for i in range(65, 91):
        char = chr(i)
        message.write(char.encode('utf-8'), withResponse=True)
        print("No.%02d:Send '%s' to ESP32" % (i-64, char))
        time.sleep(2)
except:
    print("Communication failed.")
 
finally:
    print("Successfully send 26 ASCII characters.")
    bluetooth.disconnect()
