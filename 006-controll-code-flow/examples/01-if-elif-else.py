#!/usr/bin/env python3

# Python code executes from top to bottom.
# By putting if, for, and while statements
# you can controll how code gets executed.

# Note! python does not use curly brackets for wrapping
# statements like if, for, while and functions.
# Python use only indentations. Like it or not, thats the syntax!

# if statement runs if some criteria is True.
name = "Luxwarp"

if name == "Mikael":
    print("Hello", name)

print("Goodbye")

if name == "Luxwarp":
    print("Hello Luxwarp")

# else statement runs if the if statement is False.
number = 2

if number < 2:
    print("It's less.")
else:
    print("It's not less.")

# chaining multiple if statements with elif
if name != "Luxwarp":
    print("You are not Luxwarp")
elif number <= 1:
    print("Crap numbers is less than or equal to 1.")
elif number >= 1:
    print("But hey, number is greater than or equal to 1.")
else:
    print("Ehm, I don't know how I feel about this.")
