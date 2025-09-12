# Write a program that reads a two-digit number N and checks if N is divisible by both the digits of N
# Print the double of N if N is divisible by both the digits of N Otherwise, print N
# Input
# The input will be a single line containing an integer representing N
# Output
# The output should be a single line containing an integer. The double of N should be printed if N is divisible by both the digits of N. Otherwise, N should be printed.

# number=input()
# AA=number[0]
# BB=number[1]
# AA=int(AA)
# BB=int(BB)
# CC=int(number)%AA==0 and int(number)%BB==0
# if CC:
#     print(int(number)*2)
# else:
#     print(number)
    
    

# Write a program that reads the rank R of a student and checks,
# If R is less than or equal to 3.
# If R is not less than or equal to 3, check if R is less than or equal to 10.
# Print One of Top 3 if the R is less than or equal to 3.
# Print Not Top 3 but One of Top 10 if R is less than or equal to 10 but not less than or equal to 3.
# Input
# The input will be a single line containing an integer representing R.
# Output
# The output should be a single line containing a string. One of Top 3 should be printed if R is less than or equal to 3. Not Top 3 but One of Top 10 should be printed if R is less than or equal to 10
# R=int(input())
# if R<=3:
#     print("One of Top 3")
# elif R<=10:
    # print("Not Top 3 but One of Top 10")
    
# Write a program that reads the weight W of a box in kg and checks,
# If W is greater than or equal to 100.
# If W is not greater than or equal to 100, check if Wis greater than or equal to 30.
# Print Box is Heavier if W is greater than or equal to 100.
# Print Box is Heavy if W is not greater than or equal to 100 but greater than or equal to 30.
# Input
# The input will be a single line containing an integer representing W.
# Output
# The output should be a single line containing a string. Box is
# Heavier should be printed if W is greater than or equal to 100. Box is Heavy should be printed if W is not greater than or equal to 100 but greater than or equal to 30.
# W=int(input())
# if W>=100:
#     print("Box is Heavier")
# elif W>=30:
#     print("Box is Heavy")
# Write a program that reads a year Y and checks if the year Yis a leap year. A year is a leap year if any of the given conditions are satisfied.
# Y is divisible by 400.
# .
# Y is divisible by 4, and not divisible by 100.
# Print True if any of the given conditions are satisfied. Otherwise,
# print False.
# Input
# The input will be a single line containing an integer representing
# Y
# Output
# The output should be a single line containing a boolean value. True should be printed if any of the given conditions are satisfied.
# Y=int(input())
# if Y%400==0:
#     print("True")
# elif Y%4==0 and  Y%100!=0:
#     print("True")
# else:
#         print("False")
        
# Write a program to display a customized message based on temperature T
# Input
# The first line is a real number T
# Output
# Print Freezing weather if T < 0
# Print Very Cold weather if 0 <= T < 10
# Print Cold weather if 10 <= T < 20
# Print Normal if 20 <= T < 30
# Print Hot if 30 <= T < 40
# Print Very Hot if T >= 40
T=float(input())
if T<0:
    print("Freezing weather")
elif 0<=T<10:
    print("Very Cold weather")
elif 10<=T<20:
    print("Cold weather")
elif 20<=T<30:
    print("Normal")
elif 30<=T<40:
    print("Hot")
else:
    print("Very Hot")
# Write a program that reads two strings Hand I and checks,
# If His equal to "Y".
# If His not equal to "Y", check if I is equal to "Y".
# Print Allowed to Exam - Has Hall ticket if His equal to "Y".
# Print Allowed to Exam - Has Identification Card if His not equal to "Y" and I is equal to "Y".
# Input
# The first line of input contains a string representing H.
# The second line of input contains a string representing 1.
# Output
# The output should be a single line containing a string. Allowed to Exam "Y". Allowed to Exam - Has Identification Card should be printed if - Has Hall ticket should be printed if His equal to His not equal to "Y" and I is equal to "Y".
    
H=str(input())
I=str(input())
if H=="Y":
    print("Alllowed to the exam")
elif H!="Y" and I =="Y":
    print("Allowes to exam-had identification card")
    

# Write a program that reads a number N and checks if N is divisible by 5 and 10.
# Print Divisible by 10 if N is divisible by 10.
# Print Divisible by 5 if N is divisible by 5 but not divisible by 10.
# Print Not Divisible by 10 or 5 if N is not divisible by 10 and N is not divisible by 5.
# Input
# The input will be a single line containing an integer representing N.
# Output
# The output should be a single line containing a string. Divisible by 10 should be printed if N is divisible by 10. Divisible by 5 should be printed if N is divisible by 5 but not divisible by 10. Not Divisible by 10 or 5 should be printed if N is not divisible by 10 and 5.
N=int(input())
if N%10==0:
    print("Divisible by 10")
elif  N%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")
# Write a program to calculate the grade of the student based on the marks he/she scored.
N=int(input())
if N>85:
    print("A")
elif N>70 or N<85:
    print("B")
elif N>60 or N<75:
    print("C")
elif N<60:
    print("F")
    
A=int(input())
B=int(input())
C=int(input())
if A>B:
    print("WIN")
elif A==B:
    print("DRAW")
elif A<B:
    print("LOSE")
# Write a program that reads the number N and prints the name of the polygon based on the N number of sides.
N=int(input())
if N<=3:
    print("Not a polygon")
elif N==3:
    print("Triangle")
elif N==4:
    print("quadrilateral")
elif N==5:
    print("Pentagon")
elif N>5:
    print("Big Polygon")
# leap year
Y=int(input())
if Y%400==0:
    print("True")
elif Y%4==0 and Y%100!=0:
    print("true")
else:
    print("False")
# Write a program that reads the Cost Price CP and Selling Price SP of a product and compares SP with CP
# print Profit if SP is greater than CP
# print Loss if SP is less than CP.
# print No Profit - No Loss if SP is equal to CP 
CP=int(input())
SP=int(input())
if SP>CP:
    print("Profit")
elif SP==CP:
    print("No Profit - No Loss")
else:
    print("Loss")
# Day name according to the 1 ex:1=monday.....7=sunday 
D=int(input())
if D==1:
    print("Monday")
elif D==2:
    print("Tuesday")
elif D==3:
    print("Wednesday")
elif D==4:
    print("Thursday")
elif D==5:
    print("Friday")
elif D==6:
    print("Saturday")
elif D==7:
    print("Sunday")
# Write a program that reads an operator O, and two numbers A and B
# Print the result by doing arithmetic operations on A and B based on the operator C
OP=input()
A=int(input())
B=int(input())
if OP=="+":
    print(A+B)
elif OP=="-":
    print(A-B)
elif OP=="*":
    print(A*B)
elif OP=="%":
    print(A%B)
else:
    AA=float(A/B)
    print(AA)
# Input
# The first line of input will contain an integer.
# Output
# The first line of output should be the sum of the digits.
A=(input())
AA=len(A)
if AA==1:
    print(A)
elif AA==2:
    a=int(A[0])
    b=int(A[1])
    print(a+b)
elif AA==3:
    a=int(A[0])
    b=int(A[1])
    c=int(A[2])
    print(a+b+c)
elif AA==4:
    a=int(A[0])
    b=int(A[1])
    c=int(A[2])
    d=int(A[3])
    print(a+b+c+d)