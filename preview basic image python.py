import cv2
#import matplotlib
import numpy
img = cv2.imread('elephant.jpg',cv2.IMREAD_COLOR)
cv2.imshow('Window',img)
cv2.waitkey(0)
