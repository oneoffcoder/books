Use removeprefix and removesuffix
---------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``removeprefix()`` and ``removesuffix()`` instead of manual slicing when trimming known text.

.. note::

   Python 3.9+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    filename = 'report.csv'
    if filename.endswith('.csv'):
        filename = filename[:-4]

Do this
^^^^^^^

.. code:: python

    filename = 'report.csv'
    filename = filename.removesuffix('.csv')
