# throws KeyError

students = {'John': 18, 'Jack': 19}

print(students['Joe'])

# try/catch KeyError

students = {'John': 18, 'Jack': 19}

try:
    print(students['Joe'])
except KeyError:
    print('you tried to access an entry that does not exists')
