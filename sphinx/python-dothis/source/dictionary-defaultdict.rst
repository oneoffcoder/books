Default dictionary values: defaultdict
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

The key is to avoid checking to see if a key exists in the dictionary, and if not, then initialize its associated value. The use of defaultdict will initialize a value associated with a key that does not yet exists upon first access. Check out `itertools` too.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    d = {}
    for name in names:
        key = len(name)
        if key not in d:
            d[key] = []
        d[key].append(name)

Do this
^^^^^^^

.. code:: python

    from collections import defaultdict
    
    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    d = defaultdict(list)
    for name in names:
        key = len(name)
        d[key].append(name)

.. code:: python

    import itertools
    
    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    key = lambda s: len(s)
    d = {k: list(g) for k, g in itertools.groupby(sorted(names, key=key), key)}
