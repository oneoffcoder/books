Prefer pathlib over os.path
---------------------------

.. highlight:: python
   :linenothreshold: 1

Prefer ``pathlib`` when working with filesystem paths. It composes operations more cleanly than string-based ``os.path`` code.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import os

    path = os.path.join('data', 'reports', 'summary.txt')
    if os.path.exists(path):
        print(os.path.basename(path))

Do this
^^^^^^^

.. code:: python

    from pathlib import Path

    path = Path('data') / 'reports' / 'summary.txt'
    if path.exists():
        print(path.name)
