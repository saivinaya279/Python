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