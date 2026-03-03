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
