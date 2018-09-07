import numpy as np
import cv2

detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#cap_filtered=cv2.medianBlur(cap,5)

while(True):
    ret, img = cap.read()
	#Qimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    faces = detector.detectMultiScale(gray, 1.1, 5)#was 1.3,5
	#faces = detector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) ==27:
        break
    
cap.release()
cv2.destroyAllWindows()