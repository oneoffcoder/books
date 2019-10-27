from datetime import date

# create a date manually
d = date(2019, 10, 31)
print(d)

# get the current date dynamically
d = date.today()
print(d)

# get the date from a timestamp
d = date.fromtimestamp(1555244364)
print(d)

# date difference
a = date(2019, 10, 31)
b = date(2019, 10, 30)
diff = a - b
print(diff)
