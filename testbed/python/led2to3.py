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
# - Add option to cancel script not just with ctrl + C
#
# Change log: 
#
# 0.1a - Initial version. LED turns on and off every second.
#
# LED is connected to pin 24, with a 220 Ohm resistor connected to ground
#
################################################################################################################

# Logic

# Hello
# Currently set to...
# Set duration
# Set repeats
# Start
# Timeout on/off
# Quit

import RPi.GPIO as GPIO
import time

# Define variable LedPin and set the value to #27, corresponding to the GPIO pin).
LedPin = 27

# Define duration of the LEDs glowing in seconds
GlowDuration = 1

# Define how often the LED should turn on and off
GlowRepeats = 10

# Define automatic timeout in seconds
GlowDuration = 60

# Menu function
def print_message():
	print ("========================================")
	print ("|              Blink LED               |")
	print ("|    ------------------------------    |")
	print ("|         LED connect to GPIO27        |")
	print ("|                                      |")
	print ("|        LED will Blink at 500ms       |")
	print ("|                                      |")
	print ("========================================\n")
	print('Program is running...')
	print('Please press Ctrl+C to end the program...')
	input ("Press Enter to begin\n")
	#input ("Press Enter to begin") #python3 command

# Setup function ensures all parameter are correctly set.
def setup():
	# Set the GPIO mode to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	# Set LedPin's mode to output,
	# and initial level to High(3.3v)
	GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

# Main function
def main():
	# Print messages
	print_message()
	while True:
		print('LED ON - Yay')
		# Turn on LED
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(1)
		print('LED OFF - Oooh')
		# Turn off LED
		GPIO.output(LedPin, GPIO.HIGH) 
		time.sleep(1)

# Destroy function ensures a clean script finish (resetting pins, etc.)
def destroy():
	# Turn off LED
	GPIO.output(LedPin, GPIO.HIGH)
	# Release resources
	GPIO.cleanup()

# Script routine
if __name__ == '__main__':
	setup()
	try:
		main()
	# Pressing 'Ctrl+C' executes destroy() function.
	except KeyboardInterrupt:
		destroy()
