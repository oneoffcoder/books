Filtering a list
----------------

.. highlight:: python
   :linenothreshold: 1

Use a for comprehension to filter out values, not a for loop.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    nums = []
    for i in range(100):
        if i % 2 == 0:
            nums.append(i)

Do this
^^^^^^^

.. code:: python

    nums = [i for i in range(100) if i % 2 == 0]
