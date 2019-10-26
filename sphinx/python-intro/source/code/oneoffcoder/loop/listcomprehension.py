# do not create a list this way

numbers = []
for num in [1, 2, 3, 4]:
    n = num * 2
    numbers.append(n)

# use a list comprehension
numbers = [num * 2 for num in [1, 2, 3, 4]]