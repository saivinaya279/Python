# prblm-1
# Given a double value d, typecast it to an integer value and print it.
'''

# Input: d = 10.23
# Output: 10
# Explanation: The integer value of 10.23 is 1
d = float(input())
s=int(d)
print(s)
'''

# prblm-2
'''
# Given an input num as a string. You need to typecast into an integer and double it. 

# Examples:
# nput: num = "5"
# Output: 10
# Explanation: Typecast "5" to int and then double it 5 * 2 = 10
num = input()
d=int(num)
print(d*2)
'''
# prblm-3
'''
# Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a. Just write the code to swap values of a and b at the specified place.

# Examples
# Input: a = 1, b = 2
# Output: 2 1
# Explanation: Initially a = 1 and b = 2, now a = 2 and b = 1
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a,b)
'''
# prblm-4
'''
# Sum of N Numbers
# Given an integer n find the sum of the first n natural number.
#Examples:
# Input: n = 10
# Output: 55
# Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
# Input: n = 5
# Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15.

n = int(input("Enter a number: "))
d = n * (n + 1) // 2
print(d)
'''
# prblm -5
'''
#AREA OF RECTANGLE
# problem :Given length and breadth,find the area
length=int(input())
breadth=int(input())
Area=length*breadth
print(Area)
'''
# prblm-6
'''
# simple interst
# Problem: Find simple interest = (P × R × T) / 100
P=1000
R=5
T=2
SI=(P*R*T)/100
print(SI)
'''
# problem-7,8,9,10
'''
##
# Area of Circle 
# find area of circle= π × r²
R=7
pi=3.14
area=pi*R*R
print(area)
# Convert celsius to fahrenhit
# f=(c*9/5)+32
c=int(input())
f=(c*9/5)+5
print(f)
# perimeter of a square
# premiter =4*side
side=int(input())
perimeter=4*side
print(perimeter)
'''
#convert hours into minutes
# take hours as input and print totl mintues
hours=int(input())
min=hours*60
print(min)

a=int(input())
b=int(input())
c=a%b
print(c)