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