import cv2
import numpy as np 
cam = cv2.VideoCapture(0)
while(True):
        _,frame=cam.read()
        #img_gray_blur = cv2.GaussianBlur(frame, (5,5), 0)
        #cv2.imshow('img_gray_blur',img_gray_blur)
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('orignal',hsv)
        color=cv2.cvtColor(frame, 1)
        cv2.imshow('2',color)
        edges=cv2.Canny(frame, 100,200)
        cv2.imshow('edges',edges)
        if cv2.waitKey(15) & 0xff == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()