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