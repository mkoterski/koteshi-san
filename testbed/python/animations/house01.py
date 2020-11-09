#!/usr/bin/python
#
# Found on https://stackoverflow.com/questions/60783120/ascii-animation-on-python?newreg=8b4d890d592a4f678e3b64f3d918c288

import time
import platform    # Used by clear_screen
import subprocess  # Used by clear_screen

# System independent clear screen function
# https://stackoverflow.com/questions/18937058/#42877403
def clear_screen():
    command = "cls" if platform.system().lower()=="windows" else "clear"
    return subprocess.call(command) == 0

def smoke():
    # You could use the random package for a more realistic effect
    # https://docs.python.org/3/library/random.html

    shift = 15 + smoke.shift
    print(" "*(shift+2)+"(")
    print(" "*(shift  )+")")
    print(" "*(shift+2)+"(")
    print(" "*(shift  )+")")

    # Next shift using current direction
    smoke.shift += smoke.direction

    # Change direction if out of limits
    if smoke.shift>3 or smoke.shift<-2:
        smoke.direction *= -1

def house():
    print("     __________| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /     A Horror Game   \\")
    print("  |    By: A.D & T.P    |")
    print("  |     ____     ___    |")
    print("  |    |    |   |___|   |")
    print("__|____|____|___________|__")
    print()

# MAIN CODE

smoke.shift = 0
smoke.direction = 1 # could be 1 or -1


# print('\033[2J') # One possible method to clear the screen
clear_screen()

# Infinite loop. Use CTR-C to stop
while True:   
    smoke()
    house()
    time.sleep(1)
    clear_screen()