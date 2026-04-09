Looping over two collections
----------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid accessing elements by indices and manually managing which list is shorter. Use ``zip`` to iterate over both collections, stopping at the end of the shorter one.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink']

    n = min(len(names), len(colors))
    for i in range(n):
        print(names[i], colors[i])

Do this
^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink']

    for name, color in zip(names, colors):
        print(name, color)
