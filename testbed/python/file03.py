file03.py

#!/usr/bin/python
#
# When reading from a file, it follows the sequence of open, read, and no (?) close
#
#

Read_me = open("example_file.txt","r").read() # "r" read, "w" write, or "a" append

# Returns a list
#Read_me = open("example_file.txt","r").readlines() # "r" read, "w" write, or "a" append

Print(Read_me)