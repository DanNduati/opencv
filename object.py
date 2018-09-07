import cv2
cap=cv2.VideoCapture(0)
while (1):
	#take each frame
	_, frame=cap.read
	#convert from bgr to hsv
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#define the range of the blue color
	lower_blue=[110,50,50]
	upper_blue=[130,255,255]
	#threshold the hsv to get only the blue color
	mask=cv2.inRange(hsv,lower_blue,upper_blue)
	#bitwise_AND the mask and the original image
	res=cv2.bitwise_and(frame,frame,mask=mask)
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k=cv2.waitKey(0)
	if k==27:
		break
cv2.destroyAllWindows()