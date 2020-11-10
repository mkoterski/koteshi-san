#!/usr/bin/python
#
# When writing a file, it follows the sequence of open, write, close
#
#

text_to_write = "Sample text to save!\n" # \n for line break

save_file = open("example_file.txt","w") # "r" read, "w" write, or "a" append

save_file.write(text_to_write)

save_file.close()
