# Print numbers from 1 to 10 using a for loop.
i=0
for i in range(11):
    print(i)
# Print numbers from 1 to 10 using a for loop.
for i in range(10, 0, -1):
    print(i)
  
# Print even numbers from 1 to 20.
i=0
for i in range(0,21,2):
    print(i)
# Print all multiples of 5 from 1 to 50.
i=0
for i in range(0,51,5):
    print(i)
i=0
# 
for i in range(1,51):
    if i%5==0:
        print(i)
# Find the sum of numbers from 1 to N (take N as input).
n=int(input())
total=0
for i in range(1,n+1):
    total+=i
print(total)
# Find the product (multiplication) of numbers from 1 to N.
n=int(input())
prod=0
for i in range(1,n+1):
    prod*=i
print(total)
# Find the sum of numbers from 1 to N (take N as input).
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
# Find the product (multiplication) of numbers from 1 to N.
n=int(input())
prod=1
for i in range(1,n+1):
    prod=prod*i
print(prod)
# Count how many numbers between 1 and 50 are divisible by 3.
i=0
count=0
for i in range(1,51):
    if i%3==0:
        count=count+1
print(count)
# Print the square of each number from 1 to 10.

for i in range(1,11):
    i=i**2
    print(i)
    

    
    
    

    