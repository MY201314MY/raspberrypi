import cv2
import datetime

path = "jump.png"
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread(path)
img = cv2.resize(img, (240, 240))
img[0:22, 0:110, 0] = 255
img[0:22, 0:110, 1] = 255
img[0:22, 0:110, 2] = 255
time = datetime.datetime.now().time().strftime("%H:%M:%S")
cv2.putText(img, time, (18, 18), font, 0.64, (0, 0, 255), 2)
cv2.rectangle(img, (0, 0), (110, 22), (0, 0, 255), 1)
cv2.line(img, (119, 0), (119, 239), (255, 0, 0), 1)
cv2.line(img, (0, 119), (239, 119), (0, 0, 255), 1)
cv2.putText(img, "IP:", (0, 119), font, 0.64, (0, 0, 255), 2)
cv2.circle(img, (0, 119), 1, (0, 0, 0), -1)
logo = cv2.imread("apple.png")
logo = cv2.resize(logo, (18, 18))
img[2:20, 0:18, 0] = logo[0:18, 0:18, 0]
img[2:20, 0:18, 1] = logo[0:18, 0:18, 1]
img[2:20, 0:18, 2] = logo[0:18, 0:18, 2]
cv2.imshow("m", img)
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
