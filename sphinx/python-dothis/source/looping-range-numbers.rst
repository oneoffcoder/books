Looping over a range of numbers
-------------------------------

.. highlight:: python
   :linenothreshold: 1

The key is to avoid creating an array. Use the range function instead as it will make your code more concise and is more memory efficient.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    for i in [0, 1, 2, 3, 4, 5]:
        print(i ** 2)

Do this
^^^^^^^

.. code:: python

    for i in range(6):
        print(i ** 2)
