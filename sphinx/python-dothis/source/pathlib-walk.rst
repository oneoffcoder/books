Use Path.walk in pathlib code
-----------------------------

.. highlight:: python
   :linenothreshold: 1

If you are already using ``pathlib``, prefer ``Path.walk()`` over dropping back to ``os.walk()``. This is available in Python 3.12 and later.

Staying inside ``pathlib`` avoids mixing path styles in the same block of code and makes later refactors cleaner. The main win is consistency: once the root is a ``Path``, the traversal can remain ``Path``-oriented end to end.

.. note::

   Python 3.12+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import os
    from pathlib import Path

    root = Path('src')
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.py'):
                print(Path(dirpath) / filename)

Do this
^^^^^^^

.. code:: python

    from pathlib import Path

    root = Path('src')
    for dirpath, dirnames, filenames in root.walk():
        for filename in filenames:
            if filename.endswith('.py'):
                print(dirpath / filename)
