msg = ["abc", "dewdf"]

with open("message.txt",'w') as file:
        file.write("")

for i in range(0,2):
    with open("message.txt",'a') as file:
        file.write(msg[i]+"\n")

with open("message.txt",'r') as file:
    for i in range(0,2):
        x = file.readline()
        print(x)
