#!/usr/bin/env python

# val = input("Enter your value: ") 
# print(val)

# menu
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
        print ("Starting backup...")
elif choice == 2:
		print ("Starting user management...")
elif choice == 3:
        print ("Rebooting the server...")
else:    ## default ##
        print ("Invalid number. Try again...")