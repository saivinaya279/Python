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