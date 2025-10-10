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
    