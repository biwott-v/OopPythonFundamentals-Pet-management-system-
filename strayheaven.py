'''class Pet:
    def __init__(self,sound):
        self.sound = sound
    def makeSound(self):
        return "{0} {1} {2}".format(self.sound,self.sound,self.sound)
    def __str__():
        return f"I make the {self.sound, self.sound} sound"
        
class Dog(Pet):
    pass

class Cat(Pet):
    def __init__(self,name,sound):
        super().__init__(sound)
        self.name=name

class Rat:
    pass


mydog = Dog("woof")
print(mydog.sound)
print(mydog.makeSound())'''



'''class Pet:
    def bark():
        return "woof"

mypet = Pet
print(mypet)
mypet.bark()
'''

#class initialization with defaylt __init
class Pet:
    def speak(self):
        print("sound made")

rasmus = Pet()
rasmus.name = "Rasmus"
print(rasmus.name)
rasmus.speak()
#A simple class to represent a dog with modified __init__

class Dog:
    def __init__(self,name,breed,age="N/A"):
        self.name = name
        self.age = age
        self.breed = breed
    def speak (self):
        return f"{self.name} says woof! woof!"

class Cat:
    pass

class Rat:
    pass

amad= Dog("amad","Black goat")
koba = Dog("koba","Great Dane","3")
print(koba.name)
print(koba.speak())
print(koba.age)
print(amad.age)
