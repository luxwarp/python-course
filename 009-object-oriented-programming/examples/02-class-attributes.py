#!/usr/bin/env python3


class Dog:

    # this is a class object attribute. It will be the same for
    # all class instances. Like a global variable for this class.
    category = "animal"

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age


my_dog = Dog(breed="Lab", name="Aida", age=7)

print(f"My dog {my_dog.name} is an {my_dog.breed}, born {my_dog.age} years ago. A dog is an {my_dog.category}")
