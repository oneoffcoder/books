Looping over a collection with indices
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``enumerate`` when you need both the index and the element.

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
