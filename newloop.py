78for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(5,0,-2):
    for j in range(i):
        print("*",end=" ")
    print()
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
    print()    
n=5
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()
# write a program that reads a number N and prints 10 numbers after N
n=int(input())
b=0
for i in range(1,11):
    b=n+i
    print(b)
m=int(input())
n=int(input())
for i in range(m,n+1):
    print(i)
# given two integers M and N ,write a program to print sum to the numbers from m to n 
m=int(input())
n=int(input())
sum=0
for i in range(m,n+1):
    sum=sum+i
print(sum)
"""You are given an array nums containing n distinct numbers in the range [0, n].
Your task is to find the one number missing from this range."""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = n * (n + 1) // 2 # this is the formula to find the sum of n natuaral numbers(0 to n)
        actualSum = sum(nums)   # calculating actuall sum
        return expectedSum - actualSum

nums = [3, 0, 1,2,5]
sol = Solution()
missing = sol.missingNumber(nums)
print(f"The missing number is: {missing}")
A=int(input())
Sum=0
Avg=1 
for i in range(1,A+1):
    i=int(input())
    Sum=Sum+i
Avg=Sum/A
print(Avg)
# sum of digits
n=int(input())
sum=0
for i in  str(n):
    sum=sum+int(i)
print(sum)
# factorical of numbers
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
# write a program that reads a number N,and prints the sum of the cubes of numbers from 1 to N# Reverse a number using a for loop. (Input: 1234 → Output: 4321)
n = input()
rev = ""
for i in n:
    rev = i + rev
print(int(rev))
# Numbers in decreasing order (inverted triangle):

n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# Row number repeated in each row:

n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
3. Print pattern of alphabets



A
A B
A B C
A B C D
A B C D E
n = 5
for i in range(1, n + 1):       # Controls number of rows (1 to 5)
    for j in range(65, 65 + i): # Controls which alphabets to print in each row
        print(chr(j), end=" ")
    print()
# inverted alphabetical trirangle
A B C D E 
A B C D 
A B C 
A B 
A
n = 5
for i in range(n, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()
#row repeated alphabets 
n = 5
for i in range(65, 65 + n):
    for j in range(65, i + 1):
        print(chr(i), end=" ")
    print()

