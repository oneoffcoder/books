Default dictionary values: defaultdict
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid checking whether a key exists before initializing its value. ``defaultdict`` creates the default value for a missing key on first access. ``itertools.groupby`` can also help in some grouping cases.

That removes repeated existence checks and keeps the happy path focused on the update itself. It is most useful when the default for a missing key is part of the data shape, such as an empty list, set, or counter value.

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
