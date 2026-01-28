
def single_digit(a):
    if n>=0 and n<=9:
        return "Single_Digit"
    return "not "
n=int(input())
print(single_digit(a))
n=int(input())
sum_i=0
while n >0:
    d=n%10
    sum_i+=d
    n//=10
print(sum_i)
def smallest_num(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    return c
a=int(input())
b=int(input())
c=int(input())
print(smallest_num(a,b,c))
def leap_year(n):
    if n%400==0:
        return "leap year"
    elif n%4==0 and n%100!=0:
        return "leap year"
    return "not leap year"
n=int(input())
print(leap_year(n))

def pass_fail(n):
    if n>=35:
        return "Pass"
    return "Fail"
n=int(input())
print(pass_fail(n))
def age_elb(n):
    if n>=18:
        return "Eligible"
    return "Not Eligible"
n=int(input())
print(age_elb(n))
def pos_neg(n):
    if n>0:
        return "Positive"
    return "Negative"
n=int(input())
print(pos_neg(n))
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
        print("*",end=" ")
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
        