Decorators
==========

.. code:: python

    from functools import wraps

    def log(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            print(f'init: {args}, {kwargs}')
            output = f(*args, **kwargs)
            print(f'output = {output}')
            print('finished')
            return output
        return decorated

    @log
    def do_something(a):
        print('doing something')
        return 1

    print(do_something(a=1))