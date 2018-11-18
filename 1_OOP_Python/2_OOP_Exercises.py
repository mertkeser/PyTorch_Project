# In this exercise, methods are explained. Description and Speak method inside of the Dog class is created and usage
# of this methods are shown.

class Dog:

    #Class Attribute
    species = 'mammal'


    #Initializer/Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance Method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    #instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

#Instantianete Dog Object
philo = Dog('Philo', 5)
mikey = Dog('Mikey', 6)

#Access the instance attributes
print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age ))

#Is Philo a mammal?
if philo.species == "mammal":
    print("{} is a {}!".format(philo.name, philo.species))

print(philo.description())
print(philo.speak('bark'))