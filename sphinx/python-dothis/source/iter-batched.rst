Use itertools.batched for chunking
----------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``itertools.batched()`` to split an iterable into fixed-size chunks instead of writing the indexing logic yourself.

Using the standard tool makes the chunking rule obvious immediately and avoids off-by-one mistakes in hand-written slice loops. It also keeps the code focused on what a batch means instead of on index arithmetic.

.. note::

   Python 3.12+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    items = list(range(10))
    batches = []
    for i in range(0, len(items), 3):
        batches.append(items[i:i + 3])

Do this
^^^^^^^

.. code:: python

    from itertools import batched

    items = list(range(10))
    batches = list(batched(items, 3))
