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