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

Range
-----

The ``range()`` function generates a range of values. To generate a range of numbers from [0, 9], we would do the following.

.. code-block:: python
   :linenos:

   numbers = list(range(10))
   print(numbers)

Note that ``range()`` does not create the numbers in the range until we start asking for the elements. ``range()`` is said to be a ``generator function``. To get the actual numbers out, we have to convert the output of ``range()`` to a list.

We can specify the range of integers to output by supplying start and stop (exclusive) integers.

.. code-block:: python
   :linenos:

   numbers = list(range(10, 21))
   print(numbers)

We can also specify what number to increment the current number by to step over numbers.

.. code-block:: python
   :linenos:

   numbers = list(range(10, 21, 2))
   print(numbers)

Exercise
^^^^^^^^

Generate a list of numbers from [0, 10] with only odd numbers.

Solution.

.. code-block:: python
   :linenos:

   numbers = [num for num in range(11) if num % 2 != 0]
   print(numbers)

Random
------

Functions are also stored in built-in Python ``libraries`` (or ``modules``). A library is just a collection of code that logically and/or conceptually belong together. To use these functions, we must import the function from the library. One built-in Python library is the ``random`` library, which deals with generating random numbers. Let's see how we can import the ``randint()`` function. 

.. code-block:: python
   :linenos:

   from random import randint

The syntax to import a function from a library is :code:`from <library> import <function>`. After we import a function from a library, then we can use the function. The ``randint()`` function generates random number between two numbers (inclusive on both ends). 

.. code-block:: python
   :linenos:

   from random import randint

   # generate 3 random numbers in the range [0, 9]
   a = randint(0, 9)
   b = randint(0, 9)
   c = randint(0, 9)

   print(a)
   print(b)
   print(c)

The ``choice()`` function selects an element from a collection at random (all elements have an equal chance of being selected).

.. code-block:: python
   :linenos:

   from random import choice

   numbers = [1, 2, 3, 4, 5, 6]

   a = choice(numbers)
   b = choice(numbers)
   c = choice(numbers)

   print(a)
   print(b)
   print(c)

The ``random()`` function generates a real number in the range [0, 1.0). 

.. code-block:: python
   :linenos:

   from random import random

   a = random()
   b = random()
   c = random()

   print(a)
   print(b)
   print(c)

Exercise
^^^^^^^^

Generate 10 random numbers in the range [0, 9].

Solution.

.. code-block:: python
   :linenos:

   from random import randint

   numbers = [randint(0, 9) for _ in range(10)]

Exercise
^^^^^^^^

Generate 10 random numbers in the range [0, 9] only if the index associated with the random number is even.

Solution.

.. code-block:: python
   :linenos:

   from random import randint

   numbers = [randint(0, 9) for i, _ in enumerate(range(10)) if i % 2 == 0]
   print(numbers)

Exercise
^^^^^^^^

Simulate rolling a die 1000 times. Each time you roll an even number, you win. How many times did you win?

Solution.

.. code-block:: python
   :linenos:

   from random import choice

   die = [1, 2, 3, 4, 5, 6]

   rolls = [choice(die) for _ in range(1000)]
   wins = sum([1 for roll in rolls if roll in {2, 4, 6}])
   print(wins)

Exercise
^^^^^^^^

Simulate rolling two dice 1000. Each time you roll the dice and the sum of the outcomes is 7, you win. How many times did you win?

Solution.

.. code-block:: python
   :linenos:

   from random import choice

   die = [1, 2, 3, 4, 5, 6]

   rolls = [choice(die) + choice(die) for _ in range(1000)]
   wins = sum([1 for roll in rolls if roll == 7])
   print(wins)

itertools
---------

Check out the ``itertools`` module. There are a lot of utility functions you can use to make working with collections easier. The ``cycle()`` function endlessly cycles through a list of elements. Imagine you have a list of people that you need to assign to two teams, Team Red and Team Blue. How can we assign the list of people to these two teams?

.. code-block:: python
    :linenos:

    from itertools import cycle

    colors = ['red', 'green']
    persons = ['Jack', 'John', 'Mary', 'Mandy', 'Moesha', 'Fatimah']

    teams = [(person, color) for person, color in zip(persons, cycle(colors))]
    print(teams)

What if we have a list of lists and wanted to flatten the list? Try the ``chain()`` function.

.. code-block:: python
    :linenos:

    from itertools import chain

    teams = [['Jack', 'Mary'], ['John', 'Moesha'], ['Mandy', 'Fatimah']]
    persons = list(chain(*teams))
    print(persons)

What if we have a list of names and we wanted to group them by the first letter of the name? The ``groupby()`` function will produce a key-value pair for us, where the key is what we want to group by and the value is an iterable.

.. code-block:: python
    :linenos:

    from itertools import groupby

    persons = ['Jack', 'Mary', 'John', 'Moesha', 'Mandy', 'Fatimah']

    by_first_letter = lambda name: name.lower()[0]
    name_map = {k: list(v) for k, v in groupby(persons, key=by_first_letter)}
    print(name_map)

If you have two lists and you want the resulting cross-product of the elements in those lists, try the ``product()`` function.

.. code-block:: python
    :linenos:

    from itertools import product

    products = list(product([1, 2, 3], ['A', 'B', 'C']))
    print(products)

What if you have a list of elements and you want the **n** permutations or combinations of elements from that list? In permutation, order is important, so a pair of number **2 and 3** is not the same as **3 and 2**. In combination, order is not important, so **2 and 3** is the same as **3 and 2**. Remember, a combination lock is a misnomer, and should be a permutation lock. At any rate, try ``permutations()`` and ``combinations()``.

.. code-block:: python
    :linenos:

    from itertools import combinations, permutations

    # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    print(list(permutations([1, 2, 3], 2)))

    # [(1, 2), (1, 3), (2, 3)]
    print(list(combinations([1, 2, 3], 2)))

Exercise
^^^^^^^^

The Mega Millions is based on a player selecting 5 numbers from the range [1, 70] and one number from the range [1, 25]. How many combinations of numbers are possible?

Solution.

.. code-block:: python
    :linenos:

    from itertools import combinations, product

    white_nums = list(range(1, 71, 1))
    gold_nums = list(range(1, 26, 1))

    n = sum([1 for play in product(combinations(white_nums, 5), gold_nums)])
    print(f'{n:,}') # 302,575,350

Exercise
^^^^^^^^

The Power Ball is based on a player selecting 5 numbers from the range [1, 69] and one number from the range [1, 26]. How many combinations of numbers are possible?

Solution.

.. code-block:: python
    :linenos:

    from itertools import combinations, product

    white_nums = list(range(1, 70, 1))
    red_nums = list(range(1, 27, 1))

    n = sum([1 for play in product(combinations(white_nums, 5), red_nums)])
    print(f'{n:,}') # 292,201,338