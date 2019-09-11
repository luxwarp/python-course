#!/usr/bin/env python3

# Python code executes from top to bottom.
# By putting if, for, and while statements
# you can controll how code gets executed.

# Note! python does not use curly brackets for wrapping
# statements like if, for, while and functions.
# Python use only indentations. Like it or not, thats the syntax!

# While loops is used to run some code as long as some condition is True

number = 0

while number < 3:
    print(f"Hey number: {number} is less then 3.")
    number += 1

# Watch out for infinity loops, they will run for ever.
# this is a common misstake for everyone.
# while True:
#     print("Infinity loop. Watch out!")
