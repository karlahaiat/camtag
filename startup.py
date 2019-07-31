import time
import threading
import os

def startprgm(i):
    	if (i == 0):
        	os.system("sudo python /home/pi/camtag/ledstart.py")
    	elif (i == 1):
        	os.system("sudo python /home/pi/camtag/sensors/gps.py")
	elif (i == 2):
		os.system("sudo python /home/pi/camtag/sensors/read_sensors.py")
	elif (i ==3):
		os.system("sudo python /home/pi/camtag/sensors/camera.py")
	else:
        	pass

for i in range(4):
    t = threading.Thread(target=startprgm, args=(i,))
    t.start()
