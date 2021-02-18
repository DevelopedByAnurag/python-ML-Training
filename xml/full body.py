import cv2
import numpy as np
smile=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture("../O-Face _ 100 People Show Us Their O-Faces _ Keep it 100 _ Cut.mp4");

while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    smiles=smile.detectMultiScale(gray,1.3,5)
    for(r,t,m,j) in smiles:
        cv2.rectangle(img,(r,t),(r+m,t+j),(255,255,0),2)
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()