#!/usr/bin/env python3

# tuples is a type of list.
# tuples is immutable.
# the structure of a tuple: (1, "nice work", 2.3, [1,2,"hey"])

my_tuple = ("hey", 1, 2, "hey ho!", "hey", "hey")
print("My tuple:", my_tuple)

# to get a tuple value use it's index
print("Second item in my_tuple:", my_tuple[1])

# to count how many times a values appears in a tuple: tuple.count(value)
# returns 0 if no values exists.
print("How many 'hey' in my_tuple:", my_tuple.count("hey"))

# go get the index value of a tuple item. tuple.index(value)
# if value does not exist you will get an error like "ValueError: tuple.index(x): x not in tuple"
print("Index position of 'hey ho!' in my_tuple:", my_tuple.index("hey ho!"))

# tuples are immutable so you cannot reassign a value like
# my_tuple[2] = "wop wop"
# TypeError: 'tuple' object does not support item assignment
