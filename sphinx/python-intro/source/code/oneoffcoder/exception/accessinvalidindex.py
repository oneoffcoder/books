# throws IndexError
names = ['John', 'Jack', 'Joe']
print(names[4])

# try/catch IndexError
names = ['John', 'Jack', 'Joe']

try:
    print(names[4])
except IndexError:
    print('no such index')
