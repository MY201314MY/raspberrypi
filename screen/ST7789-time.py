#coding: utf-8  
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
moment = datetime.datetime.now().time().strftime("%H:%M:%S")
backup =moment
font = cv2.FONT_HERSHEY_SIMPLEX
log[0:22,0:239,0] = 255
log[0:22,0:239,1] = 255
log[0:22,0:239,2] = 255
cv2.putText(log, moment, (36, 18), font, 0.64, (0, 0, 0), 2)

logo = cv2.imread("/home/pi/wechat/wechat.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 0:36, 0] = logo[0:36, 0:36, 0]
log[2:38, 0:36, 1] = logo[0:36, 0:36, 1]
log[2:38, 0:36, 2] = logo[0:36, 0:36, 2]

disp.display(log.astype('uint16'), 0, 0, 239, 239, choose=True)

font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
    moment = datetime.datetime.now().time().strftime("%H:%M:%S")
    if moment != backup:
        backup = moment
        log[0:22,36:239,0] = 255
        log[0:22,36:239,1] = 255
        log[0:22,36:239,2] = 255
        cv2.putText(log, moment, (36, 18), font, 0.64, (0, 0, 0), 2)
        disp.display(log.astype('uint16'), 0, 0, 239, 239, choose=True)
