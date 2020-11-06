Functional Programming
======================

Functional programming is just a style of programming using functions to transform data. Theoretically, functional programming has deep roots in math and is very technical. However, the easiest way to understand functional programming is to understand three main functions.

* ``map()`` transforms an item to a new one
* ``filter()`` removes an item
* ``reduce()`` collapses a collection of values into a single one

.. note:: 
    Functional programming is said to be describing ``what`` we are doing. The opposite, ``imperative programming``, is said to be describing ``how`` we are doing something. Functional programming may be viewed as ``declarative`` programming, and imperative programming may be viewed as ``procedural`` programming. 

map
---

Here's an example of using ``map()`` to transform data. Note that ``map()`` returns an iterator and so we have to convert it to a list to observe the outputs.

.. code-block:: python
    :linenos:

    numbers = [1, 2, 3, 4, 5]

    output = map(lambda x: x + 1, numbers)
    output = list(output)
    
    print(output)

Exercise
^^^^^^^^

Map the following list of integers into a new one where each element is a boolean indicating if the corresponding original element was an even number.

.. code-block:: python
    :linenos:

    numbers = [1, 2, 3, 4, 5]

Solution.

.. code-block:: python
    :linenos:

    numbers = [1, 2, 3, 4, 5]

    output = map(lambda x: x % 2 == 0, numbers)
    output = list(output)
    
    print(output)

filter
------

Here's an example of using ``filter()`` to remove items from a collection. 

.. code-block:: python
    :linenos:

    numbers = [1, 2, 3, 4, 5]

    output = filter(lambda x: x % 2 == 0, numbers)
    output = list(output)
    
    print(output)


Exercise
^^^^^^^^

Create a new list of names from the one below with names starting with 'J'.

.. code-block:: python
    :linenos:

    names = ['Jack', 'John', 'Mary', 'Jane', 'Nancy']

Solution.

.. code-block:: python
    :linenos:

    names = ['Jack', 'John', 'Mary', 'Jane', 'Nancy']

    j_names = filter(lambda name: name.lower().startswith('j'), names)
    j_names = list(j_names)

    print(j_names)

reduce
------

The ``reduce()`` function is available through the ``functools`` module. Reduce takes the elements in a collection and collapses them into one final value. Below, we use ``reduce()`` to sum up all the integers in a list.

.. code-block:: python
    :linenos:

    from functools import reduce

    numbers = [1, 2, 3, 4, 5]

    output = reduce(lambda x, y: x + y, numbers)

    print(output)

Exercise
^^^^^^^^
Reduce the following list of numbers to the product of all the numbers.

.. code-block:: python
    :linenos:

    numbers = [1, 2, 3, 4, 5]

Solution.

.. code-block:: python
    :linenos:

    from functools import reduce

    numbers = [1, 2, 3, 4, 5]

    output = reduce(lambda x, y: x * y, numbers)

    print(output)

Exercise
^^^^^^^^

Get the sum of the ages for the males and females in the data below.

.. code-block:: python
    :linenos:

    data = [
        ('John', 32, 'Male'), ('Jack', 28, 'Male'), 
        ('Jeremy', 33, 'Male'), ('Mary', 28, 'Female'), 
        ('Nancy', 27, 'Female'), ('Katherine', 33, 'Female')
    ]

Solution.

.. code-block:: python
    :linenos:

    from functools import reduce

    data = [
        ('John', 32, 'Male'), ('Jack', 28, 'Male'), 
        ('Jeremy', 33, 'Male'), ('Mary', 28, 'Female'), 
        ('Nancy', 27, 'Female'), ('Katherine', 33, 'Female')
    ]

    items = filter(lambda tup: tup[2] == 'Male', data)
    items = map(lambda: tup[1], items)
    male_total_age = reduce(lambda x, y: x + y, items)

    items = filter(lambda tup: tup[2] == 'Female', data)
    items = map(lambda: tup[1], items)
    female_total_age = reduce(lambda x, y: x + y, items)

    print(male_total_age)
    print(female_total_age)