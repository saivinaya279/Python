# Write a program that reads a two-digit number N and checks if N is divisible by both the digits of N
# Print the double of N if N is divisible by both the digits of N Otherwise, print N
# Input
# The input will be a single line containing an integer representing N
# Output
# The output should be a single line containing an integer. The double of N should be printed if N is divisible by both the digits of N. Otherwise, N should be printed.

number=input()
AA=number[0]
BB=number[1]
AA=int(AA)
BB=int(BB)
CC=int(number)%AA==0 and int(number)%BB==0
if CC:
    print(int(number)*2)
else:
    print(number)
    
    

# Write a program that reads the rank R of a student and checks,
# If R is less than or equal to 3.
# If R is not less than or equal to 3, check if R is less than or equal to 10.
# Print One of Top 3 if the R is less than or equal to 3.
# Print Not Top 3 but One of Top 10 if R is less than or equal to 10 but not less than or equal to 3.
# Input
# The input will be a single line containing an integer representing R.
# Output
# The output should be a single line containing a string. One of Top 3 should be printed if R is less than or equal to 3. Not Top 3 but One of Top 10 should be printed if R is less than or equal to 10
R=int(input())
if R<=3:
    print("One of Top 3")
elif R<=10:
    print("Not Top 3 but One of Top 10")
    
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
W=int(input())
if W>=100:
    print("Box is Heavier")
elif W>=30:
    print("Box is Heavy")
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
Y=int(input())
if Y%400==0:
    print("True")
elif Y%4==0 and  Y%100!=0:
    print("True")
else:
        print("False")
        
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