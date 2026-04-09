Use template strings for structured interpolation
-------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.14 and later, use template strings when you need structured interpolation data instead of a finished string immediately.

.. note::

   Python 3.14+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    name = 'alice'
    sql = f'SELECT * FROM users WHERE name = {name!r}'

Do this
^^^^^^^

.. code:: python

    name = 'alice'
    query = t'SELECT * FROM users WHERE name = {name!r}'
