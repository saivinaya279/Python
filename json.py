"""# JSON in Python
Python has a built-in package called json, which can be used to work with JSON data."""
import json
"""Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method."""
# Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
"""Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method."""
# Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
