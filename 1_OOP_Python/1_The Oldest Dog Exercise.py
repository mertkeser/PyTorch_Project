## This is the first Exercise for Python Objects

#Using the same Dog class, instantiate three new dogs, each with a different age.
# Then write a function called, get_biggest_number(), that takes any number of ages (*args) and returns the oldest one.
# Then output the age of the oldest dog like so:

#The oldest dog is 7 years old.

class Dog:

    #class Attribute
    species = "mammal"

    #Initiation of Class
    def __init__(self,name,age):
        self.name = name
        self.age = age

Mikey = Dog("Mikey", 12)
Philo = Dog("Philo", 15)
Lucky = Dog("Lucky", 21)

def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old".format(get_biggest_number(Mikey.age, Philo.age, Lucky.age)))

