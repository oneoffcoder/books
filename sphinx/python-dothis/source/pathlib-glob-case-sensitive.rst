Use explicit case sensitivity in pathlib globbing
-------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When matching paths across platforms, use explicit case sensitivity when that behavior matters.

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
