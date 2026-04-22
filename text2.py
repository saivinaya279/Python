"""Section D — Real-Time Coding Questions 
Question 1 — 
Student Management Create class: 
Student Attributes: name marks
Method: grade() If marks > 50 → Pass Else → Fail --- """
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks > 50:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")


s1 = Student("Sai", 60)
s2 = Student("vinaya", 40)

s1.grade()
s2.grade()
"""Question 2 — ATM Machine Create class: ATM Methods: deposit() withdraw() check_balance() Use encapsulation. 
"""
"""Question 3 — Employee System Parent Class: Employee Method: work() Child Class: Developer Manager Override method."""
class Employee:
    
    def work(self):
        print("Employee works")


class Developer(Employee):
    
    def work(self):
        print("Developer writes code")


class Manager(Employee):
    
    def work(self):
        print("Manager manages team")


d = Developer()
m = Manager()

d.work()
m.work()
"""Question 4 — Shape Example (Abstraction) Create Abstract Class: Shape Method: area() Create child classes: Circle Rectangle --- 
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    
    def area(self):
        print("Area of Circle")


class Rectangle(Shape):
    
    def area(self):
        print("Area of Rectangle")


c = Circle()
r = Rectangle()

c.area()
r.area()
"""Question 5 — Shopping Cart Create class: Product Attributes: name price Method: display() Create 3 objects."""
class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Name:", self.name)
        print("price",self.price)

p1 = Product("Pen", 10)
p2 = Product("Book", 50)
p3 = Product("Bag", 500)

p1.display()
p2.display()
p3.display()