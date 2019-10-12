#coding: utf-8
import os
import cv2
import time
import numpy as np
import datetime
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import ST7789 as TFT
from PIL import Image, ImageDraw, ImageFont, ImageColor

# Raspberry Pi pin configuration:
RST = 27
DC  = 25
LED = 24
SPI_PORT = 0
SPI_DEVICE = 0
SPI_MODE = 0b11
SPI_SPEED_HZ = 40000000
IP = "192.168.3.16"
disp = TFT.ST7789(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=SPI_SPEED_HZ),
       mode=SPI_MODE, rst=RST, dc=DC, led=LED)
disp.begin()
disp.clear()

imagex = Image.open('/home/pi/wechat/wechat.jpg')
imagex.thumbnail((240, 240), Image.ANTIALIAS)
disp.display(imagex)
time.sleep(2)

disp.clear()
log = cv2.imread('/home/pi/TFT/watch.jpg')
log = cv2.resize (log,(240,240))

log[0:239,0:240,0] = 0xFF
log[0:239,0:240,1] = 0xEF
log[0:239,0:240,2] = 0xBF

moment = datetime.datetime.now().time().strftime("%H:%M:%S")
font = cv2.FONT_HERSHEY_SIMPLEX
log[0:40,0:240,0] = 255
log[0:40,0:240,1] = 255
log[0:40,0:240,2] = 255
cv2.putText(log, moment, (38, 18), font, 0.64, (0, 0, 0), 2)
cv2.putText(log, "IP:" + IP, (38, 36), font, 0.64, (0, 0, 0), 2)

logo = cv2.imread("/home/pi/wechat/wechat.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 2:38, 0] = logo[0:36, 0:36, 0]
log[2:38, 2:38, 1] = logo[0:36, 0:36, 1]
log[2:38, 2:38, 2] = logo[0:36, 0:36, 2]

for i in range(8):
    cv2.line(log, (0,40+18*i), (239,40+18*i),(0,0,128),1)
cv2.rectangle(log, (0, 215), (239, 238), (0, 0, 255), 2)
disp.display(log.astype('uint16'), 0, 0, 239, 239, choose=True)
font = ImageFont.truetype(font="simhei.ttf", size=20, encoding="utf-8")
FileName='log.txt'
creat = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(FileName).st_ctime))
while True:
    motify = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(FileName).st_ctime))
    if creat != motify:
        creat = motify
        log[40:215,0:240,0] = 0xFF
        log[40:215,0:240,1] = 0xEF
        log[40:215,0:240,2] = 0xBF
        for i in range(8):
            cv2.line(log, (0,40+18*i), (239,40+18*i),(0,0,128),1)
        with open("log.txt","r") as file:
            string = file.read()
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
        log = cv2.cvtColor(log, cv2.COLOR_BGR2RGB)
        log = Image.fromarray(log)
        draw = ImageDraw.Draw(log)
        for i in range(len(msg)):
            print(msg[i])
            cls = "                        "
            draw.text((0, 40+18*i), cls, (0, 0, 0), font = font)
            draw.text((0, 40+18*i), msg[i], (0, 0, 0), font = font)
        log = cv2.cvtColor(np.array(log), cv2.COLOR_RGB2BGR)

        disp.display(log.astype('uint16'), 0, 0, 239, 239, choose=True)
        time.sleep(1)
