Use removeprefix and removesuffix
---------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``removeprefix()`` and ``removesuffix()`` instead of manual slicing when trimming known text.

The dedicated methods encode the exact intent and avoid off-by-one or accidental-match bugs from manual slicing. They are also easier to read because a reviewer does not have to reconstruct why a particular slice index was chosen.

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
