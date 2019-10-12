import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 255, 0), 4)

img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(1)&0xFF == ord('q')
        break
cv2.destroyAllWindows()
