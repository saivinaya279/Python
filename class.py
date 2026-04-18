""""# Create class Car with attributes
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
# Print object info using method
class Book:
    def __init__(self, title):
        self.title = title

    def show(self):
        print(self.title)

b = Book("Python")
b.show()
# Store multiple objects in list
class Student:
    def __init__(self, name):
        self.name = name

students = [Student("A"), Student("B")]

for s in students:
    print(s.name)"""
"""
class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(self.name,"is barking")
d1=Dog("tommy")
d2=Dog("leo") 
d1.bark()
d2.bark()
 class A:
    def show(self):
        print("Hello")

A.show()
class A:
    def show(self):
        print("Hello")

a1 = A()
A.show(a1)"""
class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("name",self.name)
s1=Student("ram")
s1.display()
class Car:
    def __init__(self,brand):
        self.brand=brand
    def show(self):
        print("The Car Brand Name is ",self.brand)
c1=Car("BMW")
c1.show()
c2=Car("Honda")
c2.show()
class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"{self.name} is barking")
d1=Dog("Tommy")
d1.bark()
"""Mobile Class
Store price
Method show_price()"""
class Mobile:
    def __init__(self,price):
        self.price=price
    def show_price(self):
        print("The Price of the Mobile",self.price)
p1=Mobile(20000)
p1.show_price()
"""5️⃣ Book Class
Store title
Method read() → print "Reading <title>"
"""
class Book:
    def __init__(self,title):
        self.title=title
    def read(self):
        print(f"Reading {self.title}")
B1=Book("The Love Story ")
B1.read()
        
"""
🔹 INTERMEDIATE (Understand self properly)
6️⃣ Person Class
Store name, age
Method show_details() → print both
7️⃣ Laptop Class
Store brand, ram
Method display() → print details
🔹 LOGIC BASED (IMPORTANT)
8️⃣ Bank System (VERY IMPORTANT)

Create class Bank:

balance
Method deposit(amount)
Method withdraw(amount)
Method show_balance()

👉 Test:

deposit
withdraw
print balance
9️⃣ Student Marks

