from datetime import datetime

# get the date-time now
dt = datetime.now()
print(dt)

# create a date-time manually
dt = datetime(2019, 10, 31, 23, 55, 59, 100000)
print(dt)

# create a date-time from a string
# the date format code is available at https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# strptime stands for string parse time
dt = datetime.strptime('2019-10-31 23:55:59.999999', '%Y-%m-%d %H:%M:%S.%f')
print(dt)

# formatting date-time
# strftime stands for string format time
s = datetime.strftime(dt, '%m-%d-%Y %H:%M:%S.%f %p')
print(s)

# subtract dates, datetime.timedelta
a = datetime(2019, 10, 31, 23, 55, 59, 100)
b = datetime(2018, 10, 31, 23, 55, 59, 100)
c = a - b
print(c)
