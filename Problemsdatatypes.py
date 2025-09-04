# INTEGERS
# Add two integers and check the type of the result.
# Divide two integers and check the type of the result.
a=20
b=30 
c=a+b
print(type(c))
d=30
e=20
f=d/e
print(type(f))
# Strings
# Convert a string into uppercase and lowercase.
text = "VinAya"
lower_text = text.lower()
print(lower_text) 

text="vinaya"
upper_text=text.upper()
print(upper_text)
# Extract the first and last character of a string.
text="Vinaya"
print(text[0])
print(text[5])

# LISTS
# Create a list of numbers and print its type.
text=[1,3,4,6]
print(type(text))
# Find the length of a list.
text=[1,2,3,6,5]
print(len(text))
# Access the first, middle, and last elements from a list.
text=[1,2,3,6,5]
print(text[0])
print(len(text)//2)
print(text[-1])
# Append an element to a list and print it.
text=[3,5,6,7]
text.append(4)
print(text)

# tuples
# Create a tuple and print its type.
text=(1,2,4,5,7,3,2,8,2)
print(type(text))
# Find how many times a value appears in a tuple using .count().
print(text.count(2))
# Convert a tuple into a list.
text=("sdfgh","sdfghj","rtvb")
char_list=list(text)
print(char_list)
