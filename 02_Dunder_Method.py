#Create a class pets from class Animals and further create class DOG from pets. Add a method bark to class dog

#Multilevel inheritance

class Animals:
    animalType = "Mammal"

class Pets:
    petColor = "White"

class Dog:
    @staticmethod
    def bark():
        print("bow, bow!")

d = Dog()
d.bark()