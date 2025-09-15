# write code to print the next 3 consecutive numbers of the given integer input
c=int(input())
counter=0# intialization
while counter < 3:#termination condition
    c=c+1
    print(c)
    counter=counter+1 # Updation
#  intialization
#  while termination_condition:
#      block of code 
#      updation
#  write a program to print stars in N rows and N columns ,where integer N is given as an input
N=int(input())
counter=0
while counter < N:
    print("*"*N)
    counter=counter+1
# Write a program that reads a number N and prints the number 0 N times on N lines.
# Input
# The input will be a single line containing an integer representing N.
# Output
# The output should be N lines containing an integer O on each line.   # 
N=int(input())
counter =0
while counter < N:
    print(0)
    counter =counter+1
# Write a program to print integers from 1 to the given integer (N).
# Input
# The first line of input will contain a positive integer.
# Output
# The output should be of N lines, printing an integer in each line.
N=int(input())
count=0
while count < N:
    print(count+1)
    count=count+1
# Input The first line of input will contain an integer. 
# The second line of input will contain an integer. 
# Output The output should be printing an integer in each line, starting from M to N. 
n=int(input())
m=int(input())
count=n
while count<=m:
    print(count)
    count=count+1
# Input
# The input will be a single line containing an integer representing N
# # Output
# The output should be a single line containing a float that is the average of N numbers from 1.
N=int(input())
A=1
sum=0
while A<=N:
    sum=sum+A
    A=A+1
avg =sum/N
print(avg)
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
# The first line of input contains an integer representing N
# The next N lines of input contain integers.
# Output
# The output should be the product of the given N inputs.
A=int(input())
AA=0
PR=1
IN=0
while AA<A:
    AA=AA+1
    IN=int(input())
    PR=PR*IN
print(PR)
    