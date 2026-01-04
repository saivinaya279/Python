"""BASIC QUESTIONS

Create a dictionary with 5 key–value pairs.

Access a value using a key.

Add a new key–value pair to an existing dictionary.

Update the value of an existing key.

Delete a key from a dictionary.

Check whether a key exists in a dictionary.

Find the number of key–value pairs in a dictionary.

Print all keys of a dictionary.

Print all values of a dictionary.

Print all key–value pairs.

🟡 INTERMEDIATE QUESTIONS

Count the frequency of each element in a list using a dictionary.

Count the frequency of characters in a string.

Find the key with the maximum value in a dictionary.

Find the key with the minimum value in a dictionary.

Merge two dictionaries into one.

Remove duplicate values from a dictionary.

Convert two lists into a dictionary.

Sort a dictionary by keys.

Sort a dictionary by values.

Reverse keys and values of a dictionary.

🔵 LOGIC BUILDING / INTERVIEW QUESTIONS

Find the first non-repeating character in a string using a dictionary.

Check whether two strings are anagrams using a dictionary.

Find all elements that appear more than once in a list.

Find the most frequent element in a list.

Group words with the same frequency of characters.

Check if all values in a dictionary are unique.

Find common keys between two dictionaries.

Find common values between two dictionaries.

Replace dictionary values with their squares.

Create a dictionary from a string where keys are characters and values are ASCII codes.

🔴 ADVANCED / PLACEMENT LEVEL

Given a dictionary of student marks, find the topper.

Given a sentence, find the word with highest frequency.

Implement a phone directory using dictionary.

Design a dictionary-based login system.

Implement LRU Cache logic using dictionary.

Find pairs of elements whose sum is equal to a given number.

Find subarray with zero sum using dictionary.

Find longest substring without repeating characters.

Group anagrams from a list of strings.

Find number of good pairs (i < j and nums[i] == nums[j])."""
d1={1:'Geeks',2:'for',3:'geeks'}
print(d1)
# create dictionary using dict() constructor
d2=dict(a="geeks",b="for",c="geeks")
print(d2)
# Accessing Dictionary Items
"""We can access a value from a dictionary by using the key within square brackets or get() method."""
print(d2["a"]) # access using key
# access using get()
print(d2.get("b"))
# Adding and Updating Dictionary Items
# We can add new key-value pairs or update existing keys by using assignment.
d2["age"]=22 # adding a new key- value pair
d2["a"]="love"
print(d2)
"""Removing Dictionary Items
We can remove items from dictionary using the following methods:

del: Removes an item by key.
pop(): Removes an item by key and returns its value.
clear(): Empties the dictionary.
popitem(): Removes and returns the last key-value pair."""
# Using del to remove an item
del d2["age"]
print(d2)
# Using pop() to remove an item and return the value
val=d2.pop("b")
print(val)
# using popitem to removes and returns
# the last key-value pair
key,val=d2.popitem()
print(f"Key:{key},Value:{val}")
print(d2)
# Clear all items from the dictionary
d2.clear()
print(d2)
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
# nested
d = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(d)
student = {
    "name": "Vinaya",
    "age": 20,
    "course": "Data Science"
}
print(student)
 # Create a dictionary with 5 key–value pairs.
student={
    "name":"vinaya",
    "age":20,
    "course":"ds",
    "email" : " kumbamsai@gmail.com",
    "roll no":280
}
print(student)
student["college"] = "GITAM"
student["age"] = 21
del student["course"]     # remove specific key
student.pop("age")        # remove and return value

print(student)
# Count the frequency of each element in a list using a dictionary.
n=[1,2,3,1,2,3]
freq={}
for num in n:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)
# othere method (refer notes)
nums = [1,2,2,3,1,1]
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1 # (key,default)

print(freq)
