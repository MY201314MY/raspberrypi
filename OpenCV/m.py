import cv2
import datetime
import numpy as np

print("The version of OpenCV we used:%s" % cv2.__version__)

cap = cv2.VideoCapture(0)
cap.set(propId=3, value=320)
cap.set(propId=4, value=240)
print("----The width:%d, the hight:%d----" % (cap.get(3), cap.get(4)))
fps = 0
message = {"goals":0}
value = 0
low = np.array([0, 0, 221])
up = np.array([180, 30, 255])
font = cv2.FONT_HERSHEY_SIMPLEX
backup = datetime.datetime.now().time().strftime("%H:%M:%S")
while (True):
    moment = datetime.datetime.now().time().strftime("%H:%M:%S")
    if moment != backup:
        backup = moment
        value = fps
        fps = 0
        
    ret, frame = cap.read()
    fps = fps + 1
    image = frame[0:240, 40:280]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low, up)
    cv2.imshow("goal", mask)
    count = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for i in range(0, len(count)):
        ((x, y), radius) = cv2.minEnclosingCircle(count[i])
        center = (int(x), int(y))
        if radius > 10:
            message["goals"] +=  1
            cv2.circle(image, center, 3, (0, 255, 0), -1)
            cv2.circle(image, center, int(radius), (0, 0, 255), 3)
    cv2.putText(frame, "fps:{0}".format(value), (48, 18), font, 0.64, (0, 0, 255), 2)
    cv2.putText(frame, "sum:{0}".format(message["goals"]), (120, 18), font, 0.64, (0, 0, 255), 2)
    cv2.imshow("ST7789", image)
    message["goals"] = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
