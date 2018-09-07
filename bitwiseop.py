import cv2
import numpy as np
#load the images
img2 = cv2.imread('mbappe.png')
img1 = cv2.imread('messi_d1.jpg')

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
while (1):
	cv2.imshow('messi',gray)
	cv2.imshow('mask',mask)
	cv2.imshow('res',mask_inv)
	k = cv2.waitKey(1) & 0XFF
	if k == 27:
		break
cv2.destroyAllWindows()
