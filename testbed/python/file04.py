#!/usr/bin/python
#
# When reading from a file, it follows the sequence of open, read, and no (?) close
#
#
# Sample Output:
# pi@koteshi-san:/koteshi-san/testbed/python $ sudo python3 file04.py 
# ['Sample text to save!\n', '\n', 'Append sample text to an existing file!\n', 'Append sample text to an existing file!']

# Returns a list
Read_me = open("example_file.txt","r").readlines() # "r" read, "w" write, or "a" append

print(Read_me)
