#!/usr/bin/python
#
# When appending to a file, it follows the sequence of open, write, close
#
#

append_text = "\nAppend sample text to an existing file!" # \n for line break

append_file = open("example_file.txt","a") # "r" read, "w" write, or "a" append

append_file.write(append_text)

append_file.close()
