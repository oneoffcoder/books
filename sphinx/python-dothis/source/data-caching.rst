Caching data and results
------------------------

.. highlight:: python
   :linenothreshold: 1

The key here is to use the lru_cache decorator to cache results of functions that are idempotent, especially if they are expensive to call. Note how calls to add takes about 700 milliseconds? However, using the lru_cache decorator, subsequent calls are on the order of microseconds.

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
