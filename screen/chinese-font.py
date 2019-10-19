#coding:utf-8
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

image = cv2.imread("jump.png")
image = cv2.resize(image, (240, 240))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font="simhei.ttf", size=18, encoding="utf-8")
draw.text((0, 30), "我们去图书馆吧！然后回到自", (0, 0, 0), font=font)

img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imshow("m", img)
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()