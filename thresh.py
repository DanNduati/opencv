import cv2
import numpy as np
image = cv2.imread('thresh3.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#simple thresholding
_,thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
#adaptive thresholdings
th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,3)
cv2.imshow('image',gray)
cv2.imshow('threshimg',thresh)
cv2.imshow('adaptive',th2)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()