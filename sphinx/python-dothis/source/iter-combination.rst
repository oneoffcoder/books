Combinations of a list
----------------------

.. highlight:: python
   :linenothreshold: 1

Create combinations from a list of items.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    symbols = ['A', 'B', 'C', 'D']

    combs = []

    for i, symbol_i in enumerate(symbols):
        for j, symbol_j in enumerate(symbols):
            if i < j:
                tup = symbol_i, symbol_j
                combs.append(tup)

Do this
^^^^^^^

.. code:: python

    from itertools import combinations

    symbols = ['A', 'B', 'C', 'D']

    combs = list(combinations(symbols, 2))
