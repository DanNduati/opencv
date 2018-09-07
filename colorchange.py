import cv2
filename='tom.jpg'
img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('cvt',gray)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()