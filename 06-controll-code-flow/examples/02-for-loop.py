#!/usr/bin/env python3

# Python code executes from top to bottom.
# By putting if, for, and while statements
# you can controll how code gets executed.

# Note! python does not use curly brackets for wrapping
# statements like if, for, while and functions.
# Python use only indentations. Like it or not, thats the syntax!

# for loops is used to iterate through for example a list.

awesome_list = [1, 2, 3, 4, 5, 6, 7]

for item in awesome_list:
    print(item)

# now you don't need to use the item variable. You can use
# the iterateable items just to create a loop and
# maybe print out hello 7 times.

for item in awesome_list:
    print("hello")
