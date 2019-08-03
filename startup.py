import time
import threading
import os

def startprgm(i):
	#This script turns on led and logs time
    	if (i == 0):
        	os.system("sudo python /home/pi/camtag/ledstart.py")
	#This script starts the gps
    	elif (i == 1):
        	os.system("sudo python /home/pi/camtag/sensors/gps.py")
	#This script starts all the i2c sensors
	elif (i == 2):
		os.system("sudo python /home/pi/camtag/sensors/read_sensors.py")
	#This script starts the camera feeds
	elif (i ==3):
		os.system("sudo python /home/pi/camtag/sensors/camera.py")
	else:
        	pass

for i in range(4):
    t = threading.Thread(target=startprgm, args=(i,))
    t.start()
