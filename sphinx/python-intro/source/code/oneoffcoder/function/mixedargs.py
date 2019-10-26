# mixed arguments: standard + *args + **kwargs
def do_print(a, b, *args, **kwargs):
    print(f'standard args: {a}, {b}')

    for arg in args:
        print(f'*args: {arg}')

    for key, val in kwargs.items():
        print(f'**kwargs: {key} => {val}')


do_print(1, 2, *[3, 4, 5], **{'name': 'John Doe', 'age': 18})
