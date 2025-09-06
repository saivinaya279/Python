# Arithmetic Operators 
# 1. Take two integers as input and print their sum, difference, product, and quotient.
a=15
b=4
print(a+b)
print(a-b)  
print(a*b)# 
print(a/b)# 
print(a//b)#n
print(a%b) 
print(a**b)
# Input a number and print its square and cube using **. 
c=int(input())
d=c**2
e=c**3
print(d)
print(e)
print("/n")
# Input a number and print the remainder when divided by 7.
d=int(input())
f=d%7
print(f)
# Input two floats and print the result of dividing the first by the second with 2 decimal places. 
c=int(input())
d=int(input())
e=c/d
print(e)
# Comparison Operators
#  Input two numbers and check if the first is greater than the second.
a=int(input())
b=int(input())
print(a>b)
# : Input two strings and check if they are equal
s=input()
s1=input()
print(s==s1)
# Input an age and check if it is greater than or equal to 18
age=int(input())
print(age>=18)
# logical operators
# Input two Boolean values (True/False) and print their and, or, not results.
c=bool(int(input()))
d=bool(int(input()))
print(c and b)
print(c or d)
print(not d)
# Input a number and check if it lies between 10 and 20 (inclusive) using logical operators.
number=int(input())
print(number>=10 and number<=20)
# Input three numbers and check if all are positive.
a=int(input())
b=int(input())
c=int(input())
print(a>0 and b>0 and c>0)
# Assignment Operators 
# Input a number and increase it by 10 using +=. Print the result.
a = int(input())
a += 10
print(a)
# Input a number and reduce it by half using /=. Print the result.
b = int(input())
b /= 2
print(b)
# Input two integers and print their &, |, and ^.
a = int(input())
b = int(input())
print(a & b)
print(a | b)
print(a ^ b)
# Input an integer and print its left shift by 2 and right shift by 2.
c = int(input())
print(c << 2)
print(c >> 2)
# 15. Input a number and check if it is odd or even using bitwise & 1.give this answers ..use a,b,c,d only for variables and dont give ay sentences
d = int(input())
print("Even" if (d & 1) == 0 else "Odd")