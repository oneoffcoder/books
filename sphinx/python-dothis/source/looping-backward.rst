Looping backward
----------------

.. highlight:: python
   :linenothreshold: 1

Avoid awkward ``-1`` bounds when iterating backward. Use ``reversed`` to make the code clearer.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    for i in range(len(names) - 1, -1, -1):
        print(names[i])

Do this
^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    
    for name in reversed(names):
        print(name)
