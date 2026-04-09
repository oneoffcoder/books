Looping over a collection
-------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid using an index just to access elements in a collection.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    for i in range(len(names)):
        print(names[i])

Do this
^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    
    for name in names:
        print(name)
