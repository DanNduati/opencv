import cv2
import numpy as np
#import argparse
import imutils
#load the image and compute the ratio of the old height
#to the new height clone it and resize it
image = cv2.imread('scan2.jpg')
ratio = image.shape[0]/800.0
orig = image.copy()
image = imutils.resize(image,height=500)

#convert to grayscale clur it and find the edges
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh =cv2.threshold(image,20,255,cv2.THRESH_BINARY)
gray = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(gray,75,200)

print("step 1 edge detection")
cv2.imshow('THRESH',thresh)
cv2.imshow('image',image)
cv2.imshow('grey',gray)
cv2.imshow('edged',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
