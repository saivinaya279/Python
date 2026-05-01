# Getting current date
import datetime

x = datetime.datetime.now()
print(x)
# Getting only date
import datetime

x = datetime.date.today()
print(x)
# Accessing year, month, day
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.month)
print(x.day)
# Creating a custom date
import datetime

x = datetime.datetime(2025,5,10)

print(x)
# Formatting dates (very important)

# Using strftime()

import datetime

x = datetime.datetime.now()

print(x.strftime("%Y"))  # Year
print(x.strftime("%B"))  # Month name
print(x.strftime("%A"))  # Day name
# Date difference (important in data analysis)
import datetime

d1 = datetime.date(2025,5,1)
d2 = datetime.date(2025,5,10)

diff = d2 - d1

print(diff.days)
