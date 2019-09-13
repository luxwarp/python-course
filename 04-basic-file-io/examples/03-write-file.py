#!/usr/bin/env python3

# check the example file 01-read-file.py first

# To write data to a file in python you need to open the file in
# mode = w
# if the file does not exist, python will create it.
# if the file does exist, all data inside it will be overwritten.

import os

text_to_write = "I will overwrite any existing text."

# first open file and read it.
with open(os.path.dirname(__file__)+"/textfile.txt") as f:
    content = f.read()
    print("Content before write:", content)

# then open the file in write mode and overwrite it's content with the
# value inside variable text_to_write
with open(os.path.dirname(__file__)+"/textfile.txt", mode="w") as f:
    f.write(text_to_write+"\n")

# lastly open the file and read the content again.
with open(os.path.dirname(__file__)+"/textfile.txt") as f:
    content2 = f.read()
    print("Content after write:", content2)
