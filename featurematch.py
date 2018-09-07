import cv2
import numpy
import matplotlib.pyplot as plt
img1=cv2.imread('karius.jpeg',1)
img2=cv2.imread('rubbish2.jpeg',-1)
orb =cv2.ORB_create()
#gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#retval, threshold = cv.threshold(img1,120,255, cv2.TRESH_BINARY)
kp1, des1 =orb.detectAndCompute(img1,None)
kp2, des2 =orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)

#find matches
matches = bf.match(des1, des2)
matches = sorted(matches , key = lambda x:x.distance)

img3= cv2.drawMatches(img1,kp1, img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()
