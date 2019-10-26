# do not do this, it's not memory efficient
x = (10, ) * 100000
y = [num * 2 for num in x]

# do this instead, use a generator comprehension
x = (10, ) * 100000
y = (num * 2 for num in x)