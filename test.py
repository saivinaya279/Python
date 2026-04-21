"""Create a class Student

Attributes:

name

marks

Method:

display()
"""
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("The name of the student",self.name)
        print("The marks of student ",self.marks)
S1=Student("Ram",300)
S1.display()
"""Create 2 objects and print details.

Question 2 — Constructor

Create class Employee

Constructor should accept:

name

salary

Method:

show_details()

"""

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print("The Name of the Employee ",self.name)
        print("The Salary of the Employee",self.salary)
E1=Employee("vinaya",20000)
E1.show_details()
"""Question 3 — Encapsulation

Create class Bank

Private variable:

balance

Methods:

deposit()

withdraw()

show_balance()
"""
class Bank:
    
    def __init__(self):
        self.__balance = 0   

    def deposit(self, amount):
        self.__balance = amount

    def withdraw(self, amount):
        self.__balance = amount

    def show_balance(self):
        print("Balance:", self.__balance)


# Create object
b = Bank()

b.deposit(1000)
b.show_balance()

b.withdraw(500)
b.show_balance()



"""Question 4 — Inheritance

Create Parent Class:

Vehicle
Method:

start()

Create Child Class:

Car
Method:

drive()

"""
class Vechile:
    def start(self):
        print("the vechile is started")
class Car(Vechile):
    def drive(self):
        print('the car started')
C1=Car()
C1.start()
C1.drive()
"""
Question 5 — Polymorphism

Create class:

Animal

Method:

sound()

Create child classes:

Dog

Cat

Override sound() method.
"""
class Animal:
    def sound(self):
        print("the sound of animal")
class Dog(Animal):
    def sound(self):
        print("the Dog barks")
class Cat(Animal):
    def sound(self):
        print("the Cat say Meow")
D=Dog()
C=Cat()
D.sound()
C.sound()
""""""
"""Question 1 — Student Management

Create class:

Student

Attributes:

name

marks

Method:

grade()

If marks > 50 → Pass
Else → Fail

---
"""
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
class Test:
    def __init__(self):
        print("Constructor called")

t = Test()
