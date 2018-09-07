import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#ret,thresh = cv2.threshold(gray,cv2.TRHESH_BINARY)
	#hsv = cv2.cvtColor(gray, cv.COLOR_GRAY2HSV)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows