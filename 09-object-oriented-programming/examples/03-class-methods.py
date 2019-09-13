#!/usr/bin/env python3


class Dog:

    category = "animal"

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    # this is a method. A method is just like a function
    # but it's defined inside a class and can be called from
    # the outside. You always need to pass in self as a parameter.
    def bark(self):
        print("Woof!")

    def translate(self, dogword=None):
        if dogword == "WOOF!":
            print("I don't like you!")
        elif dogword == "Woof":
            print("Throw the ball, I will catch it!")
        else:
            print("I'm hungry again!")


my_dog = Dog(breed="Lab", name="Aida", age=7)

print(f"My dog {my_dog.name} is an {my_dog.breed}, born {my_dog.age} years ago. A dog is an {my_dog.category}")
print("Let's see if we can make my dog bark.")
my_dog.bark()

print("Hey you cute dog!")
my_dog.translate("WOOF!")

print("Are you ready?")
my_dog.translate("Woof")

print("What are you saying?")
my_dog.translate()
