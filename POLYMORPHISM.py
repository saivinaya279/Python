"""Method overloading (Python way)

Python does not support traditional overloading, but we simulate it.
"""
class Math:

    def add(self,a,b,c=0):
        print(a+b+c)

m = Math()

m.add(2,3)
m.add(2,3,4)
# Method overriding

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()

d.sound()