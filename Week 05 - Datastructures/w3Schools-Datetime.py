# Practicing datetime function, examples in https://www.w3schools.com/python/python_datetime.asp
# Author: Ross Downey

import datetime

x = datetime.datetime.now()
print(x) # displays the current date and time


print(x.year) # prints what year it is
print(x.strftime("%A")) # strftime % A gives the day

y = datetime.datetime(2021, 2, 19) # telling the program what date it is (year, month, day)
# default 00:00:00 for time

print(y)

z = datetime.datetime(2021, 2, 19)

print(z.strftime("%B")) # strftime %B will give the month
print (z.strftime("%A")) # strftime %A will give the day
print (z.strftime("%w")) # strftime %w will give the day as a number (0 = Sunday, 6 = Saturday)