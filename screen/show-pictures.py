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

log = cv2.imread('/home/pi/wechat/welcome.jpg')
log = cv2.resize (log,(240,240))


logo = cv2.imread("/home/pi/wechat/wechat.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 2:38, 0] = logo[0:36, 0:36, 0]
log[2:38, 2:38, 1] = logo[0:36, 0:36, 1]
log[2:38, 2:38, 2] = logo[0:36, 0:36, 2]

logo = cv2.imread("/home/pi/wechat/ba.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 42:78, 0] = logo[0:36, 0:36, 0]
log[2:38, 42:78, 1] = logo[0:36, 0:36, 1]
log[2:38, 42:78, 2] = logo[0:36, 0:36, 2]

logo = cv2.imread("/home/pi/wechat/wei.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 82:118, 0] = logo[0:36, 0:36, 0]
log[2:38, 82:118, 1] = logo[0:36, 0:36, 1]
log[2:38, 82:118, 2] = logo[0:36, 0:36, 2]

logo = cv2.imread("/home/pi/wechat/dao.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 122:158, 0] = logo[0:36, 0:36, 0]
log[2:38, 122:158, 1] = logo[0:36, 0:36, 1]
log[2:38, 122:158, 2] = logo[0:36, 0:36, 2]

logo = cv2.imread("/home/pi/wechat/pay.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 162:198, 0] = logo[0:36, 0:36, 0]
log[2:38, 162:198, 1] = logo[0:36, 0:36, 1]
log[2:38, 162:198, 2] = logo[0:36, 0:36, 2]

logo = cv2.imread("/home/pi/wechat/ku.jpg")
logo = cv2.resize(logo, (36, 36))
log[2:38, 202:238, 0] = logo[0:36, 0:36, 0]
log[2:38, 202:238, 1] = logo[0:36, 0:36, 1]
log[2:38, 202:238, 2] = logo[0:36, 0:36, 2]

disp.display(log.astype('uint16'), 0, 0, 239, 239, choose=True)
time.sleep(2)
path=["wechat.jpg","ba.jpg","wei.jpg","dao.jpg","pay.jpg","ku.jpg"]
while True:
    for i in path:
        logo = cv2.imread("/home/pi/wechat/"+i)
        logo = cv2.resize(logo, (120, 120))
        log[60:180, 60:180, 0] = logo[0:120, 0:120, 0]
        log[60:180, 60:180, 1] = logo[0:120, 0:120, 1]
        log[60:180, 60:180, 2] = logo[0:120, 0:120, 2]
        disp.display(log.astype('uint16'), 0, 0, 239, 239, choose=True)
        time.sleep(2)
