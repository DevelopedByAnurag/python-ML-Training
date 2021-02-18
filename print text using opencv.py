import cv2
import datetime
cap = cv2.VideoCapture(0)
cap.set(3,3000)
cap.set(4,4000)
print(cap.get(3))
print(cap.get(3))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'width' + str(cap.get(3)) +'Height' + str(cap.get(4)) 
        dat = str(datetime.datetime.now())
        frame = cv2.putText(frame,text ,(10,50),font,1,(0,255,255),1,cv2.LINE_AA)
        frame = cv2.putText(frame,dat,(10,100),font,1,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(15) & 0xff == ord('q'):
            break
    else:
            break
cap.release()
cv2.destroyAllWindows()