for i in range(5):
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

# write a program that reads a number N,and prints the sum of the cubes of numbers from 1 to N
n=int(input())
cube=0
for i in range(1, n+1):
    cube_num=i**3
    cube =cube+cube_num
print(cube)
    

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
"""3. Print pattern of alphabets



A
A B
A B C
A B C D
A B C D E
n = 5"""
for i in range(1, n + 1):       # Controls number of rows (1 to 5)
    for j in range(65, 65 + i): # Controls which alphabets to print in each row
        print(chr(j), end=" ")
    print()
"""# inverted alphabetical trirangle
A B C D E 
A B C D 
A B C 
A B 
A"""
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
"""65 
65 66 
65 66 67 
65 66 67 68"""
s = "ABCD"

for i in range(1, len(s) + 1):
    for j in range(i):
        print(ord(s[j]), end=" ")
    print()
"""Check if a String Is a Pangram

Concept

A pangram is a sentence that contains every letter (a–z) at least once, ignoring case and spaces.
s = "The quick brown fox jumps over the lazy dog"""

# Convert to lowercase to handle case-insensitive
s = s.lower()

alphabets = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for ch in alphabets:
    if ch not in s:
        is_pangram = False
        break

if is_pangram:
    print("Pangram")
else:
    print("Not Pangram")


"""1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 """
n=5
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
# Square of Stars (solid and hollow).
    
"""f n = 5, the output should be:

*****
*****
*****
*****
*****"""


n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
# Write a program to print a hollow square pattern using stars (*).
"""f n = 5, the output should be:

*****
*   *
*   *
*   *
*****"""
""" method-1"""
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i ==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
""" method -2"""
n=int(input())
for i in range(n):
    if i ==0 or i==n-1:
        print("*" * n)
    else:
        print("*" + " " *(n-2) + "*")
"""Simple Number Pyramid

Each row starts from 1 every time.

Example (n = 5):

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
# first n natural numbers in reverse order.
""" 5 4 3 2 1"""
n=int(input())
for i in range(n,0,-1):
    print(i,end=" ")
# Print First n Natural Numbers in a Single Line
"""If n = 5, the output should be:

1 2 3 4 5"""
n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
# Print Digits of a Number Separated by Spaces
"""Example:
If the input number is 4521, the output should be:

4 5 2 1 """
n=input()
for i in n: 
    print(i,end=" ")
# Print a Single Asterisk Increasing Series (1 to n)
"""Example:
If n = 5, the output should be:

*
**
***
****
*****"""
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
# Print an n × n Matrix of Numbers (Row-wise)
"""Example:
If n = 4, the output should be:

1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()