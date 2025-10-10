# Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# Print numbers from 10 to 1 using a for loop
for i in range(10, 0, -1):
    print(i)

# Print even numbers from 1 to 20
for i in range(0, 21, 2):
    print(i)

# Print all multiples of 5 from 1 to 50 (method 1)
for i in range(0, 51, 5):
    print(i)

# Print all multiples of 5 from 1 to 50 (method 2)
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# Find the sum of numbers from 1 to N (take N as input)
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)

# Find the product (multiplication) of numbers from 1 to N
n = int(input("Enter a number: "))
prod = 1
for i in range(1, n + 1):
    prod *= i
print("Product:", prod)

# Count how many numbers between 1 and 50 are divisible by 3
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
print("Count of numbers divisible by 3:", count)

# Print the square of each number from 1 to 10
for i in range(1, 11):
    print(i ** 2)

# Print each character of a string using a for loop
n = "Python"
for char in n:
    print(char, end=" ")
print()

# Take a list of numbers and print only the positive numbers
nums = [-10, 50, -20, 40, 80]
for i in nums:
    if i > 0:
        print(i)

# Take a list of numbers and count how many are odd and even
even = 0
odd = 0
nums = [1, 2, 3, 4, 5, 7, 6, 8]
for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

# Calculate the factorial of a number using a for loop
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# Reverse a number using a while loop
n = int(input("Enter a number to reverse: "))
rev = 0
temp = n
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print("Reversed number:", rev)

# Print the first N terms of Fibonacci series
n = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Given two integers M and N, print the sum of numbers from M to N
m = int(input("Enter M: "))
n = int(input("Enter N: "))
sum_range = 0
for i in range(m, n + 1):
    sum_range += i
print("Sum from M to N:", sum_range)

# Program that reads a number N and prints 10 numbers after N
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n + i)

# Print a simple number triangle pattern
n = int(input("Enter a number for pattern: "))
for i in range(1, n + 1):
    row = (str(i) + " ") * i
    print(row)

# Print number pattern using nested loops
n = int(input("Enter a number for nested pattern: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# Palindrome number pyramid pattern
n = int(input("Enter a number for palindrome pattern: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number missing from the array.
# Example: nums = [3,0,1] → Output: 2

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = n * (n + 1) // 2
        actualSum = sum(nums)
        return expectedSum - actualSum
