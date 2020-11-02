Built-in Functions
==================

There are many functions that are built into Python that you should reuse and try to not re-invent yourself. The ``print()`` function that we have been using from the start is one of those functions. As you progress and study more into Python, you will acquire exposures to ever more utility functions available. 

Here are some useful built-in functions.

Types
-----

The function ``type()`` returns the type of a value or variable.

.. code-block:: python 
    :linenos:

    s = 'test'
    i = 32
    f = 32.2
    b = False

    type_s = type(s)
    type_i = type(i)
    type_f = type(f)
    type_b = type(b)

    print(type_s)
    print(type_i)
    print(type_f)
    print(type_b)

The following functions converts data from one type to another.

* ``str()`` converts something into a string
* ``int()`` converts something to an integer
* ``float()`` converts something to a float

.. code-block:: python 
    :linenos:

    a = str(32)
    b = int('32')
    c = float('32.2')

    print(a)
    print(b)
    print(c)

The function ``isinstance()`` checks to see if a variable/value is an instance of a particular type.

.. code-block:: python
    :linenos:

    a = isinstance('s', str)
    b = isinstance(3, int)
    c = isinstance(3.1415, float)
    d = isinstance(False, bool)

    print(a)
    print(b)
    print(c)
    print(d)

Exercise
^^^^^^^^

Filter out the items in the list below for only integers, and create a new list from the integers.

.. code-block:: python
    :linenos:

    data = [1, 2, 'test', 3, 88, True, False, 32.2, 88.5, 0]

Solution.

.. code-block:: python
    :linenos:

    data = [1, 2, 'test', 3, 88, True, False, 32.2, 88.5, 0]
    numbers = [item for item in data if isinstance(item, int)]
    print(numbers)

Math
----

Use ``sum()`` to add up all the numbers in a collection.

.. code-block:: python 
    :linenos:

    numbers = [23, 3, 5, 8]
    total = sum(numbers)

    print(total)

Use ``abs()`` to get the absolute value of a number.

.. code-block:: python 
    :linenos:

    a = -9
    b = 9

    c = abs(a)
    d = abs(b)

    print(c)
    print(d)

Use ``min()`` and ``max()`` to find the minimum and maximum numbers in a collection, correspondingly.

.. code-block:: python 
    :linenos:

    numbers = [23, 3, 5, -8, 100]

    smallest = min(numbers)
    largest = max(numbers)

    print(smallest)
    print(largest)

Use ``round()`` to round numbers to certain precisions (number of decimal places).

.. code-block:: python 
    :linenos:

    a = 2.675255

    b = round(a, 1)
    c = round(a, 2)
    d = round(a, 3)

    print(b)
    print(c)
    print(d)

Exercise
^^^^^^^^

The following is a list of lists. For each list, compute the average and store the averages into a new list.

.. code-block:: python
    :linenos:

    data = [
        [10, 23, 88, 32, 343, 88, 77],
        [22, 20, 18, 23, 45, 77, 88],
        [55, 77, 32, 38, 67, 21, 33]
    ]

Solution.

.. code-block:: python
    :linenos:

    data = [
        [10, 23, 88, 32, 343, 88, 77],
        [22, 20, 18, 23, 45, 77, 88],
        [55, 77, 32, 38, 67, 21, 33]
    ]

    averages = [sum(arr) / len(arr) for arr in data]
    print(averages)

Collections
-----------

The following functions create different collections.

* ``list()`` creates an empty list or converts a collection into a list
* ``set()`` creates an empty set or converts a collection into a set
* ``tuple()`` creates an empty tuple or converts a collection into a tuple
* ``dict()`` creates an empty dictionary

.. code-block:: python 
    :linenos:

    a = set([1, 2, 3, 4, 5, 1, 3])
    b = tuple(a)
    c = list(b)

    print(a)
    print(b)
    print(c)

The function ``all()`` will return ``True`` if all the elements in a collection are not null e.g. ``None``. The function ``any()`` will return ``True`` if at least one lement in a collection is not null e.g. ``None``.

.. code-block:: python
    :linenos:

    numbers = [1, None, 2]

    print(all(numbers)) # False
    print(any(numbers)) # True

The function ``len()`` will return the number of elements in a collection.

.. code-block:: python
    :linenos:

    numbers = [1, None, 2]
    total = len(numbers)
    print(total)

The function ``sorted()`` sorts a collection in ascending order. The function ``reversed()`` reverse sorts a collection (descending order). Note that ``reversed()`` returns an iterator and not a collection, and so we convert that iterator to a list with ``list()``.

.. code-block:: python
    :linenos:

    numbers = [32, 33, 2, 88, 31, 3]

    print(sorted(numbers))
    print(list(reversed(numbers)))

Exercise
^^^^^^^^

The following is a list of lists. For each sub-list, sort it into a new list. Your resulting list should be a list of sorted lists.

.. code-block:: python
    :linenos:

    data = [
        [10, 23, 88, 32, 343, 88, 77],
        [22, 20, 18, 23, 45, 77, 88],
        [55, 77, 32, 38, 67, 21, 33]
    ]

Solution.

.. code-block:: python
    :linenos:

    data = [
        [10, 23, 88, 32, 343, 88, 77],
        [22, 20, 18, 23, 45, 77, 88],
        [55, 77, 32, 38, 67, 21, 33]
    ]

    sorted_data = [sorted(arr) for arr in data]
    print(sorted_data)