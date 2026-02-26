"""Python Functions are a block of statements that does a specific task
You:
•	give it input
•	it does some work
•	it gives output
Defining a Function
•	We can define a function in Python, using the def keyword. A function might take input in the form of parameters.
•	Python def keyword: is used to define a function, it is placed before a function name that is provided by the user to create a user-defined function.
Basic structure
def function_name():
    # work

Meaning of each part
•	def → define (create a function)
•	function_name → name of the function
•	() → inputs will come here
•	: → start of function body
•	Indentation (spaces) → tells Python what belongs to the function
# defining function
def func():
    print("Hello")

# calling function    
func()




FULL CODE for execution"""
def class_(a,b):
    return a+b
a=int(input())
b=int(input())
result=class_(a,b)
print(result)



# 
def class_(a, b):
    return a + b

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calling the function
result = class_(a, b)

# Printing the result sum
print("Sum is:", result)
def class_(a,b):
    return a+b
a=int(input())
b=int(input())
result=class_(a,b)
print(result)
# square
def square(x):
    return x * x

x=int(input())
ans= square(x)
print(ans)
# factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
n=int(input())
ans= factorial(n)
print(ans)
# even or odd 
def evenodd(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
a=int(input())
ans=evenodd(a)
print(ans)
# positive or negative
def function_(a):
    if a>0:
        return "positive"
    elif a<0:
        return"negative"
    else:
        return"zero"
a=int(input())
ans=function_(a)
print(ans)

# largest of 3
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print("a is large",a)
elif b>=a and b>=c:
    print("b is large",b)

else:
    print("c is large",c)
# reverse

def reverse_num(n):
    res=0
    while n>0:
        digit=n%10
        res=res*10+digit
        n=n//10
    return res
n = int(input())
print(reverse_num(n))

"""# # Given two integers a1 and a2, the first and second terms of an
Arithmetic Series respectively, the problem is to find the nth term of the series"""
def nthTermOfAP(a1, a2, n):
    nthTerm = a1 # a1=1,a2=3
    d = a2 - a1 # d=2
    for i in range(1, n): # until 9 (n=n-1)
        nthTerm += d # 1+2=3,3+2=5,...until 9th loop 
    return nthTerm


a1 = int(input()) # a1=1
a2 = int(input()) # a2=3
n = int(input()) # n=10

print(nthTermOfAP(a1, a2, n))
"""# You are given an integer n. Your task is to reverse the digits, 
ensuring that the reversed number has no leading zeroes."""

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n=int(input())
print(isPrime(n))
def checkValidity(a, b, c): 
    
    # check condition 
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True        

# driver code 
a = int
b = 10
c = 5
if checkValidity(a, b, c):
    print("Valid") 
else:
    print("Invalid")
"""# Given a positive integer, n. Find the factorial of n.

Examples :

Input: n = 5
Output: 120"""
# Explanation: 1 x 2 x 3 x 4 x 5 = 120
def factorial(n) -> int:
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input())
print(factorial(n))
"""# Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""
def myfunc():
  x = 300
  print(x)

myfunc()
# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
"""# Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.
"""
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
"""Naming Variables
If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables, one available in the global scope (outside the function) 
and one available in the local scope (inside the function):"""
# The function will print the local x, and then the code will print the global x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
"""Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global."""
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Sum of 2 numbers using function
def add(a, b):
    return a + b
print(add(5, 3))

# Even or Odd function
def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(7))

# Greeting Function
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Vinaya")

# Sum of ANY numbers
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_numbers(1,2,3,4,5))

# Find Maximum from many numbers
def find_max(*nums):
    return max(nums)
print(find_max(3,8,2,10,5))

# Multiply all numbers
def multiply(*nums):
    result = 1
    for i in nums:
        result *= i
    return result
print(multiply(2,3,4))

# Print Student Details
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_info(name="Vinaya", age=20, course="DS")

# Average of unlimited numbers
def average(*nums):
    return sum(nums) / len(nums)
print(average(10,20,30,40))

# Count positive & negative numbers
def count_numbers(*nums):
    pos=neg=0
    for n in nums:
        if n>=0:
            pos += 1
        else:
            neg += 1
    return pos, neg
print(count_numbers(5,-2,3,-1,0))

# Remove duplicates
def unique_values(*nums):
    return list(set(nums))
print(unique_values(1,2,2,3,4,4,5))

# Second largest number
def second_largest(*nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]
print(second_largest(10,20,5,8,20))
