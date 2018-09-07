import cv2
import numpy as np
img=np.zeros((1024,1024,3),np.uint8)
#D
img=cv2.line(img,(64,128),(64,383),(255,0,0),4)
img = cv2.ellipse(img,(64,255),(100,122),0,90,-90,(255,0,0),4)
#A
img=cv2.line(img,(255,128),(155,383),(0,255,0),4)
img=cv2.line(img,(255,128),(355,383),(0,255,0),4)
img=cv2.line(img,(200,255),(311,255),(0,255,0),4)
#N
img=cv2.line(img,(455,128),(455,383),(0,0,255),4)
img=cv2.line(img,(455,128),(655,383),(0,0,255),4)
img=cv2.line(img,(655,383),(655,128),(0,0,255),4)
cv2.imshow("image",img)
#cv2.waitkey(0)
if cv2.waitKey(0) & 0xFF==ord('q'):
	cv2.destroyAllWindows()