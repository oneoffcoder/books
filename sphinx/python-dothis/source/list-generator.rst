Use list comprehensions
-----------------------

.. highlight:: python
   :linenothreshold: 1

Avoid looping over elements just to store derived results. Use a list comprehension or generator expression instead. A list comprehension eagerly evaluates and returns a list, while a generator expression evaluates lazily.

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
