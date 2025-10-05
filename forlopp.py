# Loops
# So far we have seen that Python executes code in a sequence and each block of code is executed once.
# Loops allow us to execute a block of code several times.

# While Loop
# Allows us to execute a block of code several times as long as the condition is True. 
# while expression:
#     statement(s)
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
# Using else statement with While Loop
# Else clause is only executed when our while condition becomes false. If we break out of the loop or if an exception is raised then it won't be executed. 

# Syntax:

# while condition:
#      # execute these statements
# else:
#      # execute these statements
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
else:
    print("In Else Block")
# Nested Loops
# syntax:
# while expression:
#    while expression: 
#        statement(s)
#    statement(s)
# prblms:
# Write a program that reads a number N and prints the number 0 N times on N lines.
# Input
# The input will be a single line containing an integer representing N.
# Output
# The output should be N lines containing an integer O on each line.
A=int(input())
AA=1
while AA<=A:
    print("0")
    AA=AA+1
#     Write a program to print integers from 1 to the given integer (N).
# Input
# The first line of input will contain a positive integer.
# Output
# The output should be of N lines, printing an integer in each line.
A=int(input())
AA=0
while AA<A:
    print(AA+1)
    AA=AA+1
# Input
# The input will be a single line containing an integer representing N
# Output
# The output should be a single line containing a float that is the average of N numbers from 1.
N=int(input())
A=1
sum=0
while A<=N:
    sum=sum+A
    A=A+1
Avg=sum/N
print(Avg)
# input
# The input will be a single line containing an integer representing N
# Output
# The output should contain cubes of N numbers from 1, each on a new line.
A=int(input())
AA=1
while AA<=A:
    print(AA**3)
    AA=AA+1
# Write a program that reads two numbers M and N and prints N numbers after M.
# Input
# The first line of input contains an integer representing M
# The second line of input contains an integer representing N
# Output
# The output should contain N numbers after M, each on a new line.
M=int(input())
N=int(input())
A=0
while A<N:
    print(M+1)
    A=A+1
    M=M+1
# Given a number N, write a program that reads N numbers as input and prints the product of the given N numbers.
# Input
# The first line of input contains an integer representing N
# The next N lines of input contain integers.
# Output
A=int(input())
AA=0
PR=1
IN=0
while AA<A:
    AA=AA+1
    IN=int(input())
    PR=PR*IN
print(PR)
# Write a program that reads a number N and prints the number 0 N times on N lines.
# Input
# The input will be a single line containing an integer representing N.
# Output
# The output should be N lines containing an integer O on each line.
A=int(input())
AA=1
while AA<=A:
    print("0")
    AA=AA+1
#     Write a program to print integers from 1 to the given integer (N).
# Input
# The first line of input will contain a positive integer.
# Output
# The output should be of N lines, printing an integer in each line.
A=int(input())
AA=0
while AA<A:
    print(AA+1)
    AA=AA+1
# Write a program that reads a string and prints the first character of the given string on N lines, where N is the length of the given string.
# Input
# The input will be a single line containing a string.
# Output
# The output should be N lines, with each line containing a string that is the first character of the given string. Here, N is the length of the given string.
A=input()
AA=A[0]
Len=int(len(A))
Aa=0
while Aa<Len:
    Aa=Aa+1 
    print(AA)
# Calculate the factorial of a number using a for loop
n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
# Reverse a number using a for loop. (Input: 1234 → Output: 4321)
n = input()
rev = ""
for i in n:
    rev = i + rev
print(int(rev))
n = int(input())
is_prime = True
if n < 2:
    is_prime = False
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")

li = [[1, 4, 6], [4, 6, 8], [3, 6, 9]]

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

for i in range(r):
    for j in range(c):
        print(li[i][j], end=" ")
    print()  # Newline after each row

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
# Floyd’s triangle (incrementing numbers across rows):

n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
#Inverted Number Pyramid
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()
#Checkerboard Pattern
n = 5
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#Sum of Digits in Each Row
n = 5
for i in range(1, n+1):
    total = 0
    for j in range(1, i+1):
        print(j, end=" ")
        total += j
    print("= ", total)
# Write a program that reads two numbers M and N and prints N numbers after M.
# Input
# The first line of input contains an integer representing M
# The second line of input contains an integer representing N
# Output
# The output should contain N numbers after M, each on a new line.
M=int(input())
N=int(input())
A=0
while A<N:
    print(M+1)
    A=A+1
    M=M+1
# Given a number N, write a program that reads N numbers as input and prints the product of the given N numbers.
# Input
# The first line of input contains an integer representing N
# The next N lines of input contain integers.
# Output
A=int(input())
AA=0
PR=1
IN=0
while AA<A:
    AA=AA+1
    IN=int(input())
    PR=PR*IN
print(PR)
    print("In Else Block")
# Nested Loops
# syntax:
# while expression:
#    while expression: 
#        statement(s)
#    statement(s)
# prblms:
# Write a program that reads a number N and prints the number 0 N times on N lines.
# Input
# The input will be a single line containing an integer representing N.
# Output
# The output should be N lines containing an integer O on each line.
A=int(input())
AA=1
while AA<=A:
    print("0")
    AA=AA+1
#     Write a program to print integers from 1 to the given integer (N).
# Input
# The first line of input will contain a positive integer.
# Output
# The output should be of N lines, printing an integer in each line.
A=int(input())
AA=0
while AA<A:
    print(AA+1)
    AA=AA+1
# Input
# The input will be a single line containing an integer representing N
# Output
# The output should be a single line containing a float that is the average of N numbers from 1.
N=int(input())
A=1
sum=0
while A<=N:
    sum=sum+A
    A=A+1
Avg=sum/N
print(Avg)
# input
# The input will be a single line containing an integer representing N
# Output
# The output should contain cubes of N numbers from 1, each on a new line.
A=int(input())
AA=1
while AA<=A:
    print(AA**3)
    AA=AA+1
# Write a program that reads two numbers M and N and prints N numbers after M.
# Input
# The first line of input contains an integer representing M
# The second line of input contains an integer representing N
# Output
# The output should contain N numbers after M, each on a new line.
M=int(input())
N=int(input())
A=0
while A<N:
    print(M+1)
    A=A+1
    M=M+1

# Even number
n = int(input("Enter a number: "))

for i in range(1, n+1):
    if i % 2 == 0:
        
        print(i, end=" ")
