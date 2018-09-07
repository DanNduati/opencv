import cv2
import numpy as np
def nothing(x):
	pass
#create a black image 
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
#create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
#create a switch for on and off 
switch = '0:OFF\n 1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
while (1):
	cv2.imshow('image',img)
	k = cv2.waitKey(1) & 0XFF
	if k == 27:
		break
	#get current positions for the four trackbars
	r=cv2.getTrackbarPos('R','image')
	g=cv2.getTrackbarPos('G','image')
	b=cv2.getTrackbarPos('B','image')
	s=cv2.getTrackbarPos(switch,'image')
	if s == 0:
		img[:] =0
	else:
		img[:] =[b,g,r]
cv2.destroyAllWindows()