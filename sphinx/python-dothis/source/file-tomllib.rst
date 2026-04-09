Use tomllib for reading TOML
----------------------------

.. highlight:: python
   :linenothreshold: 1

Use the standard-library ``tomllib`` module for read-only TOML parsing.

Using the standard library removes an extra dependency for a very common configuration format and makes the parsing expectations obvious to readers. It is a strong default when you only need to read TOML, which is the common case for files like ``pyproject.toml``.

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
