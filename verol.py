import cv2
import numpy as np
cap= cv2.VideoCapture(0)

while (cap.isOpened()):
	_ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow("frame",gray)
	if cv2.waitKey(0) & 0XFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()
	