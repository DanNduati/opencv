import cv2
import numpy as np
img = cv2.imread('neymar.jpg');
#access the pixel value at the following coordinates
px = img[100,100]
print (px)
print img.shape#returns row columns and channels of the image
print img.size#total no ofpixels 
print img.dtype#data type