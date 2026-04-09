Decorators
==========

Decorators are annotations that modify the behavior of functions. The mental model of a decorator is that it is an outer function wrapped around a target function. The outer function has a chance to intercept the arguments and modify or interact with them, before invoking the target function. Using decorators is sometimes referred to as ``meta-programming`` since we are programming the program. 

.. uml::

   @startuml
   skinparam shadowing false

   actor Caller
   rectangle "decorated function" as Wrapped
   rectangle "decorator wrapper" as Wrapper
   rectangle "original function" as Original

   Caller --> Wrapped
   Wrapped --> Wrapper : intercept call
   Wrapper --> Original : invoke target
   Original --> Wrapper : return value
   Wrapper --> Caller : maybe log, validate,\ntransform, then return
   @enduml

Basic
-----

Below, we have a ``log()`` function that takes another function ``f`` as an argument. Inside ``log()`` is an inner function named ``decorated()``. Notice that ``decorated()`` is annotated with ``@wraps`` and accepts two flexible argument forms: the positional tuple ``*args`` and the keyword dictionary ``**kwargs``. The ``@wraps`` annotation preserves metadata from the original function, such as its name and docstring. Without it, introspection would report the wrapper's metadata instead. The ``decorated()`` function calls the target function and returns its result, and ``log()`` returns ``decorated()``.

After we define the decorator, we can use it to annotate other functions. Below, we annotate ``add_one()`` and ``minus_one()`` with ``@log``.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,4,7,10,13,18

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
    def add_one(a):
        print('add one')
        return a + 1

    @log
    def minus_one(a):
        print('minus one')
        return a - 1

    print(add_one(a=10))
    print(minus_one(a=10))

Exercise
^^^^^^^^

Write a decorator to ensure that the value passed into the function below is always in the range [0, 100]. If the value passed in is not in this range, throw an exception (which exception is appropriate?).

.. code-block:: python
    :linenos:

    def add_one(a):
        return a + 1

Solution.

.. code-block:: python
    :linenos:

    from functools import wraps

    def ensure_legal_range(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            for arg in args:
                if arg < 0 or arg > 100:
                    raise ValueError(f'{arg} is not in [0, 100]')
            
            for k, v in kwargs.items():
                if v < 0 or v > 100:
                    raise ValueError(f'{k}={v} is not in [0, 100]')
            
            output = f(*args, **kwargs)
            return output
        return decorated

    @ensure_legal_range
    def add_one(a):
        return a + 1

    print(add_one(10))
    print(add_one(a=10))

    print(add_one(-10))
    print(add_one(a=-10))

Multiple decorators
-------------------

Here's another example of defining two decorators and using them together. The ``log()`` decorators simply logs the inputs and outputs of a function. The ``positive_inputs()`` decorator modifies the inputs to always be positive. We decorate the ``add_one()`` and ``minus_one()`` functions with ``@log`` and ``@positive_inputs``.

.. code-block:: python
    :linenos:

    from functools import wraps

    def log(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            output = f(*args, **kwargs)
            print(f'name = {f.__name__}, inputs={args}, {kwargs}, output = {output}')
            return output
        return decorated

    def positive_inputs(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            nargs = [abs(a) for a in args]
            nkwargs = {k: abs(v) for k, v in kwargs.items()}

            output = f(*nargs, **nkwargs)

            return output
        return decorated

    @log 
    @positive_inputs
    def add_one(a):
        return a + 1

    @log
    @positive_inputs
    def minus_one(a):
        return a - 1

    print(add_one(a=-10))
    print(add_one(a=10))
    print(minus_one(a=10))
    print(minus_one(a=-10))

Parameterized decorators
------------------------

Your decorator can also be parameterized to change its own behavior. To achieve a parameterized decorator, we wrap the **real** decorator yet inside another wrapper function. 

.. uml::

   @startuml
   skinparam shadowing false

   rectangle "range_check(lower, upper)" as Factory
   rectangle "real_decorator(f)" as Decorator
   rectangle "wrapper(*args, **kwargs)" as Wrapper
   rectangle "target function" as Function

   Factory --> Decorator : returns configured decorator
   Decorator --> Wrapper : returns wrapper
   Wrapper --> Function : calls after checks
   @enduml

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,7,9,23

    from functools import wraps

    def range_check(*a, **k):
        lower = 10 if 'lower' not in k else k['lower']
        upper = 100 if 'upper' not in k else k['upper']

        def real_decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                for arg in args:
                    if arg < lower or arg > upper:
                        raise ValueError(f'{arg} is not in [{lower}, {upper}]')

                for k, v in kwargs.items():
                    if v < lower or v > upper:
                        raise ValueError(f'{k}={v} is not in [{lower}, {upper}]')
                
                retval = f(*args, **kwargs)
                return retval
            return wrapper
        return real_decorator

    @range_check(lower=-10, upper=100)
    def add_one(a):
        return a + 1

    print(add_one(10))
    print(add_one(-10))
    print(add_one(-100))

Exercise
^^^^^^^^
Write a decorator to time the following functions. Make sure to parameterize the time duration in seconds ``s`` or milliseconds ``ms``. The use of the ``time`` module will help in capturing duration.

.. code-block:: python
    :linenos:

    # capture the time duration in seconds
    def get_numbers_s(n=50000000):
        return [i for i in range(n)]

    # capture the time duration in milliseconds
    def get_numbers_ms(n=50000000):
        return [i for i in range(n)]

    # capture the time duration in seconds
    def get_numbers_slow(n=50000000):
        numbers = []
        for i in range(n):
            numbers.append(i)
        return numbers

Solution.

.. code-block:: python
    :linenos:

    from functools import wraps
    import time

    def benchmark(*a, **k):
        units = 's' if 'unit' not in k else k['unit']
        units = units if units in {'s', 'ms'} else 's'

        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                start = time.time()
                retval = f(*args, **kwargs)
                stop = time.time()
                diff = stop - start
                if units == 'ms':
                    diff = diff * 1000
                print(f'diff = {diff}')
                return retval
            return wrapper
        return decorator


    @benchmark(unit='s')
    def get_numbers_s(n=50000000):
        return [i for i in range(n)]

    @benchmark(unit='ms')
    def get_numbers_ms(n=50000000):
        return [i for i in range(n)]

    @benchmark(unit='s')
    def get_numbers_slow(n=50000000):
        numbers = []
        for i in range(n):
            numbers.append(i)
        return numbers

    get_numbers_s()
    get_numbers_ms()
    get_numbers_slow()

Built-in decorators
-------------------

There are many built-in decorators. Use ``@lru_cache`` to cache outputs based on inputs to a function. The second and third calls to ``get_data()`` below will be super fast.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,4

    from functools import lru_cache
    import time

    @lru_cache
    def get_data(n=50000000):
        return [i for i in range(n)]

    # first call
    start = time.time()
    get_data()
    diff = time.time() - start
    print(f'{diff:.10f} seconds')

    # second call
    start = time.time()
    get_data()
    diff = time.time() - start
    print(f'{diff:.10f} seconds')

    # third call
    start = time.time()
    get_data()
    diff = time.time() - start
    print(f'{diff:.10f} seconds')

The ``@property`` decorator will enable you to treat a function as if it was a property of an object. The ``@staticmethod`` decorator will turn a method into a static one (a static method is associated with a class not an instance of that class; you do not have to instantiate an instance of the class to use a static method).

.. code-block:: python
    :linenos:
    :emphasize-lines: 7,11,15,19,26-27

    import math

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @property
        def area(self):
            return Circle.__get_area(self.radius)

        @property
        def circumference(self):
            return Circle.__get_circumference(self.radius)

        @staticmethod
        def __get_area(r):
            return math.pi * r ** 2
        
        @staticmethod
        def __get_circumference(r):
            return 2.0 * math.pi * r

    circle = Circle(10)

    print(circle.radius)
    print(circle.area)
    print(circle.circumference)

A `list of decorators <https://github.com/lord63/awesome-python-decorator>`_ has been curated.
