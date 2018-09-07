import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
while(1):
	#check if there data coming from the serial port
	if (ser.inWaiting()):
		name =ser.readline()
		print(name)
		time.sleep(2)
		if (name == 's'):
			print("thats me")
			break
ser.close()
