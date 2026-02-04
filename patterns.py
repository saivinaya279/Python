print("hello" ,end=" ")
print("vinaya")
li=["hello","boom"]
for i in range(len(li)):
    print(li[i])
li=[["*","*","*"],["*","*","*"],["*","*","*"]]
r=len(li)
c=len(li[0])
for i in range(r):
    for j in range (c):
        print(li[i][j],end=" ")
        
    print()
# # Print a solid square of * with n rows and n columns

r=3
c=3
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()
# #  stars(* ),with (_)
r=int(input())
c=int(input())
for i in range(r):
    for j in range(c):
        print("*",end="_")
    print()
    """ *_*_*_*_*
         *_*_*_*_*
         *_*_*_*_*
         *_*_*_*_*   
         basically question  write a code to  is not to print the (_)at the end  like above"""
r=int(input())
c=int(input())
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j !=c-1:
             print("-",end="")
    print()
    
    
# # Print a solid rectangle of * with n rows and n columns
n = 4
m = 6

for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()

n = 5
# Print a right-angled triangle of * (increasing).
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
# print right-angled triangle 
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
# Print an inverted right-angled triangle aligned to the right
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
# Full Pyramid (Centered Triangle)
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
    # Inverted Full Pyramid
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
# Hollow Rectangle 
l = 4  
b = 6  

print("* " * b)

for i in range(1, l-1):
    print("*" + " " * ((b*2)-3) + "*")

print("* " * b)
# Hollow Right-Angled Triangle
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
n=5
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
# Palindromic number triangle:
n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()
# numbers in increasing order starting
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):  # start from 1, go till i
        print(j, end=" ")
    print()
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
n=5
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
n=int(input())
for i in range(n):
    if i ==0 or i==n-1:
        print("*" * n)
    else:
        print("*" + " " *(n-2) + "*")
    
    
"""Example:
If n = 4, the output should be:

1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(end=" ")
    print()
# Printing Rhombus Star Pattern