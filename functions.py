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