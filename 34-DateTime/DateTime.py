# Importing the datetime module
import datetime

# Setting the date and time
date = datetime.date(2020, 1, 1)
time = datetime.time(00, 00, 00)

# Printing date and time
print(date)
print(time)
print()

# Printing values from date and time
print(date.year)
print(time.hour)
print()

# Retrieving the current date and time
now = datetime.datetime.now()

# Printing the current date and time
print(now)