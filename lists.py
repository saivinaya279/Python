# What is a List?

# A list is an ordered, mutable (changeable) collection that can hold different data types.

fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["hello", 5, True, 3.14]
# 2️ Accessing Elements

# Python lists are zero-indexed (first element → index 0).

# You can also use negative indexing (last element → index -1).

fruits = ["apple", "banana", "cherry"]
print(fruits[0])   
print(fruits[-1])  
# Modifying & Deleting
# 
# Lists are mutable — you can change or remove elements.

fruits[1] = "mango"      
print(fruits)            
# delete
del fruits[2]            # delete using del
print(fruits)    
# List creation + indexing.

# Example:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

nums = [1,2,1]
ans = nums + nums
print(ans)
# Create & Print
colors = ["red", "green", "blue", "yellow"]
print(colors[0])    
print(colors[-1])   
# replace
animals = ["cat", "dog", "rabbit", "tiger"]
animals[1] = "lion"
print(animals)
# Access Using Negative Index
numbers = [10, 20, 30, 40, 50]
print(numbers[-2])  
print(numbers[-1])  
# List Slicing
movies = ["Inception", "Avatar", "Titanic", "Joker", "RRR", "KGF"]
print(movies[1:4])
# ️Delete Element
fruits = ["apple", "banana", "cherry", "mango"]
del fruits[1]
print(fruits)
# del list[index] removes the element at that index.

#  Length of List
subjects = ["Math", "Science", "English", "History", "Civics"]
print(len(subjects))
#  len() gives the total number of elements in the list.
# Combine Lists
a = [1, 2, 3]
b = [4, 5, 6]
combined = a + b
print(combined)
# ️ Slicing Trick
nums = [5, 10, 15, 20, 25, 30]
print(nums[::-1])
#  [::2] → step of 2, so it picks every second element starting from index 0.

