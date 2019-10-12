import cv2
import time
 
camera = cv2.VideoCapture(0)
time.sleep(2)
if camera is None:
    print('请先连接摄像头')
    exit()
 
fps = 5 
pre_frame = None 
 
play_music = False
 
while True:
    start = time.time()
    res, cur_frame = camera.read()
    if res != True:
        break
    end = time.time()
    seconds = end - start
    if seconds < 1.0/fps:
        time.sleep(1.0/fps - seconds)
    cv2.imshow('img', cur_frame)
    infor = cv2.waitKey(30) & 0xFF
    if infor == ord('q'):
        break
    gray_img = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.resize(gray_img, (500, 500))
    gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
    i = 0
    if pre_frame is None:
        pre_frame = gray_img
    else:
        img_delta = cv2.absdiff(pre_frame, gray_img)
        thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 2000: # 设置敏感度
                continue
            else:
                print("捕捉到的图片和前一张不一样, 有一些东西在运动!")
                play_music = True
                break
 
        pre_frame = gray_img
 
camera.release()
cv2.destroyAllWindows()
