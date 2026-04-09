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
# Inheritance one:
class A:
    def msg(self):
        print("Hello")

class B(A):
    pass

b = B()
b.msg()
# Polymorphism one:
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

obj = B()
obj.show()
"""# Abstraction (Simple program)

Question: Write a Python program using abstraction."""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def area(self):
        print("Area calculated")

obj = Square()
obj.area()
"""Function Polymorphism (Same function, different data)
📌 Problem:

Add numbers or strings"""

def add(a, b):
    return a + b

print(add(2, 3))        # numbers
print(add("Hi ", "You"))  # strings