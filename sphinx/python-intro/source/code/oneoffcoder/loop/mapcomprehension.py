# do not create a map in this way
names = ['Jack', 'John', 'Joe', 'Mary']

m = {}
for name in names:
    m[name] = len(name)


# create a map in this way
names = ['Jack', 'John', 'Joe', 'Mary']

m = {name: len(name) for name in names}
