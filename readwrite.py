import cv2
import numpy as np
#read the image in gray scale
img = cv2.imread('messi.jpeg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord ("s"):
    cv2.imwrite('messi_grey.png',img)
    cv2.destroyAllWindows()
