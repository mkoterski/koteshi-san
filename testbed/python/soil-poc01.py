#!/usr/bin/python
#
# Simple soil moisture sensor test
# 
# Last Update: 2020-11-07
#
# Modified by: Matthias Koterski
#
# Modified original script found at http://www.piddlerintheroot.com/soil-moisture-sensor/ and converted it to Python 3.
#

import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print("Water Detected!")
        else:
                print("Water Detected!")
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)