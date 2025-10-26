Smallest element

a=[3,5,2,8,1]
min_num=a[0]
for i in a:
    if i<min_num:
        min_num=i
print(min_num)""" nums=[1,2,3,4,5]
output=[5,4,3,2,1]"""
nums = [1, 2, 3, 4, 5]
rev = []
for i in nums:
    rev.insert(0, i)
print(rev)

# find the largest number in a list
a=[8,4,5,7,9]
max_num=a[0]
for i in a:
    if i>max_num:
        max_num=i    
print(max_num)

# # Count even & odd numbers
a=[1,2,3,4,5]
count1=0
count2=0
for i in a:
    if i%2==0:
        count1=count1+1
    else:
        count2=count2+1
print(count1)
print(count2)

# remove duplicates from a list
a=[7,4,6,8,4,5,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

# remove duplicates from a list
a=[7,4,6,8,4,5,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

# remove duplicates from a list
a=[7,4,6,8,4,5,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

# remove duplicates from a list
a=[7,4,6,8,4,5,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
# remove duplicates from a list
a=[7,4,6,8,4,5,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
#Smallest element

a=[3,5,2,8,1]
min_num=a[0]
for i in a:
    if i<min_num:
        min_num=i
print(min_num)
#Count positive, negative, and zero

a=[-2,0,5,-1,0,3]
pos=0
neg=0
zero=0
for i in a:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1
print(pos,neg,zero)
