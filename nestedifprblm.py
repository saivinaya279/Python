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
# Write a program that reads a string S and checks if all the given conditions are satisfied.
# The first three characters of S is NXT.
# The remaining characters of S contain a Number. Number is divisible by 2 or 7.
# Print Special String if all the given conditions are satisfied.
# Otherwise, print Not a Special String.
# Input
# The input will be a single line containing a string representing S
# Output
# The output should be a single line containing a string. Special String should be printed if all the given conditions are satisfied.
# Otherwise, Not a Special String should be printed.
string=input()
AA=string[:3]
BB=string[3:]
BB=int(BB)
A=AA=="NXT"
B=int(2)
C=int(9)
CC=BB%B==0 or BB%C==0
if A and CC:
    print("Special String")
else:
    print("Not a Special String")
    