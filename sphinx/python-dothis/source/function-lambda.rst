Lambdas
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``lambda`` for short throwaway callables passed inline to another function. If the function deserves a name, prefer ``def``.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    add_one = lambda x: x + 1

    add_one(3)

Do this
^^^^^^^

.. code:: python

    def add_one(x):
        return x + 1

    add_one(3)

.. code:: python

    numbers = ['10', '2', '1']
    numbers = sorted(numbers, key=lambda value: int(value))

    print(numbers)
