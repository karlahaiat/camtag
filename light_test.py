#Test Yellow and Blue LEDs
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

#Blink Yellow LED
GPIO.output(17,GPIO.HIGH)
time.sleep(3)
GPIO.output(17,GPIO.LOW)

#Blink Blue LED
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
GPIO.output(18,GPIO.LOW)
