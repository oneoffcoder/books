Flattening data
---------------

.. highlight:: python
   :linenothreshold: 1

Here, we want to flatten a list of lists into one sequence. Prefer the approach that best balances readability and performance for your case.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    data = [list(range(10000000)) for _ in range(10)]

    x = []
    for arr in data:
        for val in arr:
            x.append(val)

.. code:: python

    data = [list(range(10000000)) for _ in range(10)]

    x = []
    for arr in data:
        x.extend(arr)

Do this
^^^^^^^

.. code:: python

    data = [list(range(10000000)) for _ in range(10)]

    x = [val for arr in data for val in arr]

.. code:: python

    import itertools

    data = [list(range(10000000)) for _ in range(10)]

    x = itertools.chain.from_iterable(data)
