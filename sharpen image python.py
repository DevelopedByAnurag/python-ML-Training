import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.imshow('orignal', frame)
    npsharp = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    sharpning = cv2.filter2D(frame,-1,npsharp)
    cv2.imshow('sharp', sharpning)
    if cv2.waitKey(15) & 0xff == ord('q'):
         break
cam.release()
cv2.destroyAllWindows()