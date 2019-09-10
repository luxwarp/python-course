#!/usr/bin/env python3

# sets is a type of unordered list that can only contain unique values
# set structure: set(value, value, value, etc...)

# create an empty set
my_set = set()

# you can add a value
my_set.add(1)
my_set.add("Hey")

print("My set:", my_set)

# If you try adding a value that already exists it will be ignored.
my_set.add("Hey")
print("My set after adding another 'Hey':", my_set)

# sets are case sensitive.
my_set.add("hey")
print("My set after adding 'hey'", my_set)

# since sets only can contain unique items it's great to
# use set to only get the unique values of a list.

my_duplicate_list = [1, "ho", "hey", 1, 1, "false",
                     2, 2, "hey", "true", "true", "false", "False", ]

my_unique_list = set(my_duplicate_list)
print("My duplicate list:", my_duplicate_list)
print("My unique list as a set:", my_unique_list)

# to print out unique characters from a string
dup_char_string = "Mississippi"
print("Unique characters of string:", dup_char_string)
print(set(dup_char_string))
