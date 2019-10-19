string = "我们去图书馆吧!然后回到自习室学习高数，今晚看导数和微分部分!"
msg = []
position = 0
flag = 0
for i in range(len(string)):
    if ord(string[i]) > 255:
        position = position + 18 + 2
    else:
        position = position + 9
    if position > 240:
        position = 18 +2 if ord(string[i]) > 255 else 9
        msg.append(string[flag:i])
        flag=i
msg.append(string[flag:])

for i in msg:
    print(i)