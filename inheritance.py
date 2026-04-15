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
"""Problem

Create Person class with name and age.
Create Student class with roll number."""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll = roll

s = Student("Ravi",20,45)

print(s.name)
print(s.age)
print(s.roll)
# Override parent method.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

c = Car()
c.start()
# Call both parent and child methods.
class Shape:
    def display(self):
        print("This is shape")

class Circle(Shape):
    def show(self):
        print("This is circle")

c = Circle()

c.display()
c.show()
"""Create a parent class Animal and child class Dog

Program:
"""
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()
# Multilevel inheritance example

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

p = Puppy()

p.eat()
p.bark()
p.weep()
"""Hierarchical inheritance

Program:"""

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()
"""Abstract class example

Python uses ABC module.

Program:"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts with key")

c = Car()
c.start()
# Abstract class with multiple methods

# Program:

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        print("Area =", self.side*self.side)

s = Square(5)
s.area()
# Simple inheritance
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    pass

c = Child()
c.show()
# Add child method
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def display(self):
        print("Child")
# Constructor inheritance
class A:
    def __init__(self):
        print("A")

class B(A):
    pass

b = B()
Use super()
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")