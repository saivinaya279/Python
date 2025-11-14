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
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
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
"""3. Print pattern of alphabets



A
A B
A B C
A B C D
A B C D E
n = 5"""
for i in range(1, n + 1):       # Controls number of rows (1 to 5)
    for j in range(65, 65 + i): # Controls which alphabets to print in each row
        print(chr(j), end=" ")
    print()
"""# inverted alphabetical trirangle
A B C D E 
A B C D 
A B C 
A B 
A"""
n = 5
for i in range(n, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()
#row repeated alphabets 
n = 5
for i in range(65, 65 + n):
    for j in range(65, i + 1):
        print(chr(i), end=" ")
    print()
"""65 
65 66 
65 66 67 
65 66 67 68"""
s = "ABCD"

for i in range(1, len(s) + 1):
    for j in range(i):
        print(ord(s[j]), end=" ")
    print()# Row number repeated in each row:

n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
"""3. Print pattern of alphabets



A
A B
A B C
A B C D
A B C D E
n = 5"""
for i in range(1, n + 1):       # Controls number of rows (1 to 5)
    for j in range(65, 65 + i): # Controls which alphabets to print in each row
        print(chr(j), end=" ")
    print()
"""# inverted alphabetical trirangle
A B C D E 
A B C D 
A B C 
A B 
A"""
n = 5
for i in range(n, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()
#row repeated alphabets 
n = 5
for i in range(65, 65 + n):
    for j in range(65, i + 1):
        print(chr(i), end=" ")
    print()
"""65 
65 66 
65 66 67 
65 66 67 68"""
s = "ABCD"

for i in range(1, len(s) + 1):
    for j in range(i):
        print(ord(s[j]), end=" ")
    print()