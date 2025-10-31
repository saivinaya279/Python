# Smallest element

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
# Separate even and odd numbers


a=[1,2,3,4,5,6,7]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
#  Count how many times a specific number appears in a list.
sentences=["hjk jkl trewq dfgb utr","erfghj jkloi uytr erty uoyuk","oioiiuy rew rty dswe 2qwasd rewqASZ TYREWQX"]
max_words=0
for sentence in sentences:
    word_count = len(sentence.split())
    if word_count > max_words:
        max_words = word_count
print(max_words)

# Count how many times a specific number appears in a list.
a = [1, 2, 3, 2, 4, 2, 5]
num = 2
count = 0
for i in a:
    if i == num:
        count += 1
print(count)

# Check if an element exists in a list (take input from user).
a = [10, 20, 30, 40, 50]
x = int(input("Enter element: "))
if x in a:
    print("Exists")
else:
    print("Not exists")
    
# Find the average of numbers in a list.
a = [10, 20, 30, 40, 50]
total = 0
for i in a:
    total += i
avg = total / len(a)
print(avg)
# Print only even numbers from a list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
    if i % 2 == 0:
        print(i)
# Create a list of squares of numbers from 1 to 10

squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)
# Concatenate two lists and print the result

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# Take a string input and convert it into a list of characters.
string = input()
char_list = []
for ch in string:
    char_list.append(ch)
print(char_list)
# Count how many elements in a list are greater than a given number (without using statements)
numbers = [10, 25, 30, 45, 5, 60]
n = int(input("Enter a number: "))
count = 0

for num in numbers:
    count += num > n

print("Count of elements greater than", n, "is:", count)
	# Count how many elements in a list are greater than a given number.
lst = [2, 8, 5, 12, 3, 10]
n = 6
count = 0
for i in lst:
    if i > n:
        count += 1
print(count)

# Replace all negative numbers in a list with 0.
lst = [3, -2, 5, -7, 9]
for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0
print(lst)

# Print the list in reverse order using a loop.
lst = [1, 2, 3, 4, 5]
rev = []
for i in lst:
    rev = [i] + rev
print(rev)
