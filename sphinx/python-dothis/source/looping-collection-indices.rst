Looping over a collection with indices
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

The key here is to use enumerate which will return the index with the element.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    for i in range(len(names)):
        print(i, names[i])

Do this
^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    
    for i, name in enumerate(names):
        print(i, name)
