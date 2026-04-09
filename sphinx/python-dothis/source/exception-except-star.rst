Use except* for exception groups
--------------------------------

.. highlight:: python
   :linenothreshold: 1

When handling independent failures from concurrent work, use ``except*`` with exception groups.

Exception groups require you to think in terms of independent failures rather than one monolithic error path. ``except*`` expresses that model directly and lets you handle different error types without flattening away the structure of the group.

.. note::

   Python 3.11+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    try:
        run_parallel_jobs()
    except Exception as exc:
        for error in exc.exceptions:
            print(error)

Do this
^^^^^^^

.. code:: python

    try:
        run_parallel_jobs()
    except* ValueError as exc_group:
        for error in exc_group.exceptions:
            print(error)
