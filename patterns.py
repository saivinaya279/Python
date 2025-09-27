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
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()