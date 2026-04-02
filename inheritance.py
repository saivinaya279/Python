"""Problem

Create a parent class Animal with method sound().
Create child class Dog and call the method."""
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()