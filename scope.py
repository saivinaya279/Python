# """
# """Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function."""
# # A variable created inside a function is available inside that function:

# def myfunc():
#   x = 300
#   print(x)

# myfunc()
# """Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local."""
# # A variable created outside of a function is global and can be used by anyone:

# x = 300

# def myfunc():
#   print(x)

# myfunc()


# print(x)
# # naming Variables
# # The function will print the local x, and then the code will print the global x:
# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)
# # Global Keyword
# """f you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global."""   
# """
"""1️⃣ Local Scope """
def fun():
  x=10
  print(x)
fun()
# print(x)  Local variable cannot be accessed outside.
"""def fun():

    x = 10

fun()

print(x)""" # NameError: x not defined
# 2️⃣ Global Scope
x = 50   # global

def fun():
    # x=20 ,error ,cannot modify  
    print(x)

fun()
x = 10
# how to modify using global variable
def fun():

    global x

    x = 20

fun()

print(x)