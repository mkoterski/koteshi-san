#!/usr/bin/env python
# Simple soil moisture sensor test script with menu
# 
# Last Update: 2020-11-08
# Modified by: Matthias Koterski
#
# Change log: 
# 
# 0.1c - added colours class for some easy text formatting
# 0.1b - Relay is off when programm is started and can be switched.
# 0.1a - Initial WIP version.
#
# Working Instructions:
# Step 1: Connect any 3.3V pin from Raspberry Pi to sensor e.g. pin # .
# Step 2: Connect any ground pin from Raspberry Pi to sensor e.g. pin # .
# Step 3: Connect pin 40 from Raspberry Pi to sensor e.g. pin # .
# Step 4: Open terminal and execute the program below.
#
####################################################################################################################

import RPi.GPIO as GPIO
import time

from os import system, name # import only system from os 

GPIO.setwarnings(False) # Deactivate warning messages


# define colours class for easy font formatting
class colours: # You may need to change color settings in iPython
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    # Usage print (colours.GREEN + "text_prt1" , variable , "text_prt2.\n" , colours.ENDC)

# define clear screen function 
def clear_screen(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
# menu
def menu():
    #setup() # calling setup() would reset the pin status to OFF
    clear_screen()
    print (55 * '-')
    print ("")
    print ("    S O I L   M O I S T U R E    T E S T   0.3 \n")
    print ("Ensure that the sensor is connected to pin #40 \n")
    print (55 * '-')
    print ("1 - Check for water\n")
    #print ("2 - Check for water\n")
    print (colours.RED + "9 - Close program" , colours.ENDC)
    # print ("9 - Close program")
    print (55 * '-')
     
    # Get input and convert str to int
    choice = int(input("\nEnter your choice [1-9] : "))
     
    ### Take action as per selected menu-option ###
    if choice == 1:
            print ("Checking for water...")
            setup()
            def callback(40):
                if GPIO.input(40):
                    print("Water Detected!")
                else:
                    print("Water Detected!")
 
            GPIO.add_event_detect(40, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
            GPIO.add_event_callback(40, callback)  # assign function to GPIO PIN, Run function on change

            GPIO.output(40,False)
            time.sleep(4)
            menu()
    elif choice == 9:
            print ("Shutting down program...")
            time.sleep(1)
            clear_screen()
            destroy()
    else:    ## default ##
            print ("Invalid number. Try again...")
            time.sleep(1)
            menu()

# Define a setup function for some setup
def setup():
    # Set pin layout to BOARD instead of BCM so that the code can be easily reused
	GPIO.setmode(GPIO.BOARD)
	# Set pin to pin #40, to output, and initial level to High (3.3v/5v) depending on which pin connected.
	GPIO.setup(40,GPIO.IN)   
    #GPIO.setup(40,GPIO.OUT,initial=GPIO.HIGH)   

# Define a destroy function for clean up everything afterwards
def destroy():
    # Turn off sensor
    GPIO.output(40,False)
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