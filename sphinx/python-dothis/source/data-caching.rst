Caching data and results
------------------------

.. highlight:: python
   :linenothreshold: 1

Use the ``lru_cache`` decorator to cache the results of pure or repeatable functions, especially when they are expensive to call. The first call still does the work, but repeated calls with the same arguments can be much faster.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    def add(n):
        return sum([i for i in range(n)])

    add(10000000)

Do this
^^^^^^^

.. code:: python

    from functools import lru_cache

    @lru_cache(maxsize=32)
    def add(n):
        return sum([i for i in range(n)])

    add(10000000)
