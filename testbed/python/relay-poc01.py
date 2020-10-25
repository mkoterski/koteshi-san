#!/usr/bin/env python
# Simple relay test script with menu
# 
# Last Update: 2020-10-25
# Modified by: Matthias Koterski
#
# Change log: 
# 
# 0.1b - Relay is off when programm is started and can be switched.
# 0.1a - Initial WIP version.
#
# Relay is connected to pin 7 (GPIO4)
#
# Requirements:
# 1. Raspberry Pi B+ model
# 2. Relay controller
# 3. Water pump
#
# Working Instructions:
# Step 1: Connect any voltage pin from Raspberry Pi to Relay.
# Step 2:Connect any ground pin from Raspberry pi to Relay.
# Step 3: Connect any GPIO pin to Relay module (In this project I used pin 7(GPIO4)).
# Step 4: Open terminal and execute the program we provided below.
#
################################################################################################################

import RPi.GPIO as GPIO
import time

from os import system, name # import only system from os 

GPIO.setwarnings(False) # Deactivate warning messages


# define our clear function 
def clear_screen(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
# menu
def menu():
    #setup() # calling setup() would reset the LED status to OFF
    clear_screen()
    print (50 * '-')
    print ("")
    print ("           R E L A Y   T E S T   0.1 \n")
    print ("Ensure that the relay is connected to GPIO4 (pin #7)\n")
    print (50 * '-')
    print ("1 - RELAY ON")
    print ("2 - RELAY OFF")
    print ("3 - Close program")
    print (50 * '-')
     
    # Get input and convert str to int
    choice = int(input('Enter your choice [1-3] : '))
     
    # Take action as per selected menu-option ###
    if choice == 1:
            print ("Relay turning on...")
            setup()
            GPIO.output(7,False)
            #GPIO.output(RelayPin, GPIO.LOW)
            time.sleep(3)
            menu()
    elif choice == 2:
            print ("Relay turning off...")
            setup()
            GPIO.output(7,True)
            #GPIO.output(RelayPin, GPIO.HIGH)
            time.sleep(3)
            menu()
    elif choice == 3:
            print ("Shutting down program...")
            clear_screen()
            destroy()
    else:    ## default ##
            print ("Invalid number. Try again...")
            time.sleep(2)
            menu()

# Define a setup function for some setup
def setup():
    # Set pin layout to BOARD instead of BCM so that the code can be easily reused
	GPIO.setmode(GPIO.BOARD)
	# Set pin to No. 7 (GPIO4), to output, and initial level to High (3.3v/5v) depending on which pin connected.
    #GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(7,GPIO.OUT,initial=GPIO.HIGH)   


# Define a destroy function for clean up everything afterwards
def destroy():
    # Turn off Relay
    GPIO.output(7,False)
    # Release resource
    GPIO.cleanup()                     

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
            menu()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()