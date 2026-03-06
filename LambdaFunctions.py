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
# Using with filter()
# filter() function uses a lambda expression to select elements from a list that satisfy a given condition, such as keeping only even numbers.
c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))
# . Using with map()
a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(list(double))
"""[2, 4, 6, 8]
Explanation:

The lambda function doubles each number.
map() iterates through a and applies the transformation."""
# Square of numbers
nums = [1, 2, 3, 4, 5]

result = list(map(lambda x: x**2, nums))

print(result)
# Convert to uppercase
words = ["apple", "banana", "mango"]

upper_words = list(map(lambda x: x.upper(), words))

print(upper_words)
# Add two lists
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))

print(result)
# Multiply by 10
nums = [2, 3, 4, 5]

result = list(map(lambda x: x * 10, nums))

print(result)
# # Even numbers
nums = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x: x % 2 == 0, nums))

print(even)
# Numbers > 3
nums = [10,25,30,45,50]

result = list(filter(lambda x: x > 30, nums))

print(result)
# Descending order
nums = [5,2,8,1,9]

result = sorted(nums, key=lambda x: -x)

print(result)