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

import RPi.GPIO as GPIO
import time

# import only system and name from os for clear_screen()
from os import system, name 

# Define variable LedPin and set the value to #27, corresponding to the GPIO pin).
LedPin = 27

# Define duration of the LEDs glowing in seconds
LedInterval = 1

# Define how often the LED should turn on and off
GlowRepeats = 10

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

# Menu function
def print_message():
	print (" ")
	print ("          Interactive Blinking LED           ")
	print ("=============================================")
	print (" ")
	print(("     LED pin is set to GPIO" + str(LedPin)))
	print(("     LED interval time set to " + str(LedInterval) + " seconds"))
	print(("     LED sequence repeats set to " + str(GlowRepeats) + " times"))
	print(("     LED sequence timeout set to " + str(LedTimeout) + " seconds"))
	print (" ")
	print ("=============================================\n")
	print ("     1     - Start LED sequence")
	print ("     2     - Change GPIO pin")
	print ("     3     - Change LED blinking time")
	print ("     4     - Change LED sequence repeats")
	print ("     5     - Change LED sequence timeout\n")
	print ("     9     - End program\n")
	eval(input ("     What would you like to do?\n"))

# Get menu choice
choice = input('Enter your choice [1-3] : ')

# Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Starting backup...")
elif choice == 2:
        print ("Starting user management...")
elif choice == 3:
        print ("Rebooting the server...")
else:    ## default ##
        print ("Invalid number. Try again...")

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
		time.sleep(1)

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
