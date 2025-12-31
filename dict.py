d1={1:'Geeks',2:'for',3:'geeks'}
print(d1)
# create dictionary using dict() constructor
d2=dict(a="geeks",b="for",c="geeks")
print(d2)
# Accessing Dictionary Items
"""We can access a value from a dictionary by using the key within square brackets or get() method."""
print(d2["a"]) # access using key
# access using get()
print(d2.get("b"))
# Adding and Updating Dictionary Items
# We can add new key-value pairs or update existing keys by using assignment.
d2["age"]=22 # adding a new key- value pair
d2["a"]="love"
print(d2)
"""Removing Dictionary Items
We can remove items from dictionary using the following methods:

del: Removes an item by key.
pop(): Removes an item by key and returns its value.
clear(): Empties the dictionary.
popitem(): Removes and returns the last key-value pair."""
# Using del to remove an item
del d2["age"]
print(d2)
# Using pop() to remove an item and return the value
val=d2.pop("b")
print(val)
# using popitem to removes and returns
# the last key-value pair
key,val=d2.popitem()
print(f"Key:{key},Value:{val}")
print(d2)
# Clear all items from the dictionary
d2.clear()
print(d2)
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
# nested
d = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(d)