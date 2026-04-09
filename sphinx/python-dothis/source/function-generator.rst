Generator functions
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid materializing large collections when you only need to iterate over them. Use ``yield`` to generate values on demand. Generator functions are often more memory-efficient.

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
