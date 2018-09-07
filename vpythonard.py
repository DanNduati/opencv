import serial
#import vpython
ser = serial.Serial('/dev/ttyACM0', 9600)
while (1):
	if(ser.inWaiting()):
		data = ser.readline()
		print data