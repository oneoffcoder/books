String concatenation
--------------------

.. highlight:: python
   :linenothreshold: 1

Avoid writing extra control flow just to concatenate strings. In the first approach, you need extra logic to place commas correctly. In the second, ``join`` expresses the intent directly.

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
