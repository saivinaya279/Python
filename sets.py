set1 = {1, 2, 3, 4}
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)


# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))
set1 = {3, 1, 4, 1, 5, 9, 2}

print(set1) 
# Creating a set
set1 = {1, 2, 3}

# Add one item
set1.add(4)

# Add multiple items
set1.update([5, 6])

print(set1)
# add
s = {1, 2}
s.add(3)
print(s)
s = {1, 2, 3}
s.remove(2)
print(s)
# /length
s = {10, 20, 30}
print(len(s))
# Check if an element exists in a set
s = {5, 10, 15}
print(10 in s)
# Difference of sets
a = {1, 2, 3}
b = {2, 3}
print(a - b)
"""Problem 1: Remove Duplicate Numbers
Input
[1, 2, 2, 3, 4, 4]

Output
{1, 2, 3, 4}
"""
nums = [1, 2, 2, 3, 4, 4]
result = set(nums)
print(result)
"""🔹 Problem 2: Count Unique Elements
Input
[10, 20, 20, 30, 40, 40]

Output
4"""
nums = [10, 20, 20, 30, 40, 40]
print(len(set(nums)))
"""3: Check Common Elements Between Two Lists
Input
[1, 2, 3]
[3, 4, 5]

Output
{3}"""
a = [1, 2, 3]
b = [3, 4, 5]
print(set(a) & set(b))
"""4: Find Different Elements Between Two Lists
Input
[1, 2, 3]
[3, 4, 5]

Output
{1, 2}"""
a = [1, 2, 3]
b = [3, 4, 5]
print(set(a) - set(b))
"""5: Check if All Elements are Unique
Input
[1, 2, 3, 4]

Output
True"""
nums = [1, 2, 3, 4]
print(len(nums) == len(set(nums)))
"""6: Unique Characters in a String
Input
"hello"

Output
{'h', 'e', 'l', 'o'}
"""
s = "hello"
print(set(s))
"""7: Count Unique Words in a Sentence
Input
"python is easy and python is powerful"

Output
5"""
sentence = "python is easy and python is powerful"
print(len(set(sentence.split())))
""": Remove Duplicate Names
Input
["ram", "sam", "ram", "tom"]

Output
{'ram', 'sam', 'tom'}"""
names = ["ram", "sam", "ram", "tom"]
print(set(names))
"""10: Students Present in Both Classes
Input
Class A: [1, 2, 3]
Class B: [3, 4, 5]

Output
{3}"""
a = [1, 2, 3]
b = [3, 4, 5]
print(set(a) & set(b))
# 1: Find Missing Numbers from 1 to N
# Input
nums = [1, 2, 4, 6]
n = 6
nums = [1, 2, 4, 6]
n = 6
print(set(range(1, n + 1)) - set(nums))
# 2: Find Duplicate Elements
# Input
# [1, 2, 3, 2, 4, 3, 5]
nums = [1, 2, 3, 2, 4, 3, 5]
seen = set()
dup = set()
for i in nums:
    if i in seen:
        dup.add(i)
    seen.add(i)
print(dup)
# Find Common Words in Two Sentences
# Input
# s1 = "python is easy"
# s2 = "python is powerful"
s1 = "python is easy"
s2 = "python is powerful"
print(set(s1.split()) & set(s2.split()))
