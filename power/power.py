#!/usr/bin/env python

# Adaptation of lipopi project by Daniel Bull https://github.com/NeonHorizon/lipopi
#Script turns turns pi off safely with magnetic switch and when low battery is detected by Adafruit's Power Boost 1000
#Script is run as a service (power.service)
#lipopi is under the GNU GENERAL PUBLIC LICENSE

import os
import RPi.GPIO as GPIO
import time

#Setup the GPIO pins
def power_setup():
    global power

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) #Using GPIO number

    #Setting up shutdown pins to receive inputs
    GPIO.setup(power['shutdown_pin'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(power['low_battery_pin'], GPIO.IN)

    #Triggers so actions only happen when GPIOs change state. Events call on functions defined below
    GPIO.add_event_detect(power['shutdown_pin'], GPIO.RISING, callback=power_user_shutdown, bouncetime=300)
    GPIO.add_event_detect(power['low_battery_pin'], GPIO.FALLING, callback=power_low_battery_shutdown, bouncetime=300)

    # open log file in append mode to log shutdown times
    power['logfile_pointer'] = open(power['logfile'], 'a+')

#Function to shutdown on button press/magnetic switch change
def power_user_shutdown(channel):
    global power

    #cmd = "sudo wall 'System shutting down in %d seconds'" % lipopi['shutdown_wait']
    #os.system(cmd)

    #time.sleep(lipopi['shutdown_wait'])

    #Logged message saves time in UNIX, this is so the UNIX time stamps can be compared to real time post-processing
    msg="User Request - Shutting down at %d\n" %time.time()
    power['logfile_pointer'].write(msg)
    power['logfile_pointer'].close()
    GPIO.cleanup()
    os.system("sudo shutdown now")


# Safe shut down when low battery signal is detected from the PowerBoost. Pin is usually high
def power_low_battery_shutdown(channel):
    global power

    #cmd = "sudo wall 'System shutting down in %d seconds'" % lipopi['shutdown_wait']
    #os.system(cmd)

    #time.sleep(lipopi['shutdown_wait'])

    msg="Low Battery! - Shutting down at %d\n" %time.time()
    power['logfile_pointer'].write(msg)
    power['logfile_pointer'].close()
    GPIO.cleanup()
    os.system("sudo shutdown now")

# Close the log file and reset the GPIO pins
def power_cleanup():
    global power
    power['logfile_pointer'].close()
    GPIO.cleanup()



# Main --------------------------------------------


# Setup global variable array
power = {}

# Specify which GPIO pins to use
power['low_battery_pin'] = 5

power['shutdown_pin']  =  6

power['logfile'] = '/home/pi/power.log'  # FULL path to the log file

power_setup()

# Sleep for around 12 hours to keep program running as long as the mission
while True:
    time.sleep(45000)

power_cleanup()




