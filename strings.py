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