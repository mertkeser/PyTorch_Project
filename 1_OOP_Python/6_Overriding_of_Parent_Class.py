# This is the exercise for Showing Overriding
class Dog:
    species = "Mammal"

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = "reptile"

frank = SomeBreed()
print(frank.species)
beans = SomeOtherBreed()
print(beans.species)
