#!/usr/bin/env python3


class Dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age


my_dog = Dog(breed="Lab", name="Aida", age=7)

print(f"My dog {my_dog.name} is a {my_dog.breed}, born {my_dog.age} years ago.")
