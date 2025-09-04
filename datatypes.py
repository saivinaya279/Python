# The data types in python tell ,what type of variable is stored
# Seven in bulit types 
# int,float,bool,list,tuple,dictionary.

# Int(integers)     use case:(Lets you store multiple values in one variable.
# You can add/remove/search values easily.)
# Needed for counting, loops, indexing, math operations.
# Any program with calculation uses integers somewhere.
age = 21
students = 50
print(age + students)

# bool(boolean) use cases:(Login systems,yes/no questions.)
# Crucial for decision-making (if, while, conditions).
# Without booleans, programs can’t choose between options.
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
    
# string(str) use cases:(Displaying UI text, emails, usernames, chat messages.)
# Every app needs text: names, messages, input/output.
# String operations help formt data and show it nicely.
name = "Vinaya"
greeting = "Hello, " + name
print(greeting) 


# float use cases:(E-commerce prices, bank interest rates, measurements.)
#  Meaning: Numbers with decimal points.
# Needed for precise calculations like prices, percentages, scientific values.
# Avoids rounding issues
price = 99.50
discount = 12.5
final_price = price - discount
print(final_price)  # 87.0

# list use cases:(Shopping cart items, student names, database rows.)
# Meaning: Ordered collection (can change it).
# Lets you store multiple values in one variable.
# You can add/remove/search values easily.
fruits = ["apple", "banana", "mango"]
fruits.append("grape")
print(fruits)  

# tuple :Real-world use: GPS coordinates, fixed configurations, unchangeable settings.
# Why learn?
# Use when data should never change (security & performance).
# Tuples are faster than lists.
coordinates = (10, 20)
print(coordinates[0]) 
 
# dict (Dictionary):Real-world use: User profiles, settings, storing structured data.
# Meaning: Key–Value pairs (like a mini database).
# You can store related data together & access by key (like a name tag).
# Most real-world data is in key-value format (JSON, APIs, DBs).
student = {"name": "Vinaya", "age": 21, "branch": "CSE"}
print(student["branch"])  





