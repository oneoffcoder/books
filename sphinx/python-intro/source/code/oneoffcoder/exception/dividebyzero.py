# throws ZeroDivisionError
a = 20
b = 0
c = a / b

# try/catch ZeroDivisionError
try:
    a = 20
    b = 0
    c = a / b
except ZeroDivisionError:
    print('your denominator is zero')
