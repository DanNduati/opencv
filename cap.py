import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
while (True):
	_,frame = cap.read()
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1) &0XFF
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows