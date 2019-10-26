# create a tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# create a tuple without parentheses
numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9

# access elements of a tuple
x = numbers[0]
y = numbers[1]
z = numbers[3]

print(x, y, z)

# slicing a tuple
x = numbers[0:5]

print(x)

# check membership
result = 3 in numbers

# concatenation
numbers = (1, 2, 3, 4, 5) + (6, 7, 8, 9)

# expansion
t = (10, )
u = t * 10

# get the number of elements in tuple
len(numbers)
