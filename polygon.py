import cv2
import numpy as np
#create black image
img = np.zeros((512,512,3), np.uint8)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))
img=cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('img',img)
if cv2.waitKey(0) & 0xFF==ord('q'):
	cv2.destroyAllWindows()