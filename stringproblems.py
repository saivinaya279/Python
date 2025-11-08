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
print(vowels)3
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
# 1. Reverse a string
ch="hello"
rev=""
for i in ch:
    rev=i+rev
print(rev)
# 2.Palindrome check
ch="qewr"
rev=""
for i in ch:
    rev=i+rev
if ch==rev:
    print("palindrome")
else:
    print("not palindrome")

# 3.Write a Python program to remove all spaces from a given string.
s=" h e l l o"
result=""
for ch in s:
    if ch!=" ": # if  not space then 
        result+= ch # add to the result
print(result)

# s="I love Python"
# b="python"
# c="java"
# for ch in s:
#     if b==len(s):
#         b=c
#     print(b)
""" 4.Given a string and a word, check whether the string starts with or ends with that particular word.

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

        
"""5.Given a sentence, write a program to capitalize the first letter of the sentence while keeping the rest of the characters unchanged.

Example:
Input: "hello world"
Output: "Hello world" """
s=input()
result=""
for i in range(len(s)):
    if i==0:
        result+=s[i].upper()
    else:
        result+=s[i]
print(result)
# direct
# s=input()
# s[0].upper+s[1:]
# print(s)
"""6.Given a sentence, count how many times each word appears in it and display the frequency of every word.

Example:
Input: "apple banana apple orange banana apple"
Output:

apple → 3  
banana → 2  
orange → 1"""
s=input()
words=s.split()
counted=[]
for i in range(len(words)):
    word=words[i]
    if word not in counted:
        count=0
        for j in range(len(words)):
            if words[j]==word:
                count+=1
        print( f"{word} ,{count}")
        counted.append(word)
"""Problem Statement: Count Consonants

Given a string s, write a program to count the total number of consonants present in the string.

A consonant is any alphabetic character that is not a vowel (i.e., not ‘a’, ‘e’, ‘i’, ‘o’, or ‘u’).
You should consider both uppercase and lowercase letters.

Example 1:

Input:
s = "Hello World"

Output:
7

Explanation:
The consonants are: H, l, l, W, r, l, d → total 7."""
s=input()
a=['A','E','I','O','U','a','e','o','i','u']
count=0
for ch in s:
    if ch.isalpha() and ch not in  a:
        count+=1
print(count)
"""Problem Statement: Find All Occurrences of a Substring

Given two strings, s (the main string) and sub (the substring), write a program to find all the starting indices where the substring sub occurs in s.

The search should be case-sensitive and should include overlapping occurrences.

Example 1:

Input:
s = "ABCDCDC"
sub = "CDC"

Output:
[2, 4]

Explanation:
The substring "CDC" appears starting at indices 2 and 4 in the main string "ABCDCDC"."""

s = input()
ss = input()

found = False

for i in range(len(s) - len(ss) + 1):
    if s[i:i+len(ss)] == ss:
        print(i)
        found = True

if not found:
    print("Substring not found")
    
#  Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.   # 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in map_s_t and map_s_t[char_s] != char_t:
                return False
            if char_t in map_t_s and map_t_s[char_t] != char_s:
                return False
            map_s_t[char_s] = char_t
            map_t_s[char_t] = char_s

        return True

        # leetcode
        class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = n1 + n2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        return ''.join(reversed(result))

