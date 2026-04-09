Using a dictionary to store counts
----------------------------------

.. highlight:: python
   :linenothreshold: 1

Like ``defaultdict``, ``Counter`` initializes missing counts to zero. That lets you avoid checking whether a key already exists.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    d = {}
    for name in names:
        key = len(name)
        if key not in d:
            d[key] = 0
        d[key] = d[key] + 1

Do this
^^^^^^^

.. code:: python

    from collections import defaultdict

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    d = defaultdict(int)

    for name in names:
        key = len(name)
        d[key] = d[key] + 1

.. code:: python

    from collections import Counter

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    d = Counter()
    for name in names:
        key = len(name)
        d[key] = d[key] + 1

.. code:: python

    from collections import Counter

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']

    d = Counter(map(lambda s: len(s), names))
