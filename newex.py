#  Smallest element

a=[3,5,2,8,1]
min_num=a[0]
for i in a:
    if i<min_num:
        min_num=i
print(min_num)
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