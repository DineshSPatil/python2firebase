import sys
import serial
arduino = serial.Serial('COM4', 9600, timeout=.1)
while True:
	data = arduino.readline() # #the last bit gets rid of the new-line chars [:-2]
	if data:
		print(data.decode('utf-8'))