String reversal
---------------

.. highlight:: python
   :linenothreshold: 1

Use ``string indexing`` to reverse a string, not a for loop or for-comprehension.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    name = 'one-off coder'
    name = ''.join([name[i] for i in range(len(name) - 1, -1, -1)])

Do this
^^^^^^^

Use slicing to reverse a string. The first number is the start index, the second number is the stop index and the last number is the skip. Since we are starting and stopping at the start and stop index, those values are omitted. The skip is -1 which forces the skip to go backwards.

.. code:: python

    name = 'one-off coder'
    name = name[::-1]

We can also print just even-indexed characters backwards.

.. code:: python

    name = 'one-off coder'
    name = name[0::2][::-1]

We can also print just odd-indexed characters backwards.

.. code:: python

    name = 'one-off coder'
    name = name[1::2][::-1]