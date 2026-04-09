Use tomllib for reading TOML
----------------------------

.. highlight:: python
   :linenothreshold: 1

Use the standard-library ``tomllib`` module for read-only TOML parsing.

.. note::

   Python 3.11+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import toml

    with open('pyproject.toml', 'rb') as f:
        data = toml.load(f)

Do this
^^^^^^^

.. code:: python

    import tomllib

    with open('pyproject.toml', 'rb') as f:
        data = tomllib.load(f)
