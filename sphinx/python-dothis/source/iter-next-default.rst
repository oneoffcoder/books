Use next with a default for searches
------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``next()`` with a generator expression when you want the first matching item.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    match = None
    for user in users:
        if user.id == target_id:
            match = user
            break

Do this
^^^^^^^

.. code:: python

    match = next((user for user in users if user.id == target_id), None)
