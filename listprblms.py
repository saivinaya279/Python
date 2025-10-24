""" nums=[1,2,3,4,5]
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
        