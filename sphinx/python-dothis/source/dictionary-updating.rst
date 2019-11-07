Updating dictionaries
---------------------

.. highlight:: python
   :linenothreshold: 1

The key is to avoid copying and updating dictionaries just to override values. ChainMap will take care of this concern. Notice how the discouraged approached copies d1 then updates with d2, while ChainMap starts with d2 followed by d1. This part of the ChainMap is awkward.

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