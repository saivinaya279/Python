# Print numbers from 1 to 10 using a for loop.
i=0
for i in range(11):
    print(i)
# Print numbers from 1 to 10 using a for loop.
for i in range(10, 0, -1):
    print(i)
  
# Print even numbers from 1 to 20.
i=0
for i in range(0,21,2):
    print(i)
# Print all multiples of 5 from 1 to 50.
i=0
for i in range(0,51,5):
    print(i)
# 
for i in range(1,51):
    if i%5==0:
        print(i)
# Find the sum of numbers from 1 to N (take N as input).
n=int(input())
total=0
for i in range(1,n+1):
    total+=i
print(total)
# Find the product (multiplication) of numbers from 1 to N.
n=int(input())
prod=0
for i in range(1,n+1):
    prod*=i
print(total)
# Find the sum of numbers from 1 to N (take N as input).
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
# Find the product (multiplication) of numbers from 1 to N.
n=int(input())
prod=1
for i in range(1,n+1):
    prod=prod*i
print(prod)
# Count how many numbers between 1 and 50 are divisible by 3.
i=0
count=0
for i in range(1,51):
    if i%3==0:
        count=count+1
print(count)
# Print the square of each number from 1 to 10.

for i in range(1,11):
    i=i**2
    print(i)
# Print each character of a string using a for loop. 
# (Input: "Python" → Output: P y t h o n)
n = "Python"
for char in (n):
    print(char, end=" ")
# Take a list of numbers and print only the positive numbers.
n=[-10,50,-20,40,80]
for i in n:
    if i>0:
        print(i)
# Take a list of numbers and count how many are odd and how many are even.
even=0
odd=0
n=[1,2,3,4,5,7,6,8]
for i in n:
    if i %2==0:
        even=even+1
    elif i%2==1:
        odd=odd+1
print(even)
print(odd)
# Calculate the factorial of a number using a for loop.
n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i   
print(fact)
# Reverse a number using a for loop. (Input: 1234 → Output: 4321)
n = int(input())
rev = 0
original = n  
for i in str(n):  
    rev = rev * 10 + int(i)
print(rev)
# Print the first N terms of Fibonacci series using a for loop.
n = int(input())
a, b = 0, 1
print( end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b  
# given two integers M and N ,write a program to print sum to the numbers from m to n 
m=int(input())
n=int(input())
sum=0
for i in range(m,n+1):
    sum=sum+i
print(sum)
# write a program that reads a number N and prints 10 numbers after N
n=int(input())
b=0
for i in range(1,11):
    b=n+i
    print(b)
n=int(input())
for i in range(1,n+1):
    char=str(i)
    row=(char +" ")*i
    print(row)
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
# Palindrom number
n=int(input())
for i in  range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j, end="")
    for j in range(2,i+1):
        print(j, end="")
    print()

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]

# Output: 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expectedSum=n*(n+1)//2
        actualSum=sum(nums)
        return expectedSum-actualSum
        
    
    
    

    