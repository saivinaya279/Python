# Python Lambda Functions
""" Lambda functions are small anonymous functions, meaning they do not have a defined name."""
a = 'GeeksforGeeks'
upper = lambda x: x.upper()  
print(upper(a))
# use cases
""". Using with Condition Checking
A lambda function can use conditional expressions (if-else) to return different results based on a condition."""
check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))   
print(check(-3))  
print(check(0))
"""checks divisibility by 2 and returns "Even" or "Odd" accordingly.

"""



check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7))
"""Using with List Comprehension
Lambda functions can be combined with list comprehensions to apply the same operation to multiple values in a compact way."""
func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())
# Using for Returning Multiple Results
"""Although a lambda can contain only one expression, it can still return multiple results by combining them into a tuple."""
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)