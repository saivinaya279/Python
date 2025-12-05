n = input()
count = 0
for i in range(len(n)):
    if n[i] in "aeiouAEIOU":
        count += 1
print(count)
"""# 🔵 SECTION A — Very Easy (Warmup: Q1–Q5)
1️⃣ Print your name 5 times.

(Use a loop)

2️⃣ Take two numbers as input and print their sum.
3️⃣ Take a string input and print its first and last character.
4️⃣ Find if a number is even or odd.
5️⃣ Create three variables (name, age, branch) and print them neatly.
🔵 SECTION B — Easy Basics (Q6–Q10)
6️⃣ Take a list of numbers and print the sum.
7️⃣ Count how many vowels are in a string.
8️⃣ Take a sentence and count how many words are present.
9️⃣ Check if two numbers are equal, greater, or smaller (using if-else).
🔟 Convert temperature from Celsius → Fahrenheit.

Formula:

F = (C × 9/5) + 32

🔵 SECTION C — Strings Practice (Q11–Q14)
1️⃣1️⃣ Reverse a string without using reverse()
1️⃣2️⃣ Count the number of uppercase and lowercase letters in a string.
1️⃣3️⃣ Replace all spaces in a string with underscores.
1️⃣4️⃣ Check if the given string is a palindrome.
🔵 SECTION D — List Practice (Q15–Q18)
1️⃣5️⃣ Find the largest and smallest element in a list.
1️⃣6️⃣ Remove duplicates from a list (without using set).
1️⃣7️⃣ Print the list in reverse order (without using reverse()).
1️⃣8️⃣ Add a new element at the beginning and end of a list.
🔵 SECTION E — Medium Level (Q19–Q20)
1️⃣9️⃣ From a list, print only the even numbers.
2️⃣0️⃣ Input 5 numbers from the user → store them in a list → print:

sum

average

max

min"""
# 1️⃣ Print your name 5 times.
n=input()
for i in range(5):
    print(n)
# 2️⃣ Take two numbers as input and print their sum.

# Write a Python program that asks the user to enter two numbers, adds them, and prints the total.
a=int(input())
b=int(input())
sum_o=a+b
print(sum_o)
# 3️⃣ Take a string input and print its first and last character.
a=input()
print(a[0])
print(a[-1])
# 4️⃣ Find if a number is even or odd.
a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")
# 5️⃣ Create three variables (name, age, branch) and print them neatly.
name=input()
age=int(input())
branch=input()
print("NAME",name)
print("AGE",age)
print("branch",branch)
# 6️⃣ Take a list of numbers and print the sum.
a=[2,3,5,7]
sum_=0
for i in a:
    sum_=sum_+i
print(sum_)
# 7️⃣ Count how many vowels are in a string.
a=input()
vowels=0
for i in range(len(a)):
    if a[i]in"aeiouAEIOU":
        vowels=vowels+1
print(vowels)
        
    
