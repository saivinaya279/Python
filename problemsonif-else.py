# Write a program that reads a number and converts it to a positive number.
# If the given number is negative, convert it to a positive number and print it. Otherwise, print the given number.
a=int(input())
if (a<0):
    a=a*(-1)
print(a)
# Write a program that reads the student's marks as input and prints PASS or FAIL.If the student has scored more than 50, print PASS.
# In all other cases print FAIL.
# Input:
# The input will be a single line containing a number.
# Output:
# The output should be a single line containing PASS or FAIL.
a=int(input())
if (a>50):
    print("PASS")
else:
    print("FAIL")
# Solved
# Write a program that reads two numbers A and B and prints the greatest among the two numbers.
# Input
# The first line of input contains an integer representing A
# The second line of input contains an integer representing B
# Output
# The output should be a single line containing an integer that is the greatest among the two numbers.
a=int(input())
b=int(input())
if (a>b):
    print(a)
else:
    print(b)
# Write a program that reads the age of a person and checks if the age of the person is greater than or equal to 18 for eligibility to vote.
# Print Eligible if the age of the person is greater than or equal to 18, otherwise print Not Eligible.
# Input
# The input will be a single line containing an integer.
# Output
# The output should be a single line containing a string. Eligible should be printed if the age of the person is greater than or equal to 18, otherwise Not Eligible should be printed.
a=18
b=int(input())
if(b>=a):
    print("Eligible")
else:
    print(" not Eligible")
# Write a program to print the relation between two numbers, X and Y.
# Input
# The first line is integer X.
# The second line is integer Y
# Output
# Print XY if X is less than Y otherwise, print X >= Y.
first_number=int(input())
second_number=int(input())
if first_number<second_number:
    print("X < Y")
else:
    print("X >= Y")
# Write a program to check if the given two numbers are equal.
# Input
# The first line of input contains a number.
# The second line of input contains a number.
# Output
# If the given numbers are equal, print "Equal". In all other cases, print "Not Equal".
a=int(input())
b=int(input())
if a==b:
    print("Equal")
else:
    print(" Not Equal")
# Input
# The first line of input will contain the length of the box.
# The second line of input will contain the breadth of the box.
# Output
# If the given length and breadth are equal, print "Square". In all other cases, print "Rectangle".
lenght=int(input())
breadth=int(input())
if lenght==breadth:
    print("Square")
else:
    print("Rectangle")
# Input
# The input will be a single line containing an integer.
# Output
# The output should be a single line containing a string. Eligible should be printed if the age of the person is greater than or equal to 18, otherwise Not Eligible should be printed.
age=int(input())
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")
# Input
# The input will be a single line containing an integer.
# Output
# The output should be a single line containing a string. Can go for a walk should be printed if the temperature is between 15 and 40, otherwise Cannot go for a walk should be printed.
temper=int(input())
AA=temper>15 and temper<40
if AA:
    print("Can go for a walk" )
else:
    print("Cannot go for a walk")
# Input
# The first line of input contains an integer representing A
# The second line of input contains an integer representing B.
# Output
# The output should be a single line containing a string. Pair should be printed if both A and B are less than or equal to 1000 or B is greater than 500. Otherwise, Not a Pair should be printed.
A=int(input())
B=int(input())
aa=A<=1000 and B<=1000
bb=B>500
if aa or bb:
    print("Pair")
else:
    print("Not a Pair")
# Input
# The first line of input contains an integer representing the score
# The second line of input contains an integer representing the score B
# Output
# The output should be a single line containing a string. Can team up should be printed if one of the scores is greater than 300 and the sum of the scores is less than 500, otherwise Cannot team up should be printed.
playerA=int(input())
playerB=int(input())
AA=playerB>300 or playerA>300
BB=playerA+playerB<500
if AA and BB:
    print("Can team up")
else:
    print("Cannot team up")
# Input
# The input will be a single line containing an integer.
# Output
# The output should be a single line containing a string. Zero should be printed if the given number is equal to 0. Positive should be printed if the given number is greater than 0.
number=int(input())
if number==0:
    print("Zero")
else:
    print("Positive")


# Input
# The first line of input contains a string representing S
# The second line of input contains an integer representing C.
# Output
# The output should be a single line containing a string. Buy a Book should be printed if S is equal to large or C is greater than or equal to 300. Otherwise, Do Not Buy a Book should be printed.
String=input()
noofpages=int(input())
if String==("large") or noofpages>=300:
    print("buy a Book")
else:
    print("Do Not Buy a Book")
# Input
# The first line of input contains an integer representing the score A
# The second line of input contains an integer representing the score B
# Output
# The output should be a single line containing a string. Can team up should be printed if one of the scores is greater than 300 and the sum of the scores is less than 500, otherwise Cannot team up should be printed.
A=int(input())
B=int(input())
a=B>300 or A>300
b=A+B<500
if a and b:
    print("can team up")
else:
    print("cannot team up")

# Write a program that reads a number N and checks if N is greater than 10.
# Print the result of N + 5 if N is greater than 10. Otherwise, print the result of N + 1
# Input
# The input will be a single line containing an integer representing N
# Output
# The output should be a single line containing an integer. The result of N + 5 should be printed if N is greater than 10. Otherwise, the result of N + 1 should be printed.
a=int(input())
if a>=10:
    print(a+10)
else:
    print(a+1)
# Input
# The first line of input contains an integer representing angle A
# The second line of input contains an integer representing angle B
# The third line of input contains an integer representing angle C
# Output
# The output should be three lines containing a Triangle as shown in the sample output if the sum of A 180. B and C is equal to
# Otherwise, the output should be a single line containing the string Not a Valid Triangle.
A=int(input())
B=int(input())
C=int(input())
if A+B+C==180:
    print("*")
    print("**")
    print("***")
else :
    print("Not valid triangle")
# Write a program that reads three numbers A B, and C , and checks if each number is greater than 100.
# Print All are greater than 100 if each number is greater than 100. Otherwise, print Not all are greater than 100.
# Input
# The first line of input contains an integer representing A
# The second line of input contains an integer representing B
# The third line of input contains an integer representing C
# Output
# The output should be a single line containing a string. All are greater than 100 should be printed if each number is greater than 100. Otherwise, Not all are greater than 100 should be printed.
A=int(input())
B=int(input())
C=int(input())
if A+B+C>100:
    print("All are greater than 100")
else:
    print("Not all are greater than 1000")
# A company decided to give a bonus of 5% to an employee if his/her years of service is more than five years.
# write a program that reads an employee's salary and years of service and decides whether the employee gets the bonus or not.
# input
# The first line of input will contain the salary of an employee.
# The second line of input will contain years of service.
# Output
# the employee gets a bonus, print the net bonus amount.
# the employee doesn't get the bonus, print "No Bonus",.
salary=int(input())
exprince=int(input())
if exprince>5:
    print(salary*0.05)
else:
    print("No Bonus")
    
# Write a program that reads two numbers A and B and checks if one of the below conditions is satisfied.
# One of A and B is equal to 6.
# The sum of A and B is equal to 6.
# The difference between A and B is equal to 6.
# Print Lucky if one of the given conditions is satisfied. Otherwise, print Not Lucky. 
# Input
# The first line of input contains an integer representing A
# The second line of input contains an integer representing B.
# Output
# The output should be a single line containing a string. Lucky should be printed if one of the given conditions is satisfied.
# Otherwise, Not Lucky should be printed.
    
A=int(input())
B=int(input())
a=A==6 and B == 6
b=A+B==6
c=A-B==6 or B-A==6
if a or b or c:
    print("Lucky")
else:
    print("Not Lucky")
A=int(input())
B=int(input())
# Write a program that reads two numbers A and B, and prints the remainder when A is divided by B
# Input
# The first line of input contains an integer representing A.
# The second line of input contains an integer representing B
# Output
# The output should be a single line containing an integer that is the remainder when A is divided by B
a=int(input())
b=int(input())
print(a%b)
# Solved
# Write a program that reads a number N and checks if Nis divisible by 2.
# Print Even if N is divisible by 2. Otherwise, print Odd.
# Input
# The input will be a single line containing an integer representing N
# Output
# The output should be a single line containing a string. Even should be printed if N is divisible by 2. Otherwise, Odd should be printed.
N=int(input())
if N%2==0:
    print("even")
else:
    print("odd")
    
# Write a program that reads a number N and finds the,
# Remainder when N is divided by 4.
# Remainder when N is divided by 5.
# Print the greatest remainder among the two remainders when Nis divided by 4 and 5.
# Input
# The input will be a single line containing an integer representing N
# Output
# The output should be a single line containing an integer that is the greatest remainder among the two remainders when N is divided by 4 and 5.
N=int(input())
A=N%4
B=N%5
if A>B:
    print(A)
else:
    print(B)
# Write a program that reads a number N and checks if the remainder is O or 1 when N is divided by 11.
# Print Special Eleven if the remainder is 0 or 1 when N is divided by 11. Otherwise, print Normal Number.
# Input
# The input will be a single line containing an integer representing N.
# Output
# The output should be a single line containing a string. Special Eleven should be printed if the remainder is 0 or 1 when N is divided by 11. Otherwise, Normal Number should be printed.
N=int(input())
if N%11==0 or N%11==1:
    print("special Number")
else:
    print("Normal Number")

# Even or Odd
num = int(input())
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
# Sum of Digits
num = int(input("Enter a number: "))
total = 0
for digit in str(num):
    total += int(digit)
print(total)

# Count Vowels in a String
text = input()
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print(count)

# Largest of Three Numbers
a = int(input())
b = int(input())
c = int(input())
if a>=b and a>=c:
    print(a)
elif b>=c:
    print(b)
else:
    print(c)
    
# Fibonacci Series
n = int(input())
a,b=0,1
for i in range(n):
    print(a, end=" ")
    a,b=b,a+b
    
# Reverse a String
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)

# Max in List
lst = [3, 7, 2, 9, 5]
max_num = lst[0]
for x in lst:
    if x > max_num:
        max_num = x
print(max_num)

# Remove Duplicates
lst = [1, 2, 2, 3, 4, 4, 5]
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print(unique)