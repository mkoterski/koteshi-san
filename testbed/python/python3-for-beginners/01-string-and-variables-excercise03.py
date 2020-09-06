#!/usr/bin/env python3
# Strings and Variables - Excercise 03:
#
# Write a Python program that prompts for input and displays a cat "saying" what was provided by
# the user. Place the input provided by the user inside a speech bubble. Make the speech bubble
# expand or contract to fit around the input provided by the user.
#
# Created: 2020-09-06
# Updated: 2020-09-06
# By:      Matthias Koterski

# Original attempt
# dataentry = str(input("What does the cat say? "))
# print("")
# print("           |" + "-" * 10 + "|")
# print("           |   " + dataentry + " |")
# print("           |" + "-" * 10 + "|")
# print(" /---.     |")
# print("( o.o )  --")
# print(" > ^ <")
# print("")

# New attempt respecting the automatic extension of the speech bubble

text = input('What does the cat say? ')
text_length = len(text)

print('            {}'.format('_' * text_length))
print('          < {} >'.format(text))
print('            {}'.format('-' * text_length))
print('          /')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')

# Output Result
# What does the cat say? Meow
#             ____
#           < Meow >
#             ----
#           /
#  /\_/\   /
# ( o.o )
#  > ^ <