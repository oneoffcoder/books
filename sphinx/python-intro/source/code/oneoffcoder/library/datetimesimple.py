import datetime

# get the date-time now
dt = datetime.datetime.now()
print(dt)

# create a date-time manually
dt = datetime.datetime(2019, 10, 31, 23, 55, 59, 100000)
print(dt)

# create a date-time from a string
dt = datetime.datetime.strptime('2019-10-31 23:55:59.999999', '%Y-%m-%d %H:%M:%S.%f')
print(dt)

# formatting date-time
s = datetime.datetime.strftime(dt, '%m-%d-%Y %l:%M:%S.%f %p')
print(s)

# subtract dates, datetime.timedelta
a = datetime.datetime(2019, 10, 31, 23, 55, 59, 100)
b = datetime.datetime(2018, 10, 31, 23, 55, 59, 100)
c = a - b
print(c)
