import cv2
import numpy as np
img= cv2.imread('bookpage.jpg')
retval, threshold =cv2.threshold(img,12,255,cv2.THRESH_BINARY)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 115, 1)
# There is another version of thresholding that one can do, called Otsu's threshold. It doesn't serve us well here, but:
retval3,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('Adaptive threshold',gaus)
cv2.imshow('Otsu threshold',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()