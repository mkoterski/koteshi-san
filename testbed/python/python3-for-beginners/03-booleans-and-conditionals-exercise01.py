#!/usr/bin/env python3
# Booleans and Conditionals - Exercise 01:
#
# Create a program that asks the user how far they want to travel.
# If they want to travel less than three kilometers tell them to walk.
# If they want to travel more than three kilometers, but less than three hundred kilometers, tell them to drive.
# If they want to travel three thousand kilometers or more tell them to fly.
#
# Sample Output:
# How far would you like to travel in kilometers? 2500
# I suggest flying to your destination.
#
# Created: 2020-09-06
# Updated: 2020-09-06
# By:      Matthias Koterski

# Object definition

distance = input("How far would you like to travel in kilometers? ")

# if 
if distance >= 3000:
	print("I suggest you to fly to your destination.")
elif distance >= 3 and < 300:
	print("I suggest you to drive to your destination.")
else
print("I suggest you to walk your destination.")

# Output