import cv2
import numpy as np
img = cv2.imread('dan.jpg')
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
while(1):	
	cv2.imshow('roro',img)
	k= cv2.waitKey(1) & 0XFF
	if k ==27:
		break
cv2.destroyAllWindows()