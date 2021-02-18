import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fivecc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fivecc, 20.0, (740,480))
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        gray=cv2.cvtColor(frame, 1)
        cv2.imshow('frame',gray)
        if cv2.waitKey(15) & 0xff == ord('q'):
            break
    else:
            break
cap.release()
out.release()
cv2.destroyAllWindows()