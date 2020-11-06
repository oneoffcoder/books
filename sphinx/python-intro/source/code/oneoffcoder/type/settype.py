# empty set
s = set()

# declare with curly braces
s = {1, 1, 2, 3}

# create a set from a list
s = set([1, 1, 2, 3])

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

# uinion: {0, 1, 2, 3, 4, 6}
union = a | b

# intersection: {2, 4}
intersection = a & b

# difference: {0, 4, 6}
diff = a - b

# symmetric difference: {0, 1, 3, 6}
symmetric_diff = a ^ b
