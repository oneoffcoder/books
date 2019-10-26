# concatenating strings
s = 'Hello, ' + 'world!'

# interpolating values into a string using place holder
age = 32
s = 'I am {} years old'.format(age)

# interpolating values into a string using a named place holder
s = 'I am {age} years old. She is also {age} years old.'.format(age=age)

# using f-string
s = f'I am {age} years old. She is also {age} years old.'

# formatting floats in a string
pi = 3.1415
s = f'the value of pi is {pi:.2f}'

