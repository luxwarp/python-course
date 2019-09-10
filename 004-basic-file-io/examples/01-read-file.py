#!/usr/bin/env python3

# Reading a text file in python is as easy as open("/path/to/file.txt")
# Important, the file you want to open needs to be located in the same
# directory you run your python script from, or you can use an absolute path to the file.

# to open a text file in python that is located in same directory you are running
# your python script from you can use:
# my_file = open("textfile.txt")

# ( what I preferrer)
# to open a file relative to the location of your python script
# you can use:

import os

my_file = open(os.path.dirname(__file__)+"/textfile.txt")

# by default python open files in read-only mode.
# to get the content of a file
content = my_file.read()
print("Content:", content)

# The content of the file is now assigned to the content variable.
# however if you try to read the file again you will not get any content.
# Thats because python has read the file and pointer in that file is at the end.
# To reset the pointer and be able to read the file again without closeing and
# opening it again you can do:
my_file.seek(0)


# If you want to store each line as a list item you can use:
content_list = my_file.readlines()
print("Content as list:", content_list)

# when you are done using a file you need to close it
# this way you wont get any suspicious errors if you open the file
# somewhere else.
my_file.close()

# if you don't want to think about closing a file after opening it
# you can use pythons "with" statement
with open(os.path.dirname(__file__)+"/textfile.txt") as f:
    content2 = f.read()

print("Second time content:", content2)
