def student(name, age=20):
    print(name, age)

student("Sai")
student("Sai",25)
# *args
def add(*numbers):
    print(numbers)
add(1,2,3,4,5)
""""output:"""# Python converts into tuple.(1,2,3,4,5).
# example:
def add1(*numberss):
    total=0
    for n in numberss:
        total+=n
    return total
print(add1(1,2,3,4,5))
# def function(**kwargs):
def profile(**data):
    print(data)
profile(name="Sai",age=21)
# example for all arguments
def example(a,b=10,*args,**kwargs):

    print("Positional:",a)

    print("Default:",b)

    print("Args:",args)

    print("Kwargs:",kwargs)


example(5,20,30,40,name="Sai",age=21) 
"""Practice Problem 1 (Positional vs Keyword)

(Time: 5 mins)

Create a function:

student(name, age, course)

Print:

Name: Sai
Age: 21
Course: Data Science"""
def student(name,age,course="python"):
    print(name,age,course)
# Positional call
student("vinaya",20,"Datascience")
# keyword call
student(name="vinaya",age=20,course="DataScience")
student("sai",20)
# 
def student(name, age, course="python"):

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


# Positional call
student("Vinaya",20,"Data Science")

print("-----")

# Keyword call
student(course="Data Science",name="Vinaya",age=20)
# Default call
student("vinaya",20)
def calculate_bill(price,quantity,tax=5):
    total=price*quantity
    tax_amount=total*tax/100
    final=total+tax_amount
    return final
print(calculate_bill(100,2))
print(calculate_bill(100,2,18))
"""Practice Problem 3 (*args)

Create:

find_max(*numbers)

Return largest number.

Example:

find_max(10,5,20,8)
Output:
20"""
def find_max(*numbers):
    larg=numbers[0]
    for n in numbers:
        if n>larg:
            larg=n
    return larg
print(find_max(10,5,20,8))
print(find_max(-10,-5,-20,-8))
# 
def find_max(*nums):
    return max(nums)
print(find_max(10,20,-5))
# print(find_max()) # we will get max() iterable argument is empty to handle
def find_max(*numbers):

    if len(numbers)==0:
        return "No numbers given"

    larg=numbers[0]

    for n in numbers:
        if n>larg:
            larg=n

    return larg
print(find_max())
