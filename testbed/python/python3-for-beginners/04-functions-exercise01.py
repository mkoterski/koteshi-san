#!/usr/bin/env python3
# Func tions - Exercise 01:
#
# Create a fill in the blank word game. Prompt the user to enter a noun, verb, and an adjective.
# Use those responses to fill in the blanks and display the story.
# 
# Write a short story. Remove a noun, verb, and an adjective.
# Create a function to get the input from the user.
# Create a function that fills in the blanks in the story you created.
# Ensure each function contains a docstring.
# After the noun, verb, and adjective have been collected from the user, display the story using
# their input.
#
# Created: 2020-09-06
# Updated: 2020-09-07
# By:      Matthias Koterski

# Original attempt errored out :-(
# print("Welcome to the interactive story teller 0.1")

# def get_user_input():
# 	noun = input("Please enter a noun? ")
# 	verb = input("Please enter a verb? ")
# 	adjective = input("Please enter an adjective? ")

# def display_story():
# 	get_user_input()
# 	print("A Panda met his friend, the crocodile. Both of them were very {0}. All of a sudden they {1} a lot of {2}.".format(adjective, noun, verb))

# display_story()


# Works but user input is not in a separate funtion

# noun = input("Please enter a noun? ")
# verb = input("Please enter a verb? ")
# adjective = input("Please enter an adjective? ")

# def display_story():
# 	print("A Panda met his friend, the crocodile. Both of them were very {0}. All of a sudden they {1} a lot of {2}.".format(adjective, noun, verb))

# display_story()


# New attempt (based on sample solution provided)


def get_user_input(word_type):
	"""Get words from the user"""
	return input("Please enter a/an {}: ".format(word_type))

def fill_in_story(noun, verb, adjective):
	"""Fill in the previously collected words into the story"""
	story = "A {0} met his friend, the crocodile. They wanted to {1}. "\
	        "But in the end they were way too {2}.".format(noun, verb, adjective)
	return story

def display_story(story):
	"""Displays the completed story"""
	print("Here is your creation: \n")
	print(story)

def create_story():
	"""Create the entire workflow (entering words, filling the org story with words and displaying the completed story"""
	noun = get_user_input("noun")
	verb = get_user_input("verb")
	adjective = get_user_input("adjective")
	complete_story = fill_in_story(noun, verb, adjective)
	display_story(complete_story)

create_story()


# Output
# matthias@Candices-MBP python3-for-beginners % python3 04-functions-exercise01.py
# Please enter a/an noun: Sausage
# Please enter a/an verb: run
# Please enter a/an adjective: fast
# Here is your creation: 

# A Sausage met his friend, the crocodile. They wanted to run. But in the end they were way too fast.






# def get_word(word_type):
#     """Get a word from a user and return that word."""

#     # The lower() function converts the string to lowercase before testing it
#     if word_type.lower() == 'adjective':
#         # Use 'an' in front of 'adjective'
#         a_or_an = 'an'
#     else:
#         # Otherwise, use 'a' in front of 'noun' or 'verb'
#         a_or_an = 'a'
#     return input('Enter a word that is {0} {1}: '.format(a_or_an, word_type))


# def fill_in_the_blanks(noun, verb, adjective):
#     """Fills in the blanks and returns a completed story."""

#     # The \ lets the string continue on the next line to make the code easier to read
#     story = "In this course you will learn how to {1}.  " \
#             "It's so easy even a {0} can do it.  " \
#             "Trust me, it will be very {2}.".format(noun, verb, adjective)
#     return story


# def display_story(story):
#     """Displays a story."""
#     print()
#     print('Here is the story you created.  Enjoy!')
#     print()
#     print(story)


# def create_story():
#     """Creates a story by capturing the input and displaying a finished story."""
#     noun = get_word('noun')
#     verb = get_word('verb')
#     adjective = get_word('adjective')

#     the_story = fill_in_the_blanks(noun, verb, adjective)
#     display_story(the_story)

# create_story()









# Provided Sample Solution

# def get_word(word_type):
#     """Get a word from a user and return that word."""

#     # The lower() function converts the string to lowercase before testing it
#     if word_type.lower() == 'adjective':
#         # Use 'an' in front of 'adjective'
#         a_or_an = 'an'
#     else:
#         # Otherwise, use 'a' in front of 'noun' or 'verb'
#         a_or_an = 'a'
#     return input('Enter a word that is {0} {1}: '.format(a_or_an, word_type))


# def fill_in_the_blanks(noun, verb, adjective):
#     """Fills in the blanks and returns a completed story."""

#     # The \ lets the string continue on the next line to make the code easier to read
#     story = "In this course you will learn how to {1}.  " \
#             "It's so easy even a {0} can do it.  " \
#             "Trust me, it will be very {2}.".format(noun, verb, adjective)
#     return story


# def display_story(story):
#     """Displays a story."""
#     print()
#     print('Here is the story you created.  Enjoy!')
#     print()
#     print(story)


# def create_story():
#     """Creates a story by capturing the input and displaying a finished story."""
#     noun = get_word('noun')
#     verb = get_word('verb')
#     adjective = get_word('adjective')

#     the_story = fill_in_the_blanks(noun, verb, adjective)
#     display_story(the_story)

# create_story()


# Output


