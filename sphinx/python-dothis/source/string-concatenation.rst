String concatenation
--------------------

.. highlight:: python
   :linenothreshold: 1

Avoid writing extra control flow just to concatenate strings. In the first approach, you need extra logic to place commas correctly. In the second, ``join`` expresses the intent directly.

``str.join`` also makes it clear that the separator belongs to the whole operation, not to any one element. That reduces fiddly edge-case logic around leading or trailing delimiters.

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
