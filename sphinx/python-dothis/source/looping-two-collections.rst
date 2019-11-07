Looping over two collections
----------------------------

.. highlight:: python
   :linenothreshold: 1

The key is to avoid accessing elements by indicies and also managing the concern of which list is smaller than which. Use `zip` to iterate over the two lists; the iteration will only go until the end of the shorter list.

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
