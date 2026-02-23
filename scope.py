"""Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function."""
# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()
"""Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local."""