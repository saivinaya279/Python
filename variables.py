# # Variables
# Variables are like containers for storing values.
'''
# Values
# Consider that variables are like containers for storing information.
# basic operations on variables
x=5
name="vinaya"
print(x)
print(name)
# Rules for Naming Variables
# Variable names can only contain letters, digits and underscores (_).
# cannot start with a digit.
# Avoid using Python keywords (e.g., if, else, for) as variable names.
age=21
_name="hello"
score=90
print(age)
print(_name)
print(score)
# Type casting :Avoid using Python keywords (e.g., if, else, for) as variable names.
s="10"
n=int(s)
b=48
x=float(b)
age=25
s=str(age)
print(n)
print(s)
print(x)
# we can determine the type of a variable using the type() function. 
n=42
s="hello world"
bool=True
print(type(n))
print(type(s))
print(type(bool))
# Delete a variable using del
X=10
print(X)
del X
# PROBLEMS ON VARIABLES
# Swapping Two Variables
a,b=5,10
a,b=b,a
print(a)
print(b)
# Counting Characters in a String
word ="mnndyujb"
length= len(word)
print(length)
# Local Variable:
# Defined within a function or block, accessible only inside that scope.
# Global Variables:
# Defined outside functions, accessible throughout the program.
'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)