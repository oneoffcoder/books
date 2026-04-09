Updating dictionaries
---------------------

.. highlight:: python
   :linenothreshold: 1

Avoid copying and updating dictionaries just to override values. ``ChainMap`` can layer mappings without creating a merged copy, though the lookup order can be less obvious than a plain dictionary.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    d1 = {'color': 'red', 'user': 'jdoe'}
    d2 = {'color': 'blue', 'first_name': 'john', 'last_name': 'doe'}

    d = d1.copy()
    d.update(d2)

Do this
^^^^^^^

.. code:: python

    from collections import ChainMap

    d1 = {'color': 'red', 'user': 'jdoe'}
    d2 = {'color': 'blue', 'first_name': 'john', 'last_name': 'doe'}

    d = ChainMap(d2, d1)
