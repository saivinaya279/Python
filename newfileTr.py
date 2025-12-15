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

# input and print

a=input()
b=input()
print(a+b)
print(type(a),type(b))

#print seperator(,space) and end (nextline) values
print("python","python","python")
print("python","python",sep="$$")
print("15","12","2025",sep="$")
print("Javascript",end="\t")
print("python")
print("java")

#operators:operators are used to perform operations on operands
#1.arithmetic operator()
print("2"+"2")
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10%5)
print(10**2)
print(100-98+21)

#relational operators
#equaility operator (==!==)
print("2"==2)
print(2==2)
print(True==1)
print(False==0)
# comparing strings
print(ord("A"),ord("a"))
# logical; operator and or
#and:for non-boolean values in **and** operator(if a is true result is b value,if a is false result is a)
print(100 and 10)  
print(0 and "")
print(" " and 0)
print(" "and "py") # only empty string is false value means("") ,space is not consider as empty(" ")
print(False and True)
print(True and False)
"""# a and b

If a is False → result is a

If a is True → result is b
# array without value is false value 
hese are False values:

0

"" (empty string)

[], {}, ()

None

False """
print([] and "js")
# **or**
# for non-boolean values in or (if a is true result is a value ,if a is false result is b)
print("" or "py")
print("js" or "py")
print(True or "true")
print(False or "false")
"""identity operator"""
# we use == for content comprision 
# we use= to assign a value
# identity operator for address comparision or memory location comparision
# # pvm doesnt store values it stores address or memory locaation:
# if a stores value 10(a=10),then is we store b=10 then the memory location of a,b is same
a=10
print(id(a),a)
b=10
print(id(b),b)
""" insted of doing the the id opertor we cn use ** is** operator to check whether the to values shring same location"""
# common locations can be stored in only int,str ,boolean ,..we cannot use for complex
# int
a=10
b=10
print(a is b)
name_1="py"
name_2="py"
print(name_1 is name_2)
# complex: they dont store same memory 
c1=10+5j
c2=10+5j
print(c1 is c2) # real and imaginry so not sme loction
c3=c2
print(c2 is c3) # here we re just ssigning so we get true
print(c2 is not c3)
# list
l1=[10,20]; # lis stores multiple values so we caannot store the same memory location
l2=[10,20]; 
print(l1 is l2) # false 
# if we want to store then we have to assign 
print(l1 = l2)