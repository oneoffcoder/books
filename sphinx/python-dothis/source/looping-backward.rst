Looping backward
----------------

.. highlight:: python
   :linenothreshold: 1

The key here is to avoid the awkward -1 values and nested functions (look at how many parenthesis pairs are involved). Use reverse to make your code more elegant.

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
