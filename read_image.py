import cv2
import sys


im = cv2.imread('tom.jpg')
cv2.imwrite('tom.png',im)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
