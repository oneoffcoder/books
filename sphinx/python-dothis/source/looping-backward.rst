Looping backward
----------------

.. highlight:: python
   :linenothreshold: 1

Avoid awkward ``-1`` bounds when iterating backward. Use ``reversed`` to make the code clearer.

``reversed`` states the direction change without exposing the indexing mechanics needed to accomplish it. That makes the loop easier to inspect and less error-prone when the sequence bounds change.

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
