import cv2
import numpy as np
import datetime
cap = cv2.VideoCapture(0)
events = [i for i in dir(cv2) if 'EVENTS' in i]
print(events)
def click(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x," , ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x)+" , "+str(y)
        cv2.putText(img,strxy,(x,y),font,.5,(255,255,0),2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        print(x," , ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(blue)+" , "+str(green)+" , "+str(red)
        cv2.putText(img,strxy,(x,y),font,.5,(int(blue),int(green),int(red)),2)
        cv2.imshow('image',img)

img = cv2.imread("C:/Users/Tecwe/Downloads/python/chihuahua.jpg")
cv2.imshow("image",img)
cv2.setMouseCallback("image", click)
cv2.waitKey(0)
cv2.destroyAllWindows()