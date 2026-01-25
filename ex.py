
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