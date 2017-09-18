import serial
import time
import requests
import json
firebase_url = 'https://pythontofirebase-21c9e.firebaseio.com'
#Connect to Serial Port for communication
ser = serial.Serial('COM4', 9600, timeout=0)
#Setup a loop to send Temperature values at fixed intervals
#in seconds
fixed_interval = 5
sortVar = -1
while 1:
  try:
    #temperature value obtained from Arduino + LM35 Temp Sensor          
    moister_c = ser.readline()
    
    #current time and date
    time_hhmmss = time.strftime('%H:%M:%S')
    date_mmddyyyy = time.strftime('%d/%m/%Y')
    
    #current location name
    moister_location = 'Pune';
    #print(moister_c + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' + moister_location)
    
    #insert record
    data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':moister_c.decode('utf-8'), 'sortOn':sortVar}
    #result = requests.post(firebase_url + '/' + moister_location + '/Moisture.json', data=json.dumps(data))
    result = requests.post(firebase_url + '/' + moister_location + '/Moisture.json', data=json.dumps(data))
	
    print('Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text)
    sortVar-=1
    time.sleep(fixed_interval)
  except IOError:
    print('Error! Something went wrong.')
  time.sleep(fixed_interval)