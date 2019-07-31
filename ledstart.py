#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def led_setup():
    global lipopi
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    # open log file in append mode
    lipopi['logfile_pointer'] = open(lipopi['logfile'], 'a+')


def lipopi_on():
    global lipopi

    msg = "User Request - Turned on at %d\n" %time.time()
    lipopi['logfile_pointer'].write(msg)
    lipopi['logfile_pointer'].close()
    GPIO.output(18,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(18,GPIO.LOW)



# Main --------------------------------------------

# Setup LiPoPi global variable array

lipopi = {}

lipopi['logfile'] = '/home/pi/lipopi.log'  # FULL path to the log file

# setup the GPIO pins and event triggers
led_setup()

lipopi_on()
