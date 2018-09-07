import cv2
import numpy as np
#create a black image
img = np.zeros((512,512,3), np.uint8)
#draw a line
img = cv2.line(img,(0,0),(511,511),(255,0,0),4)
#draw rectangle
img=cv2.rectangle(img,(105,105),(405,405),(0,255,0),4)
#draw circle
img = cv2.circle(img,(255,255), 63, (0,0,255),-2)
#draw ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
img = cv2.ellipse(img,(256,256),(50,25),0,270,360,(120,120,120),-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))
img=cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('img',img)
if cv2.waitKey(0) & 0xFF==ord('q'):
	cv2.destroyAllWindows()
	