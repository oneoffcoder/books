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

.. code:: python

    name = 'one-off coder'
    name = name[::-1]
