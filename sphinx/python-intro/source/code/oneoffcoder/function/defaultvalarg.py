# function with list argument
def concat(names, separator=','):
    return separator.join(names)


first_names = ['John', 'Jack', 'Joe']

s = concat(first_names)
print(s)

s = concat(first_names, separator='|')
print(s)
