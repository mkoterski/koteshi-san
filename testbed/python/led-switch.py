#!/usr/bin/env python

# val = input("Enter your value: ") 
# print(val)

import RPi.GPIO as GPIO
import time

# Set #27 as LED pin
LedPin = 27

# menu
def menu():
    setup()
    print (30 * '-')
    print ("   L E D   S W I T C H  0.1 ")
    print (30 * '-')
    print ("1 - LED ON")
    print ("2 - LED OFF")
    print ("3 - Close program")
    print (30 * '-')
     
    # Get input and convert str to int
    choice = int(input('Enter your choice [1-3] : '))
     
    # Take action as per selected menu-option ###
    if choice == 1:
            print ("LED turning on...")
            setup()
            GPIO.output(LedPin, GPIO.LOW)
            time.sleep(5)
            menu()
    elif choice == 2:
            print ("LED turning off...")
            setup()
            GPIO.output(LedPin, GPIO.HIGH)
            time.sleep(5)
            menu()
    elif choice == 3:
            print ("Shutting down program...")
            destroy()
    else:    ## default ##
            print ("Invalid number. Try again...")
            time.sleep(2)
            menu()

# Define a setup function for some setup
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set LedPin's mode to output, 
    # and initial level to High(3.3v)
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
    # Print messages
    print_message()
    while True:
        print('LED ON')
        # Turn on LED
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(0.5)
        print('LED OFF')
        # Turn off LED
        GPIO.output(LedPin, GPIO.HIGH) 
        time.sleep(0.5)

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
    # Turn off LED
    GPIO.output(LedPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()                     

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()