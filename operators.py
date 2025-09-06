# Operators in Python
# Operators Type
# Arithmetic operator:+, -, *, /,%
# Relational operator:<,<=,>,>=,==,!,!=
# Logical operator:AND, OR, NOT
# Bitwise operator:&, |,<<,>>,-,^
# Assignment operator:=,+=,-=,^ * =,\%=
# identity operators:is,is not 
# Membership operators:in ,not in

 
# OPERATORS: These are the special symbols. Eg- + , * , /, etc.
# OPERAND: It is the value on which the operator is applied.
# Arithmetic Operators:
# Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.
a=15
b=4
# addition
print(a+b)
print(a-b)  # Subtraction
print(a*b)# Multiplication
print(a/b)# Division
print(a//b)# Floor Division
print(a%b) # Modulus
print(a**b)#Exponentiation
# comparison operators or relational operators:<,<=,>,>=,==,!,!=
# In Python Comparison of Relational operators compares the values. It either returns True or False according to the condition.
a = 13
b = 33
print(a>b)
print(a<b)
print(a<=b)
print(a!=b)
print(a>=b)
# Logical Operators:AND, OR, NOT
# It is used to combine conditional statements.
print("/n")
a = True
b = False
print(a and b)#True if both statements are the same
print(a or b)#True if one of the statements is true.
print(not a)#Reverse the result

# # Python Assignment Operators:=,+=,-=,^ * =,\%=
# Assignment operators are used to assign values to variables:
x = 5
print(x)
x = 5
x += 3
print(x)
x = 5
x -= 3
print(x)
x = 5
x *= 3
print(x)
x = 5
x /= 3
print(x)
x=5
x<=3
print(x)
x=5
x%=3
print(x)
# Bitwise Operators
# Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR
a = 10
b = 4
print(a & b) #AND → 1 only if both bits are 1
print(a | b)#OR → 1 if any one bit is 1
print(~a) #-(a+1)
print(a ^ b)#XOR → 1 if bits are different
print(a >> 2)#Right shift moves bits to the right by 2 places.
print(a << 2)#Left shift moves bits left by 2 places (adds two 0s at right).
