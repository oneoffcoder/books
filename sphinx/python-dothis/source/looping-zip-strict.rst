Use zip(strict=True) when equal lengths are required
----------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``zip(strict=True)`` when a length mismatch is a bug. It fails fast instead of silently dropping extra items.

That small keyword turns an implicit assumption into executable validation. It is valuable whenever silently truncating data would hide a bug rather than gracefully handling uneven inputs.

.. note::

   Python 3.10+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['alice', 'bob', 'carol']
    scores = [90, 85]

    for name, score in zip(names, scores):
        print(name, score)

Do this
^^^^^^^

.. code:: python

    names = ['alice', 'bob', 'carol']
    scores = [90, 85]

    for name, score in zip(names, scores, strict=True):
        print(name, score)
