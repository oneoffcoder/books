# declare with set
s = set([1, 1, 2, 3])

# declare with curly braces
s = {1, 1, 2, 3}

# add item
s.add(4)

# remove item
s.remove(4)

# check if element is in set
4 in s
1 in s

# set operations

a = {0, 2, 4, 6}
b = {1, 2, 3, 4}

# uinion
union = a | b

# intersection
intersection = a & b

# difference
diff = a - b

# symmetric difference
symmetric_diff = a ^ b
