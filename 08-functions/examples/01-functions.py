#!/usr/bin/env python3

# Functions are great ways to clean up your
# code and use code pieces multiple times without
# need to rewrite or copy paste.

# to create a function


def printHello():
    print("Hello!")


# now you can call this function to put it to use.
print("Welcome to my app. I'm now going to say hello down below.")
printHello()

# you can also pass parameters to functions.


def greetName(name="Unknown"):
    print("Hello " + name)


print("I'm now going to greet you.")
greetName("Luxwarp")

# you may notice the parameter above has a ="Unknown"
# that is a default value to be applied if no parameter
# is passed when calling the function.
print("I'm now trying to greet you without a name.")
greetName()
