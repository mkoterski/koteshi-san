#!/usr/bin/python
#
# When writing to files, it follows the sequence of open, write, close
#
#

import time

text_to_write = "Sample text to save!\n" # \n for line break

save_file = open("example_file.txt","w") # "r" read, "w" write, or "a" append

save_file.write(text_to_write)

save_file.close()
