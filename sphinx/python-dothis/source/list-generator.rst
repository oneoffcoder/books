Use list comprehensions
-----------------------

.. highlight:: python
   :linenothreshold: 1

The key here is to avoid looping over elements and storing results. Instead, use a for or generator comprehension. Note that the for (note the brackets) comprehension eagerly evaluates the expressions and returns a list, but the generator (note the parentheses) lazily evaluates the expressions.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    results = []

    for i in range(10):
        s = i ** 2
        results.append(s)

    total = sum(results)

Do this
^^^^^^^

.. code:: python

    total = sum([i ** 2 for i in range(10)])

.. code:: python

    total = sum((i ** 2 for i in range(10)))
