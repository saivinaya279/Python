# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
# Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)
"""Re-naming a Module
You can create an alias when you import a module, by using the as keyword:"""
import mymodule as mx

a = mx.person1["age"]
print(a)
# Import and use the platform module:

import platform

x = platform.system()
print(x)
"""There is a built-in function to list all the function names (or variable names) in a module. The dir() function:"""
# List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)
import math
print(math.sqrt(16))
import math
print(math.sqrt(25))
from math import sqrt
print(sqrt(25))
def test():
    print("Hello")

if __name__ == "__main__":
    test()
"""What is an alias in modules?

Example:
"""
import pandas as pd
import numpy as np