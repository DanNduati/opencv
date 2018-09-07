import cv2
import numpy as np

cap = cv2.VideoCapture(1)
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
	_,frame=cap.read()
	fgmask = fgbg.apply(frame)
	
	cv2.imshow('origi',frame)
	cv2.imshow('fg',fgmask)
	k = cv2.waitKey(1)
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()