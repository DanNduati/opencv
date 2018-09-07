import cv2
import numpy as np
#import matplotlib   

cap=cv2.VideoCapture(0)
while(1):
	#take each frame
	_, frame= cap.read()
	#convert bgr to hsv
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#define the range of blue color inhsv
	lower_blue=np.array([110,50,50])
	upper_blue=np.array([130,255,255])
	#threshold for hsv to get only blue colors
	mask=cv2.inRange(hsv, lower_blue,upper_blue)
	#bitwise-AND mask and original image
	res=cv2.bitwise_and(frame,frame, mask= mask)
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	cv2.waitKey(500)
cv2.destroyAllWindows()