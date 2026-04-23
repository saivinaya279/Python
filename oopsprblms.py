"""1. Class & Object
Create a class Student
Attributes:
name
age
marks
Method:
display()
Create 3 objects and print details."""
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("the name of student",self.name)
        print(f'the marks {self.marks} of the student {self.name}')
        print("the age ",self.age)
d1=Student("ram",10,100)
d1.display()

"""2. Constructor
Create class Employee
Constructor should accept:
name
department
salary
Create method:
show_details()
Create 2 objects."""
class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def show_details(self):
        print(f"The employee {self.name} working in the department {self.department},will get {self.salary} salary every month")
e1=Employee("vinaya","DS ",20000)
e1.show_details()
"""5. Inheritance (Single Inheritance)
Create Parent class:
Person
Attributes:
name
age
Method:
display()
Create Child class:
Student
Add:
marks
Create object and display details."""
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class child(parent):
    def display(self,marks):
        self.marks=marks
        print(f"{self.name} is the student of  age {self.age} gained {self.marks} marks")
c1=child("ram",20)
c1.display(200)
"""6. Inheritance (Multilevel)
Create:
Grandparent → Animal
Parent → Dog
Child → Puppy
Methods:
Animal → eat()
Dog → bark()
Puppy → weep()
Create object and call all methods."""
class Animal:
    def eat(self):
        print("it is a animal")
class Dog(Animal):
    def bark(self):
        print("the dog bark")
class Puppy(Dog):
    def weep(self):
        print("the puppy is weeping")
p=Puppy()
p.eat()
p.bark()
p.weep()

"""7. Polymorphism (Method Overriding)
Create Parent class:
Shape
Method:
draw()
Create Child classes:
Circle
Rectangle
Override draw() method."""
class Shape:
    def draw(self):
        print("The shape of image")
class Circle(Shape):
    def draw(self):
        print("these is a circle")
class Rectangle(Shape):
    def draw(self):
        print("these is a rectangle")
r=Circle()
c=Rectangle()
c.draw()
r.draw()