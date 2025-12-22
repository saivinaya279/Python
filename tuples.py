# Here’s a clear and complete explanation of Tuples in Python 👇

#  Concept of Tuple in Python
# 🔹 Definition

# A tuple is an ordered, immutable (cannot be changed) collection of items in Python.
# It is used to store multiple items in a single variable, similar to a list — but once created, you can’t modify it.

# Syntax
# my_tuple = (1, 2, 3)


# ✅ You can also create a tuple without parentheses:

# my_tuple = 1, 2, 3


# ✅ For a single-element tuple, you must include a comma:

# single = (5,)   # ✅ Tuple
# not_tuple = (5) # ❌ Just an integer

""" Characteristics of Tuples
# Property	Description
# Ordered	Elements have a defined order (index starts from 0).
# Immutable	You cannot modify (add, change, or delete) items after creation.
# Allow duplicates	Tuples can contain duplicate values.
# Can contain different data types	Numbers, strings, lists, etc."""
# Tuple Example
# student = ("Vinaya", 21, "Data Science", 8.7)
# print(student)


# Output:

# ('Vinaya', 21, 'Data Science', 8.7)

# Accessing Elements

# You can use indexing and slicing just like lists:

# t = (10, 20, 30, 40, 50)

# print(t[0])    # 10
# print(t[-1])   # 50
# print(t[1:4])  # (20, 30, 40)

""""Tuple Operations
# Operation	Example	Output
# Concatenation	(1,2) + (3,4)	(1, 2, 3, 4)
# Repetition	(1,2) * 3	(1, 2, 1, 2, 1, 2)
# Membership	3 in (1,2,3)	True
# Length	len((1,2,3))	3"""

"""Tuple Functions
# Function	Description	Example
# len()	Number of items	len(t)
# max()	Maximum value	max((1,5,2)) → 5
# min()	Minimum value	min((1,5,2)) → 1
# sum()	Sum of elements	sum((1,2,3)) → 6
# # tuple()	Converts list/string → tuple	tuple([1,2,3])"""
# """Tuple Packing and Unpacking""

# Packing:

person = ("Vinaya", 21, "Analyst")


# Unpacking:


name, age, role = person
print(name)  # Vinaya
print(age)   # 21
print(role)  # Analysts
"""Nested Tuples

Tuples can contain other tuples:"""

nested = ((1, 2), (3, 4), (5, 6))
print(nested[1][0])  # 3"""
t=(20,30,40,50)
print(sum(t))
# Create a tuple with 5 different numbers and print it.

t = (10, 20, 30, 40, 50)
print(t)
# rint the first and last elements of a tuple.

t = (1, 2, 3, 4, 5)
print("First:", t[0])
print("Last:", t[-1])
# Print a subtuple from index 1 to 3.

t = (10, 20, 30, 40, 50)
print(t[1:4])
# Join two tuples and print the result.

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)
# Repeat a tuple 3 times.

t = (5, 10)
print(t * 3)
# Check if 30 exists in a tuple.

t = (10, 20, 30, 40)
if 30 in t:
    print("yes")
else:
    print("NO")
# Find length of a tuple
t = (1, 2, 3, 4, 5)
print(len(t))
# Count how many times 2 appears.

t = (1, 2, 3, 2, 4, 2)
print(t.count(2))
# Find maximum and minimum elements
t = (4, 7, 1, 9, 3)
print(max(t))
print(min(t))
# Print all elements greater than 25.

t = (10, 20, 30, 40, 50)
for i in t:
    if i > 25:
        print(i)
# Create a tuple of 5 city names and print it.
cities = ("Vizag", "Hyderabad", "Bangalore", "Chennai", "Mumbai")
print(cities)
# Create a tuple with numbers from 1 to 10 and print the first element.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print (numbers[0])

# Print the last element of a tuple (10, 20, 30, 40, 50).
t = (10, 20, 30, 40, 50)
print(t[-1])
# Print elements from index 1 to 3 from the tuple (5, 10, 15, 20, 25).
t = (5, 10, 15, 20, 25)
print(t[1:4])
nums = (10, 25, 3, 48, 15)
# Find largest and smallest number without using min()/max()
largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)
# Check if two tuples are equal.
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (3, 2, 1)

print(t1 == t2)  
print(t1 == t3)
# Combine two tuples and display sorted result.
t1 = (9, 1, 4)
t2 = (5, 7, 2)
merged = tuple(sorted(t1 + t2))
print(merged)

 # Check Element Exists in Tuple
t=(10,20,30,40)
if 20 in t:
    print("Element found")
else:
    print("Not found")

# Nested Tuple Access
t = (1,2,(3,4,5))
print(t[2][1])  

# Find Index of an Element