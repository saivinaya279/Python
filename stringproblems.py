
# Print each character of a string

s = "hello"
for ch in s:
    print(ch)

#Count vowels in a string

s = "hello"
vowels = 0
for char in s:
    if char in "aeiouAEIOU":
        vowels += 1
print(vowels)
# Count occurrences of a specific character
# Count occurrences of a specific characte

s = "hello"
count = 0
for char in s:
    if char == 'l':
        count += 1
print(count)
# Reverse a string
ch="hello"
rev=""
for i in ch:
    rev=i+rev
print(rev)
# Palindrome check
ch="qewr"
rev=""
for i in ch:
    rev=i+rev
if ch==rev:
    print("palindrome")
else:
    print("not palindrome")

# Write a Python program to remove all spaces from a given string.
s=" h e l l o"
result=""
for ch in s:
    if ch!=" ": # if  not space then 
        result+= ch # add to the result
print(result)

s="I love Python"
b="python"
c="java"
for ch in s:
    if b==len(s):
        b=c
    print(b)
"""Given a string and a word, check whether the string starts with or ends with that particular word.

Example:
Input: "Hello world", word = "Hello"
Output: String starts with 'Hello'

Input: "Hello world", word = "world"
Output: String ends with 'world'"""
s=input()
word=input()
start= True
for i in range(len(word)):
    if s[i]!=word[i]:
        start=False
        break
end= True
for i in range(1,len(word)+1):
    if s[-i]!=word[-i]:
        end=False
        break
if start:
    print("start")
elif end:
    print("end")
else:
    print("not ")

        
