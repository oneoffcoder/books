# do not create a set in this way

s = set()
for name in ['Jack', 'John', 'Joe', 'Mary']:
    n = len(name)
    s.add(n)

# create a set in this way
s = {len(name) for name in ['Jack', 'John', 'Joe', 'Mary']}
