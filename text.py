import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Dan',(10,500),font,4,(255,0,0),2,cv2.LINE_AA)
cv2.imshow("black",img)
#cv2.destroyAllWindows()
 
if cv2.waitKey(0) & 0XFF == ord('q'):
	cv2.destroyAllWindows()