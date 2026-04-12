# Create class Car with attributes
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

c1 = Car("BMW", 5000000)
print(c1.brand, c1.price)
# Add method to display details
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s = Student("Sai")
s.display()
# Create multiple objects
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("A")
p2 = Person("B")
print(p1.name, p2.name)
# Modify object attribute
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Tom")
d.name = "Jerry"
print(d.name)
# Class with default value
class Employee:
    def __init__(self, name, salary=10000):
        self.name = name
        self.salary = salary

e = Employee("Ram")
print(e.salary)