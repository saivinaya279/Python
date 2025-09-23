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
# Print a solid square of * with n rows and n columns

r=3
c=3
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()
#  stars(* ),with (_)
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
    
    
# Print a solid square of * with n rows and n columns
