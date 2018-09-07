import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
if ser.isOpen():
    print "Port Open"
print ser.write('s'.encode())

ser.open()
ser.close()
