# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

# now call function we defined above 
clear() 

# menu
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')
 
## Get input ###
#choice = raw_input('Enter your choice [1-3] : ') # Python 2 version
choice = input('Enter your choice [1-3] : ') # Python 3 version

### Convert string to int type ##
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