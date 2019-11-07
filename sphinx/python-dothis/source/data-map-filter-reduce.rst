Transforming data with map, filter, reduce
------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Favor `map`, `filter`, and `reduce` to transform data. Your code will be more concise and better understood, as well as faster.

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

    from functools import reduce

    data = [i for i in range(10000000)]

    x = map(lambda val: val * 2, data)
    y = filter(lambda val: val % 2 == 0, x)
    z = reduce(lambda val1, val2: val1 + val2, y)