import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while (1):
	_,frame = cap.read()
	
	#convert to hsv colorspace
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#hsv ranges for the oobject you want to track 
	lower_blue = np.array([110,0,50])
	upper_blue = np.array([130,255,255])
	
	#threshold
	mask = cv2.inRange(hsv,lower_blue,upper_blue)
	#bitwise and 
	res = cv2.bitwise_and(frame,frame,mask = mask)
	
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	
	k = cv2.waitKey(1) &0XFF
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()