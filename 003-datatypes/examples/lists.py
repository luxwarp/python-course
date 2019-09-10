#!/usr/bin/env python3

# Lists are pythons version of arrays

# Lists are ordered. A list can contain different object types.
# This is a list structure.
# ["a string", 20, 0.32]

cities = ["Gothenburg", "Stockholm"]
print("Cities:", cities)

numbers = [1, 2, 3, 4]
print("Numbers:", numbers)

characters = ["a", "b", "c"]
print("Characters:", characters)

# To add a new item to a list
characters.append("d")
print("Characters with new item:", characters)

# to delete last item of a list ang get it's value
removed_number = numbers.pop()
print("Numbers after pop:", numbers)
print("Removed number:", removed_number)

# print only first items value of list
print("First city value:", cities[0])
# or print the list as a list but exclude everything but the first item.
print("First city as a list:", cities[0:1])

# change a value of a list item
cities[1] = "Alingsås"
print("Cities after value change:", cities)

# concatenate lists. (merge multiple lists to one.)
concatenated_lists = cities + numbers
print("Concatenated lists:", concatenated_lists)
