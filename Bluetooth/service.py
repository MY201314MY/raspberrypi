from bluepy.btle import UUID, Peripheral

mac = "30:ae:a4:12:cb:56"
p = Peripheral(mac,"public")

services=p.getServices()

for service in services:
   print(service)



chList = p.getCharacteristics()
print("Handle   UUID                                  Properties")
print("-------------------------------------------------------")                     
for ch in chList:
   print("  0x"+ format(ch.getHandle(),'02X')  +"   "+str(ch.uuid) +" " + ch.propertiesToString())

print()
