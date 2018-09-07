import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def nothing(x):
	pass
cv2.namedWindow('Trackbars')
cv2.createTrackbar('L-H','Trackbars',0,179,nothing)
cv2.createTrackbar('L-S','Trackbars',0,255,nothing)
cv2.createTrackbar('L-V','Trackbars',0,255,nothing)
cv2.createTrackbar('U-H','Trackbars',179,179,nothing)
cv2.createTrackbar('U-S','Trackbars',255,255,nothing)
cv2.createTrackbar('U-V','Trackbars',255,255,nothing)

while(1):
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	l_h = cv2.getTrackbarPos('L-H','Trackbars')
	l_s = cv2.getTrackbarPos('L-S','Trackbars')
	l_v = cv2.getTrackbarPos('L-V','Trackbars')
	u_h = cv2.getTrackbarPos('U-H','Trackbars')
	u_s = cv2.getTrackbarPos('U-S','Trackbars')
	u_v = cv2.getTrackbarPos('U-V','Trackbars')
	
	lower_range = np.array([l_h,l_s,l_v])
	upper_range = np.array([u_h,u_s,u_v])
	
	mask = cv2.inRange(hsv,lower_range,upper_range)
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	res = cv2.bitwise_and(frame,frame ,mask = mask)
	
	cv2.imshow('result',res)
	print("object detected!!  6cm")
	k = cv2.waitKey(1)
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()