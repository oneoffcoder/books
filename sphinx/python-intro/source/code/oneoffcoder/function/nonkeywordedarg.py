# non-keyworded, variable-length argument
def do_print(*args):
    for arg in args:
        print(arg)


def do_special_print(symbol, *args):
    for arg in args:
        print(symbol, arg)


names = ['John', 'Jack', 'Joe']

# use *, the unpacking operator
# * returns an iterable that is a tuple
do_print(*names)

do_special_print('*', *names)
