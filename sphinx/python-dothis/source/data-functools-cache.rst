Use functools.cache for unbounded memoization
---------------------------------------------

.. highlight:: python
   :linenothreshold: 1

If you want an unbounded cache, prefer ``functools.cache`` over ``lru_cache(maxsize=None)``.

The name matches the intent directly: you want memoization, not an LRU policy with an unlimited size disguised through a special argument. That small naming improvement makes maintenance easier because readers do not have to decode the configuration to understand the behavior.

.. note::

   Python 3.9+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

Do this
^^^^^^^

.. code:: python

    from functools import cache

    @cache
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
