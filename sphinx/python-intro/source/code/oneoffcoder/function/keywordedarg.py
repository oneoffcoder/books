# keyworded, variable-length argument
def do_print(**kwargs):
    for key, val in kwargs.items():
        print(key, val)


def do_special_print(symbol, **kwargs):
    for key, val in kwargs.items():
        print(symbol, key, val)


# use a dictionary
# use ** unpacking operating
data = {
    'name': 'John Doe',
    'age': 18
}

do_print(**data)

# inline keyworded argument
do_print(name='John Doe', age=18)

do_special_print('*', **data)

do_special_print('*', name='John Doe', age='18')
