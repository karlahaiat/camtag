#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def led_setup():
    global power
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    # open log file in append mode
    power['logfile_pointer'] = open(power['logfile'], 'a+')


def power_on():
    global lipopi

    msg = "User Request - Turned on at %d\n" %time.time()
    power['logfile_pointer'].write(msg)
    power['logfile_pointer'].close()
    GPIO.output(18,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(18,GPIO.LOW)



# Main --------------------------------------------

power = {}

power['logfile'] = '/home/pi/power.log'  # FULL path to the log file

# setup the GPIO pins and event triggers
led_setup()

power_on()
