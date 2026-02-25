"""Basic Decorator:
Decorators let you add extra behavior to a function, without changing the function's code
  A decorator is a function thaat takes another fun as input and returns a new function"""
#   Basic Decorator
"""Decorators are used to:

✅ Add logging

✅ Measure execution time

✅ Add authentication

✅ Validate inputs"""
"""Imagine you wrote a function:

👉 It just prints Hello

But before it runs you want to print
“Function started”

And after it runs you want to print
“Function ended”

You don’t want to edit the original function every time.

So you create a wrapper that adds extra behavior.

That wrapper = decorator"""


# normal function 
def greet():
    print("Hello")
greet()
# We create a wrapper function
"""We want:

Function started
Hello
Function ended"""
def decorator_name(func):
    def wrapper():
        # extra work before
        print("Function started")
        func()
        # extra work after
    return wrapper
@decorator_name
def my_function():
    print("Hello")
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time:", end - start)
    return wrapper
@timer
def slow():
    time.sleep(2)
    print("Done")

slow()
# Arguments in the Decorated Function
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))