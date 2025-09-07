# Conditional Statements in Python
# Conditional statements in Python are used to execute certain blocks of code based on specific conditions. 
# If Conditional Statement
# If statement is the simplest form of a conditional statement. It executes a block of code if the given condition is true.
# If Statement 
# if condition:
    # this block will excute
age = 20
if age >= 18:
    print("Eligible to vote.")
# Short Hand if
age=22
if age >18:print("eligible to vote ")
# If else Conditional Statement
# When If - Else conditional statement is used, Else block of code executes if the condition is False
a = int(input())
if a > 0:  
    print("Positive")  
else:  
    print("Not Positive")  
print("End")
age = 30
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
# The short-hand if-else statement allows us to write a single-line if-else statement.
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")
# elif Statement
# elif statement in Python stands for "else if." It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true. 
a=6
b=((a*12)==32)
if b:
    print("True")
else:
    print("False")
a = 15
b = 8
if a>b:
    print(a-b)
print(a+b)
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
# Nested if..else Conditional Statement
# Nested if..else means an if-else statement inside another if statement. We can use nested if statements to check conditions within conditions.
ge = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
