
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
    if ch!=" ":
        result+= ch
print(result)