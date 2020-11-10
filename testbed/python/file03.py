#!/usr/bin/python
#
# When reading from a file, it follows the sequence of open, read, and no (?) close
#
# Sample Output:
#pi@koteshi-san:/koteshi-san/testbed/python $ sudo python3 file03.py 
# Sample text to save!

# Append sample text to an existing file!
# Append sample text to an existing file!

Read_me = open("example_file.txt","r").read() # "r" read, "w" write, or "a" append

# Returns a list
#Read_me = open("example_file.txt","r").readlines() # "r" read, "w" write, or "a" append

print(Read_me)
