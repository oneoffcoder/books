Transforming data with map, filter, reduce
------------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python, comprehensions and generator expressions are usually easier to read than chaining ``map``, ``filter``, and ``reduce``. Reach for the functional tools when they are clearly the best fit, not by default.

Most Python readers parse comprehension syntax faster because the transformation and filter live next to the resulting collection shape. That reduces the cognitive overhead of jumping between multiple function calls and anonymous lambdas.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    data = [i for i in range(10000000)]

    x = []
    for val in data:
        x.append(val * 2)
        
    y = []
    for val in x:
        if val % 2 == 0:
            y.append(val)
            
    z = 0
    for val in y:
        z = z + val

Do this
^^^^^^^

.. code:: python

    data = [i for i in range(10000000)]

    z = sum(val * 2 for val in data if (val * 2) % 2 == 0)
