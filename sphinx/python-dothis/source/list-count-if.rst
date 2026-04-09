Count matching items without a temporary list
---------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When you only need a count, use a generator expression instead of building a temporary list first.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    nums = list(range(100))
    count = len([n for n in nums if n % 2 == 0])

Do this
^^^^^^^

.. code:: python

    nums = list(range(100))
    count = sum(1 for n in nums if n % 2 == 0)
