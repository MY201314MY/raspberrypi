string = "abcdefghijklmnopqrstuvwxyz"
msg = []
position = 0
flag = 0
for i in range(len(string)):
    if ord(string[i]) < 255:
        position = position + 9 + 1
    if position > 240:
        position = 9 + 1
        msg.append(string[flag:i])
        flag=i
msg.append(string[flag:])

for i in msg:
    print(i)
'''
draw.text((0, 40), "WeChat iMessage", (0, 0, 0), font = font)
draw.text((0, 40+18*1), "Please help me turn on the light", (0, 0, 0), font = font)
#draw.text((0, 40+18*2), unicode("As long as you like", 'utf-8'), (0, 0, 0), font = font)
draw.text((0, 40+18*2), "abcdefghijklmnopqrstuvwxyz", (0, 0, 0), font = font)
