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