#!/usr/bin/env python
# Interactive script which lets you choose how many times and for how long an LED is blinking
# 
# Last Update: 2020-09-03
# Modified by: Matthias Koterski
#
# To do:
# - Create menu
# - Add option for number of blinkings
# - Add option for duration of blinkings
#
# Change log: 
#
# 0.1a - Initial version. LED glows in endless loop for 1 second
#
# Based on original work by Scott Kildall (www.kildall.com)
# LED is on pin 4, use a 270 Ohm reistor to ground
#
################################################################################################################


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
	GPIO.output(4,True)
	time.sleep(1)	
	GPIO.output(4,False)
	time.sleep(1)
