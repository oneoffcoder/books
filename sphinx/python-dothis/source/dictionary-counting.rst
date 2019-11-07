Using a dictionary to store counts
----------------------------------

.. highlight:: python
   :linenothreshold: 1

Like defaultdict, Counter initialize values associated with keys to 0. Note how we get rid of checking to see if a key entry exists?

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