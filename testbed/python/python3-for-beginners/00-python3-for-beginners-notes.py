Basic OOP
Every object has a type
"apple" is an object of the type "str"
"apple" is a string object
fruit = "apple"
fruit is a string object
Methods are functions run against an object
object.method()



S T R I N G S   A N D   V A R I A B L E S 

The lower() String Method
fruit = "Apple"
print (fruit.lower())

# object fruit changed to lowercase
>>> apple


String Concatenation

print ("I " + "love " + "Python")
print ("I" + " love" + " Python")

>>> I love Python

first = "I"
second = "love"
third = "Python"

sequence = first + " " + second + " " + third + "."

>>> I love Python.


Repating Strings

print("-" * 10)

>>> ----------

happiness = "happy" * 3
print(happiness)

>>> happy happy happy


The str() Function

#without str() below command would error out as version type is of integer
#instead of string which is needed for print()
version = 3
print("I love Python " + str(version) + ".")

>>> I love Python 3.


Formatting Strings

print("I {} Python.".format("love"))
print("{} {} {}".format("I", "love", "Python."))

>>> I love Python #same output

print("I {0} {1}. {1} {0}s me.".format("love", "Python"))

>>> I love Python. Python loves me.

first = "I"
second = "love"
third = "Python"
print("{} {} {}.").format(first, second, third)

>>> I love Python

version = 3
print("I love Python {}.".format(version))

>>> I love Python 3


Formatting Strings
print("{0:8} | {1:8}".format("Fruit", "Quantity"))
print("{0:8} | {1:8}".format("Apples", "3"))
print("{0:8} | {1:8}".format("Oranges", "10"))

>>> Fruit   | Quantity
    Apples  | 3
    Oranges | 10


Formatting String - Alignment
< left
^ center
> right

print("{0:8} | {1:<8}".format("Fruit", "Quantity"))
print("{0:8} | {1:<8}".format("Apples", "3"))
print("{0:8} | {1:<8}".format("Oranges", "10"))

>>> Fruit   | Quantity
    Apples  | 3
    Oranges | 10


f    Float
.Nf  N = The number of decimal spaces

Example:
{:.2f}

print("{0:8} | {1:<8}".format("Fruit", "Price in EUR"))
print("{0:8} | {1:<8.2}".format("Apples", 0.87123))
print("{0:8} | {1:<8.2}".format("Oranges", 1))

>>> Fruit   | Price in EUR
    Apples  | 0.87
    Oranges | 1.00


Getting User Input
input()    Accepts Standard Input

input("Prompt to display")

fruit = input("Enter a name of a Fruit: ")
print("{} is a lovely fruit.".format(fruit))

>>> Name a fruit: apple
    apple is a lovely fruit.


Summary
- Variables are names that store values.
- Variables must start with a letter, but may contain numbers and underscores.
- Assign values to variables using the 
  variable_name = value syntax
- Strings are surrounded by quotation marks
- Each character in a string is assigned an index
- A function is reusable code that performs an action
- Built-in functions:
-- print() : Display values
-- len() : Returns the length of an item
-- str() : Returns a string object
-- input() : Reads a string
- Everything in Python is an object
- Objects can have methods
- Methods are functions that operate on an object
- String methods:
-- upper() : Returns a copy of the string in uppercase.
-- lower() : Returns a copy of the string in lowercase.
-- format() : Returns a formatted version of the string.



N U M B E R S   A N D   M A T H

Numbers do not use quotation marks

int = 42  # integer
float = 1.23   # floating point

SYMBOL OPERATION     
+      add
-      subtract
*      multiply
/      divide        # performs floating point operation and returns floating point value
**     exponentiate  # 2 ** 5 means 2 * 2 * 2 * 2 * 2 "2 raised by the power of 5"
%      modulo        # 3 % 2 = 1 means 3 divided by 2 leaves 1 remaining
                     # 4 % 2 = 0  means 4 divided by 2 leaves 0 remaining
                     # returns the remainder

Divisions performs floating point operations and returns floating point values
8 / 2 = 4.0

Operations with floating point values return floating point results
1 + 2.0 = 3.0


Strings and Numbers

Convert strings to integers
int()

Example:
quantity_string = "3"
total = int(quantity_string) + 2 # without int() this would result in an error as 3 is a string due to "" marks
print(total)

>>> 5

Convert strings or integers to floating points
float()

Example:
meters = "3"
total = float(meters) # float() add decimals
print(total)

>>> 3.0

Summary
- Unlike strings, numbers require no special decoration
- If you enclose a number with quotation marks, it will become a string
- To convert a string to to an integer, use the int() function
- To convert a string to to a float, use the float() function
- Single line comments begin with #
- Multi-line comments begin with (""") and end with (""")



B O O L E A N S   A N D   C O N D I T I O N A L S

Boolean
- Can only be True or False
a_boolean = True
the_other_boolean = False
print(a_boolean)
print(the_other_boolean)

>>> True
    False

Comparators:

OPERATOR   DESCRIPTION
==         equal to
>          greater than
>=         greater than or equal
<          less than     
<=         less than or equal
!=         not equal

>>> 1 == 2
    False

>>> 1 > 2
    False

>>> 1 >= 2
    False

>>> 1 < 2
    True

>>> 1 <= 2
    True

>>> 1 != 2
    True


Boolean Operators:

OPERATOR   DESCRIPTION     
and        Evaluates to True if both statements are true, otherwise evaluates to False
or         Evaluates to True if either of the statements is True, otherwise evaluates to False
not        Evaluates to the opposite of the statement

>>> 37 > 29
    True

>>> 37 < 42
    True

>>> 37 > 29 and 37 < 42 # both statements are true therefore the result is True
    True

>>> 37 > 29 or 37 < 42 # if one statement is True the result is True
                       # both statements are true therefore the result is True
    True

>>> not 37 > 29 # While 37 > 29 is True, not evaluates to the opposite statement
    False


Order of Operations for Booleans
not
and
or

# This is True
True and False or not False
True and False or True
False or True


Controlling the Order of Operations

Anything surrounded by parenthesis is evaluated first and as its own unit.

# These are the same
True and False or not False
(True and False) or (not False)
((True and False) or (not False))


Conditionals

>>> if 37 < 40:
	    print("Thirty-seven is less than 40.") # Pay attention at indentation
    Thirty-seven is less than 40.


Code Blocks

Block One
    Block Two
    Block Two
        Block Three
Block One
Block One

# Remember those 
IndentationError: expected an indented block


The if Statement

Example 1:
>>> age = 31
    if age >= 35:
	    print("You are old enough to be US president")


    print("Have a nice day.")
    Have a nice day.


Example 2:
>>> age = 31
    if age >= 35:
	    print("You are old enough to be US president.")
	else:
		print("You are NOT old enough to be US president.")


    print("Have a nice day.")
    You are NOT old enough to be US president.
    Have a nice day.


Example 3:
>>> age = 31
    if age >= 35:
	    print("You are old enough to be a US Senator or the US President.")
	elif age >= 30:
		print("You are old enough to be a US Senator.")
	else:
		print("You are NOT old enough to be a US Senator or the US President.")


    print("Have a nice day.")
    
	You are old enough to be a US Senator.
    Have a nice day.


Example 4:
>>> age = 99
    if age >= 35:
	    print("You are old enough to be a US Representative, a US Senator or the US President.")
	elif age >= 30:
		print("You are old enough to be a US Senator.")
	elif age >= 25:
		print("You are old enough to be a US Representative.")
	else:
		print("You are NOT old enough to be a US Representative, a US Senator or the US President.")


    print("Have a nice day.")
    
	You are old enough to be a US Representative, a US Senator or the US President.
    Have a nice day.



F U N C T I O N S

Functions - Part I

Functions
- Dry = Don't Repeat Yourself
- Write one time, use many times
- what has been defined, has to be called
- Define your functions at the top of your programm

>>> def function_name():
        # Code Block

>>> def say_hi(): # defines function
        print("Hi!")

    say_hi() # calls function


    Hi!

>>> def say_hi(name): # defines function with parameter "name"
        print("Hi {}!".format(name))

    say_hi("Jayson") # calls function
    say_hi("everybody") # calls function with everybody applied to name parameter


    Hi Jayson!
    Hi everybody!

>>> def say_hi(name): # defines function
        print("Hi {}!".format(name))

    say_hi() # calls function without parameter "name"
    

    Error
    TypeError: say_hi() missing 1 required positional argument 'name'

>>> def say_hi(name = "there"): # defines function with parameter "name"
        print("Hi {}!".format(name))

    say_hi() # calls function without parameter value, therefore defaults to value "there"
    say_hi("Jayson") # calls function with "Jayson" applied to "name" parameter


    Hi there!
    Hi Jayson!

>>> def say_hi(first, last):
        print("Hi {} {}!".format(first, last))

    say_hi("Candice", "Yang")
    

    Hi Candice Yang!

>>> def say_hi(first, last): # We define here the parameter order
        print("Hi {} {}!".format(first, last))

    say_hi(first = "Candice", last = "Yang")
    say_hi(last = "Koterski", last = "Matthias") # Definition order doesn't matter since the we pre-
                                                 # defined the order when we define the function

    Hi Candice Yang!
    Hi Matthias Koterski!

>>> def say_hi(first, last = "Yang"): # "last" default value is "Yang" unless overwritten by function call parameters
        print("Hi {} {}!".format(first, last))

    say_hi("Candice")
    say_hi("Matthias", "Koterski")


    Hi Candice Yang!
    Hi Matthias Koterski!








Functions - Part II

Functions
doc strings are notes which can we parsed by help() and should tell you about the function's purpose

>>> def odd_or_even(number):
        """ Determine if the number is odd or even """
        if number % 2 == 0:
            return "even"
        else:
            return "odd"


    odd_or_even_string = odd_or_even(7)
    print(odd_or_even_string)

>>> def is_odd(number):
        """ Determine if the number is odd """
        if number % 2 = 0:
            return False
        else:
            return True

    print(is_odd(7))


    True

>>> def get_name():
        name = input("What is your name? ")
        return name

    def say_name(name):
        print("Your name is {}.".format(name))

    def get_and_say_name():
        """ Get and display name """
        name = get_name()
        say_name(name)

    get_and_say_name()


    What is your name? Matthias
    Your name is Matthias.

Summary
- A function is a block of reuseable code that performs and action
  and can optionally return data.
- A function must be defined before it is called.
- The basic syntax for defining a function is:

def function_name(parameter_name):

- A function can accept parameters. To make a parameter optional, supply a default value for that parameter
- You can supply a docstring as the first line of your function
- The return statement exits the function and passes back what follows return.
- Use the built-in help() function to get help with an object. When supplying a function
  to help() the docstring contained within the function is displayed.



L I S T S

Lists
- A list is a data type that can hold an ordered collection of items
- The items can be of various data types
- You can even have lists of lists

Creating Lists

list_name = [item_1, item_2, item_N]    # Creates a list with items
list_name = []                          # Creates empty list
list_name[index]                        # index#0 is the first item




















