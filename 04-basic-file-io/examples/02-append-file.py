#!/usr/bin/env python3

# check the example file 01-read-file.py first

# To append data to a file in python you need to open the file in
# mode = a.

import os

text_to_append = "I love to be appended to a file."

# first open file and read it.
with open(os.path.dirname(__file__)+"/textfile.txt") as f:
    content = f.read()
    print("Content before append:", content)

# then open the file and append some text.
with open(os.path.dirname(__file__)+"/textfile.txt", mode="a") as f:
    f.write(text_to_append+"\n")

# lastly open the file and read the content again.
with open(os.path.dirname(__file__)+"/textfile.txt") as f:
    content2 = f.read()
    print("Content after append:", content2)
