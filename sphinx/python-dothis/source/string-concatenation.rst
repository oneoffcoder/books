String concatenation
--------------------

.. highlight:: python
   :linenothreshold: 1

The key here is to avoid writing too much code just to concatenate a string. In the discouraged approach, note how we have to add logic to append a comma `,`? In the encourage approach, the for loop is gone and there is no more need for when to add a comma.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    s = ''
    for i, name in enumerate(names):
        s += name
        if i < len(names) - 1:
            s += ', '

Do this
^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    
    s = ', '.join(names)
