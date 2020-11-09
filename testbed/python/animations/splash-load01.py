
#My Progress Bar - www.101computing.net/splash-screen-and-progress-bar
import os
import time

def progress_bar(seconds):
  for progress in range(0,seconds+1):
    percent = (progress * 100) // seconds
    print("\n")
    print("Loading...")
    print("<" + ("=" * progress) + (" " * (seconds-progress)) + "> " + str(percent) + "%")
    print("\n")
    time.sleep(1)
    os.system('clear')  
  
  
# Main Program Starts Here....
progress_bar(10)
username=input("Please enter your username: ")
