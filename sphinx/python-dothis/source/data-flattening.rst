Flattening data
---------------

.. highlight:: python
   :linenothreshold: 1

Here, we need to flatten an array of arrays into one array. Notice that the second discouraged approach is actually the fastest (faster than the encouraged approaches)? The setup with the `x` array and use of a for loop spans 3 lines. This example appears controversial with trading off idiomatic Python for speed.

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