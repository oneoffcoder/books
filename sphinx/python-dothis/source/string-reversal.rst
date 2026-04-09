String reversal
---------------

.. highlight:: python
   :linenothreshold: 1

Use slicing to reverse a string instead of building it character by character.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    name = 'one-off coder'
    name = ''.join([name[i] for i in range(len(name) - 1, -1, -1)])

Do this
^^^^^^^

Use slicing to reverse a string. The first number is the start index, the second is the stop index, and the last is the step. Here, the start and stop values are omitted, and the step is ``-1``, which moves backward through the string.

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
