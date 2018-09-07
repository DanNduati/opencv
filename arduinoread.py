import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
while(ser.isOpen()):
	name =ser.readline() 
	print (name)
	if(name == 27):
		break
ser.close()
	