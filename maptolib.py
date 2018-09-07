import cv2
import sys
from matplotlib import pyplot as plt
img_name = 'tom.jpg'
img = cv2.imread(img_name)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
