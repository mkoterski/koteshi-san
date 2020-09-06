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
print("{} is a lovely fruit."format(fruit))

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


















