# Next, add a walk() method to both the Pets and Dog classes so that when you call the method on the Pets class, each
# dog instance assigned to the Pets class will walk(). Save this as dog_walking.py. This is slightly more difficult.
#
# Start by implementing the method in the same manner as the speak() method. As for the method in the Pets class, you
# will need to iterate through the list of dogs, then call the method itself.
#
# The output should look like this:
#
# Tom is walking!
# Fletcher is walking!
# Larry is walking!

#Parent Class
# class Pets:
#
#     dogs = []
#
#     def __init__(self, dogs):
#         self.dogs = dogs
#
# class Dog:
#
#     # Class attribute
#     species = 'mammal'
#
#     # Initializer / Instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # instance method
#     def description(self):
#         return "{} is {} years old".format(self.name, self.age)
#
#     # instance method
#     def speak(self, sound):
#         return "{} says {}".format(self.name, sound)
#
#     isHungry = True
#
#     def eat(self):
#         self.isHungry = False
#
# # Child class (inherits from Dog class)
# class RussellTerrier(Dog):
#     def run(self, speed):
#         return "{} runs {}".format(self.name, speed)
#
# # Child class (inherits from Dog class)
# class Bulldog(Dog):
#     def run(self, speed):
#         return "{} runs {}".format(self.name, speed)
#
# my_dogs = [
#     Bulldog("Tom", 6),
#     RussellTerrier("Fletcher", 7),
#     Dog("Larry", 9)
# ]
#
# # Instantiate the Pets class
# my_pets = Pets(my_dogs)
#
# # Output
# print("I have {} dogs.".format(len(my_pets.dogs)))
# for dog in my_pets.dogs:
#     print("{} is {}.".format(dog.name, dog.age))
#
# print("And they're all {}s, of course.".format(dog.species))
# print(my_pets.dogs)
#
# dogs_Hungry = False
# for dogs in my_pets.dogs:
#     if dogs.isHungry:
#         dogs_Hungry = True
#
# if dogs_Hungry:
#     print("My dogs are Hungry")
# else:
#     print("My dogs are not Hungry.")

#################################################
#################################################
#################################################

class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    isHungry = True

    def eat(self):
        self.isHungry = False

    def walk(self):
        return "%s is walking!" % (self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

# Instantiate the Pet class
my_pets = Pets(my_dogs)

# Output
my_pets.walk()

#################################################
#################################################
#################################################