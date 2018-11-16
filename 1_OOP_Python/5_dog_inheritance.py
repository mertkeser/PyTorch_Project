# Parent Class
class  Dog:

    # Class attribute
    species = "mammal"

    #Initializer / Instance Attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #Instance Method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    #Instance Method
    def speak(self, sound):
        return "{} sounds {}".format(self.name, sound)

# Child Class
class  RusselTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child Class
class BullDog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child Classses inherit attributes and behaviors from the Parent Class
jim = BullDog("Jim", 12)
print(jim.description())

# Child Classes have spesific attributes and behavior as well
print(jim.run("Slowlly"))
print(jim.speak("bark"))

# Is Jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is Julie an Instance of Dog
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is Johnny Walker an instance of Bulldog()
johnnywalker = RusselTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, BullDog))

# Is Julie and instance of Jim?
#print(isinstance(julie, Jim))

