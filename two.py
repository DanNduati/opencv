import cv2
import numpy as np
cap = cv2.VideoCapture(1)

while (1):
	_,frame = cap.read()
	imggray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',imggray)
	
	k = cv2.waitKey(1)
	if k == 27:
		break
cap.release()

cv2.destroyAllWindows()