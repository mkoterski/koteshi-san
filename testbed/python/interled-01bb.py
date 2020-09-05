#!/usr/bin/env python
# Interactive script which lets you choose how many times and for how long an LED is blinking
# 
# Last Update: 2020-09-05
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
# 0.1b - Added menu selection screen shotwing various variables.
#      - Added.
# 0.1a - Initial version. LED turns on and off every second.
#
# LED is connected to pin 24, with a 220 Ohm resistor connected to ground
#
################################################################################################################

import RPi.GPIO as GPIO
import time

# import only system and name from os for clear_screen()
from os import system, name 

# Define variable LedPin and set the value to #27, corresponding to the GPIO pin).
LedPin = 27

# Define intervals of the LEDs glowing in seconds
LedInterval = 1

# Define how often the LED should turn on and off
LedSequenceRepeats = 10

# Define automatic timeout in seconds
LedTimeout = 60

# define our clear function 
def clear_screen(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

# Call clear screen function to 'tidy-up' menu appearance
clear_screen() 

# set_led_pin function select the corresponding GPIO pin on your Raspberry Pi
def set_led_pin():
	LedPin = 0
	while 1 > LedPin or 40 < LedPin:
	    try:
	        LedPin = int(eval(input("Please enter the GPIO pin number corresponding with the connected pin on your Pi [01 - 40]: ")))
	    except ValueError:
	        print ("Your entry was not between 01 - 40 :(")
	print_message()

# set_led_pin function select the corresponding GPIO pin on your Raspberry Pi
def set_led_interval():
	print ("Please enter the GPIO pin number corresponding with the connected pin on your Pi")

# set_led_pin function select the corresponding GPIO pin on your Raspberry Pi
def set_led_sequence_repeats():
	print ("Please enter the GPIO pin number corresponding with the connected pin on your Pi")

# set_led_pin function select the corresponding GPIO pin on your Raspberry Pi
def set_timeout():
	print ("Please enter the GPIO pin number corresponding with the connected pin on your Pi")


# Menu function
def print_message():
	clear_screen()
	#print ("\033[1;32;40m Bright Green  ")
	print ("\n          Interactive Blinking LED           ")
	print ("=============================================\n")
	print(("     LED pin is set to GPIO" + str(LedPin)))
	print(("     LED interval time set to " + str(LedInterval) + " seconds"))
	print(("     LED sequence repeats set to " + str(LedSequenceRepeats) + " times"))
	print(("     LED sequence timeout set to " + str(LedTimeout) + " seconds\n"))
	print ("=============================================\n")
	print ("     1     - Start LED sequence")
	print ("     2     - Change GPIO pin for the LED")
	print ("     3     - Change LED blinking time")
	print ("     4     - Change LED sequence repeats")
	print ("     5     - Change LED sequence timeout\n")
	print ("     9     - End program\n")
# Get menu selection and convert entered MenuSelection string to integer value
	MenuSelection = int(eval(input('Enter your choice: ')))
 
### Take action as per selected menu-option ###
	if MenuSelection == 1:
	        set_led_pin()
	elif MenuSelection == 2:
	        set_led_pin()
	elif MenuSelection == 3:
	        print ("Rebooting the server...")
	elif MenuSelection == 9:
	        print ("Closing program...\n")
	        time.sleep(1)
	        destroy()
	else:    ## default ##
	        print ("Invalid input entered. Try again...\n")
	        time.sleep(1)
	        print_message()

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
	clear_screen()
	while True:
		print("LED ON - Yay")
		# Turn on LED
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(float(LedInterval))
		print("LED OFF - Oooh")
		# Turn off LED
		GPIO.output(LedPin, GPIO.HIGH) 
		time.sleep(float(LedInterval))

# Destroy function ensures a clean script finish (resetting pins, etc.)
def destroy():
	# Turn off LED
	GPIO.output(LedPin, GPIO.HIGH)
	# Release resources
	GPIO.cleanup()



# Script routine
if __name__ == "__main__":
	setup()
	try:
		main()
	# Pressing "Ctrl+C" executes destroy() function.
	except KeyboardInterrupt:
		destroy()
