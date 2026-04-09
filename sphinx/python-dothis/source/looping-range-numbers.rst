Looping over a range of numbers
-------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid creating a list just to loop over a sequence of numbers. Use ``range`` instead because it is more concise and more memory-efficient.

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
