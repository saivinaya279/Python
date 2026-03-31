"""class Car:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class red_c(Car): # even though we a pass the parent clss naaame into the child class when the child class contains construct ,it will only prints its own ttributes aand properties cannot access the data from parent claass 
    def __init__(self,color):
        self.color=color
c=red_c("blue","ram")
print(c.color)"""
# in these case we use super key word
"""parents assert are passed to child ,..because there is no my own asserts"""
"""class Car:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class red_c(Car): # even though we a pass the parent clss naaame into the child class when the child class contains construct ,it will only prints its own ttributes aand properties cannot access the data from parent claass 
    def details(self):
        print("hi my name is",self.name)
c=red_c("Ram")
print(c.details())
"""
"""
class Car:
    def __init__(self,name):
        self.name=name
class red_c(Car):
    def details(self):
        print("hi my name is",self.name)
c=red_c("Ram")
c.details()
"""

# problem on inheritance super() keyword---
# initialise a parent class as Employee-constructor with parameter name,child class as developer and --constructor  with parameter prog_language ,use super keyword as dev to get 2 parameter data
# make a class animal-contain a method with print("animal is shouting "),make 2 child class
# dog-method with "bow"&