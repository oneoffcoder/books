Generator functions
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid generating large number of values or objects as they may take up memory. Use yield inside a function to generate values or objects as needed. Functions generating collections using yield are more space efficient and faster.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    def generate_sequential_numbers(n):
        nums = []
        for i in range(n):
            nums.append(i)
        return nums

    sum(generate_sequential_numbers(10000000))

Do this
^^^^^^^

.. code:: python

    def generate_sequential_numbers(n):
        for i in range(n):
            yield i

    sum(generate_sequential_numbers(10000000))

.. code:: python

    generate_sequential_numbers = lambda n: (i for i in range(n))

    sum(generate_sequential_numbers(10000000))