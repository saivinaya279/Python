#identifiers
name="python"
print(name)
A="python"
print(A)
"""rules
#usage:we can declare a identifier with a-zz,A-z,
# but we cannot stat with a number or special characters lie eg:_,@# etc:
#1person :it wont work
and we can't use reserve keywords, (ex:long,for if ),we can't start with them
# It is case sensitive"""
#variables
"""Its is a container to store values
# """
a=10
print(type(a))
print(id(a))
#reserve keyword
import keyword
print(keyword.kwlist)
# datatypes
""" # primitive datatypes:int,float,complex,str,boolean
# non-primitive datatypes(list,tuple,set,dict)"""


# LISTS :

# List is the ordered collection of elements.
# Lists is used to represent group of elements in ordered way with dynamic nature.
# Lists are ordered, mutable, and allow duplicate values.

emptyList=[];
print(len(emptyList))
language =["js","python","java","c++","c"]
print(language[3])  # indexing
print(language[4])
print(language[-1])  # negative indexing

# Slicing:

print(language[0:2])  # from index 1 to index 2 
print(language[2:0])   # from index 2 to index 0  , we get empty list as output because slicing works from left to right
print(language[4:1])   # from index 4 to index 1 , we get empty list as output because slicing works from left to right
print(language[1:])   # from index 1 to end
print(language[:3])   # from start to index 3
print(language[:])    # from start to end
print(language[4:1:-1])  # reverse slicing from index 4 to index 1, we get ['c', 'c++', 'java'] as output because of step -1
print(language[1:4:-1])  # reverse slicing from index 1 to index 4, we get empty list as output because slicing works from left to right
print(language[::-1])  # reverse the list, we get reversed list as output because of step -1
print(language[3:4:-1])  # reverse slicing from index 3 to index 4, we get empty list as output because slicing works from left to right
# Tuples :
# Tuple is the ordered collection of elements.
# Tuples is used to represent group of elements in ordered way with static nature.
# Tuples are ordered, immutable, and allow duplicate values.

emptyTuple=();
print(len(emptyTuple))
fruits =("apple","banana","mango","grapes","orange")
print(fruits[2])  # indexing
print(fruits[-1])  # negative indexing

t = ()
print(type(t))  # tuple
t1=(10,)
print(type(t1))
# creating tuple without parentheses
anime="one picece","spy family","naruto"
print(type(anime))  # tuple
print(anime[0:1])


# Sets :
# Set is the unordered collection of elements.

# empty set
s = {}
print(type(s))  # dict
# to create empty set
s = set()
print(type(s))  # set
s1 = {10,20,30,40,50}
print(s1)
# # Remove the duplicates from the list using set
# list = [100,200,300,100,200,400]
# s = list(set[list])
# print(s)


# # Dictionaries :
# # Dictionary is the unordered collection of key-value pairs.

# student = {
#     "name": "Ravi",
#     "age": 24,
#     "course": "datascience",
#     "college": "mru",
#     "yearsofstudy":4,
# }
# # Accessing values from dict by dot or []
# print(student["name"])
# print(student['college'])

# # formatting strings
# print(f"my name is {student["name"]}")
#dictionary key-value pairs
student={
    "name":"Alice",
    "age":20,
    "courses":["Math","Science","Art"]
}
#accessing values

print("Student Name:",student["name"])
print("Student Courses:",student["courses"])
print("One subjectz:",student["courses"][0:])
print(f"My name is {student['name']}and i am studying {student['courses'][1]} and my age is {student['age']} i Got {300+200} marks ")
print("My name is {} and i am studying {} and my age is {} ".format(student['name'],student['courses'][0],student['age']))
# type casting : converting one data type to another type
# converting str to int type *** it should be only base0(0-9) numbers ***
print("10")
"""print(int("10.55"))# we cannot convert flot string values into integers
print(int("10+5j"))#we cannot convert into int ,because we can only converty before 9 or 9 
print(int("ten")) we cannot convert normaal characters into integers"""
print(int("10"))
# converting str to floaat
print(float("10"))
print(float("100.5"))
# print(float("10+5j"))
# print(float("ten"))
print(float(True))# we will get 1.0 because the True means *1*
print(float(False))# we will get 0.0 because the false means "0"
# converting str into complex
print(complex("10"))
print(complex("10.5"))
print(complex(100,5))
print(complex(10.5,5.5))
print(complex(True,False))