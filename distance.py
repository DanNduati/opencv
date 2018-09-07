import cv2
import time
import numpy as np
import serial
cap = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyACM1', 9600)
def stream():
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1)
	
		
while (1):
	_,frame = cap.read()
	stream()
	if(ser.inWaiting()):
		data = ser.readline()
		dist = (data)
		print dist
		if dist<10:
			print "obj present"
			
		else:
			
			print "no object"
		
			

