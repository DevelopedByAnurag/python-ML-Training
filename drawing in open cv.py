import cv2
#from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("C:/Users/Tecwe/Downloads/python/obama.jpg",1)
#img = np.zeros([1024,2048,3], np. uint8)
#img = np.full([1024,2048,3], (23,46,34),np.uint8)
img = cv2.line(img,(0,0),(255,255), (147,96,44),10)
img = cv2.arrowedLine(img,(0,0),(12,255), (255,0,0), 10)
img = cv2.rectangle(img,(384,0), (510,128), (0,0,255), 10)
img = cv2.circle(img, (447,63), 63, (0,255,0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'dilpreet dala', (10,500), font, 4, (0, 255,255), 10, cv2.LINE_AA)
img = cv2.ellipse(img,(256,256),(100,50),0,0,18,255,-1)                                      
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()