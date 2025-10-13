word="-R-a-v-i"
print(word[1:8:2])
a="waterfall"
part=a[1:8:2]
print(a[1:6:3])
print(part)
""" isdigit(), .strip(),.lower,.upper(),.startwith() .endswith,.replace()
 """
pin="457a677"
is_digit=pin.isdigit()
is_4_digit=(len(pin)==4)
is_valid=is_digit and is_4_digit
print(is_valid)
""" .strip() - removes all the leading trailing spaces from a string"""
mobilie="    893456232   "
print(mobilie)
print(mobilie.strip())

name="...vinaya....."
name=name.strip(".")
print(name)
# replace 
sentence=" teh cat and teh dog"
a= sentence.replace("teh","the")
print(a)
# .startswith(value): gives True if the string starts with the specified value otherwise ,False
url="https://dfghjk.com"
is_secure_url=url.startswith("https://")
print(is_secure_url)
# str_var.enswith(value)
gmail="vinaya@gmail.com"
is_gmail= gmail.endswith("@gmail.com")
# .upper()
name="yutyiku"
print(name.upper())
name="AGHHEWjkliuy"
print(name.lower())
""" Isalpha
Syntax: str_var.isalpha()

Gives True if all the characters are alphabets. Otherwise, False

"""
is_alpha = "Rahul".isalpha()
print(is_alpha)
""" Isdecimal
Syntax: str_var.isdecimal()

Gives True if all the characters are decimals. Otherwise, False

"""
is_decimal = "9876543210".isdecimal()
print(is_decimal)
""" Islower
Syntax: str_var.islower()

Gives True if all letters in the string are in lowercase. Otherwise, False
"""
is_lower = "hello ravi!".islower()
print(is_lower)

""" Isupper
Syntax: str_var.isupper()

Gives True if all letters in the string are in uppercase. Otherwise, False
"""
is_upper = "HELLO RAVI!".isupper()
print(is_upper)
"""Isalnum
Syntax: str_var.isalnum()

Gives True if the string is alphanumeric (a letter or a number). Otherwise, False"""
is_alnum = "Rahul123".isalnum()
print(is_alnum)
# Case Conversion Methods
""" Capitalize
Syntax: str_var.capitalize()

Gives a new string after converting the first letter in the string to uppercase and all other letters to lowercase."""
capitalized = "the Planet Earth".capitalize()
print(capitalized)
"""Title
Syntax: str_var.title()

Gives a new string after converting the first letter of every word to uppercase.

If a word contains a number or a special character, the first letter after that is converted to uppercase. """
title_case = "the planet earth".title()
print(title_case)
""" Swapcase
Syntax: str_var.swapcase()

Gives a new string after converting the uppercase letters to lowercase and vice-versa."""
swapped = "mY nAME IS rAVI".swapcase()
print(swapped)
# Counting and Searching Methods
"""Count
Syntax: str_var.count(str, start_index, end_index)

Here, the start_index and the end_index are optional.

The count() method gives the number of times the specified string str appears in the string. It searches the complete string as default.

If start_index and end_index are provided, it searches between these indices. The end_index is not included."""
text = "Hello, world!"
letter_count = text.count("l")
print(letter_count)
"""Index
Syntax: str_var.index(str, start_index, end_index)

Here, the start_index and the end_index are optional.

The index() method gives the index at the first occurrence of the specified string str.

It results in an error if the specified string str is not found.

The index() method searches the complete string as default. If start_index and end_index are provided, it searches between these indices. The end_index is not included."""
text = "I have a spare key, if I lose my key"
word_index = text.index("key")
print(word_index)


""" *rIndex*
Syntax: str_var.rindex(str, start_index, end_index)

Here, the start_index and the end_index are optional.

The rindex() method gives the index at the last occurrence of the specified string str.

It results in an error if the specified string str is not found.

The rindex() method searches the complete string as default. If start_index and end_index are provided, it searches between these indices. The end_index is not included."""
text = "I have a spare key, if I lose my key"
word_index = text.rindex("key")
print(word_index)
""" *Find*
Syntax: str_var.find(str, start_index, end_index)

Here, the start_index and the end_index are optional.

The find() method gives the index at the first occurrence of the specified string str.

If the specified string str is not found, it returns -1.

The find() method searches the complete string as default. If start_index and end_index are provided, it searches between these indices. The end_index is not included."""

# It works similarly to the index() method. The only difference is that the index() method results in an error if the specified string is not found, while find() does not.
text = "I have a spare key, if I lose my key"
word_index = text.find("key")
print(word_index)
# is string not found
text = "I have a spare key, if I lose my key"
word_index = text.find("is")
print(word_index)
"""rFind
Syntax: str_var.rfind(str, start_index, end_index)

Here, the start_index and the end_index are optional.

The rfind() method gives the index at the last occurrence of the specified string str.

If the specified string str is not found, it returns -1.

The rfind() method searches the complete string as default. If start_index and end_index are provided, it searches between these indices. The end_index is not included."""

# It works similarly to the rindex() method. The only difference is that the rindex() method results in an error if the specified string is not found, while rfind() does not."""
text = "I have a spare key, if I lose my key"
word_index = text.rfind("key")
print(word_index)
text = "coo coo coo"
word_index = text.rfind("co", 3, 10) # (substring,start ,end)
print(word_index)

"""ord() and chr() Functions
The ord() function returns the integer representing the Unicode code point of a given character. Conversely, 
the chr() function returns the character corresponding to a given integer."""

print(ord("a"))
print(ord("A"))
print(chr(97))
print(chr(65))

# String Immutability
# Strings in Python are immutable, meaning that once a string is created, its characters cannot be changed.
"""Creating Strings
Strings can be created using single quotes ', double quotes ", or triple quotes ''' and .''' Triple quotes allow for multi-line strings."""

string = "geek"
print(string)
print(string[0])
print(string[-1])
print(string[1])
print(string[-2])
"""Escape Sequences
  Single Quote (\'):"""
s = 'welcome to geek\'s course'
print(s)

"""New Line (\n):
The \n escape sequence adds a new line.

Example:"""
s = 'hi\nwelcome to the course'
print(s)

"""Tab (\t):
The \t escape sequence adds a tab space.
Example:"""
s = 'hi\twelcome to the course'
print(s)

"""Double Quote (\"):
To include a double quote inside a string that is enclosed by double quotes, you need to escape it.
Example:"""
s = "He said, \"Welcome to the course!\""
print(s)

"""Backslash (\):
To include a backslash itself, you need to escape it by using double backslashes.
Example:"""
s = 'This is a backslash: \\'
print(s)

"""Creating Raw Strings
Raw strings are created by prefixing the string with r or R.
"""
s1 = r'C:\project\name.py'
print(s1)