def get_names():
    return 'John', 'Joe', 'Jack'


# bad way of acquiring tuple elements
t = get_names()
name1 = t[0]
name2 = t[1]
name3 = t[2]

# better way of acquiring tuple elements
name1, name2, name3 = get_names()
