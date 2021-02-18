import cv2
import numpy as np
#Function to generate Sketch
def sketch(image):
    
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #canny_edges = img_gray
    #Clean up image using Gaussian Blur
    #img_gray = image
    #ksize − A Size object representing the size of the kernel.
    #sigmaX − A variable of the type double representing the Gaussian kernel standard deviation in X direction.
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    cv2.imshow('img_gray_blur',img_gray_blur)
    #canny_edges = img_gray_blur
    #Extract Edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    #Binarise the image
    cv2.imshow('canny_edges',canny_edges)
    canny_edges = img_gray_blur
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('My Live Sketch', sketch(frame))
    if cv2.waitKey(15) & 0xff == ord('q'):
         break
#Release the camera and close windows
cap.release()
cv2.destroyAllWindows()