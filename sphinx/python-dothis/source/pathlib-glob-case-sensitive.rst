Use explicit case sensitivity in pathlib globbing
-------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When matching paths across platforms, use explicit case sensitivity when that behavior matters.

Path matching behavior can otherwise vary quietly across operating systems, which makes cross-platform bugs easy to miss. Being explicit documents the intended matching rule instead of leaving it to platform defaults.

.. note::

   Python 3.12+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    matches = list(Path('.').glob('*.TXT'))

Do this
^^^^^^^

.. code:: python

    from pathlib import Path

    matches = list(Path('.').glob('*.TXT', case_sensitive=True))
