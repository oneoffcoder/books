Product of lists
----------------

.. highlight:: python
   :linenothreshold: 1

Here's how to get the product of elements in multiple lists.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    a = ['cat', 'dog', 'frog']
    b = ['red', 'green', 'blue']
    c = ['big', 'small']

    product_list = []
    for animal in a:
        for color in b:
            for size in c:
                tup = animal, color, size
                product_list.append(tup)

Do this
^^^^^^^

.. code:: python

    from itertools import product

    a = ['cat', 'dog', 'frog']
    b = ['red', 'green', 'blue']
    c = ['big', 'small']

    product_list = product(a, b, c)

.. code:: python

    from itertools import product

    a = ['cat', 'dog', 'frog']
    b = ['red', 'green', 'blue']
    c = ['big', 'small']

    list_of_list = [a, b, c]
    product_list = product(*list_of_list)
