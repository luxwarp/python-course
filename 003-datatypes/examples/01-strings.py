#!/usr/bin/env python3

# Strings (str) are values that contain text like, "hey", "hey ho!", "i love number 13"

print("Hello you!")
print("Nice, I see you at 12 pm.")
print("Do you like pi? 3.14....")

# you can also combine strings
print("Hello " + "world")

# However you cannot do this.
# It will generate an error like "TypeError: can't multiply sequence by non-int of type 'str'"
# print("Hello" * "world")

# But you can do this.
# The len() functions counts how many characters the string has and returns a number that
# then multiplies "Hello" 5 times to the console.
print("Hello " * len("world"))
