Use next with a default for searches
------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``next()`` with a generator expression when you want the first matching item.

This idiom captures a very common search pattern: first match or fallback. It keeps the success condition close to the iteration and avoids sentinel setup, ``break`` bookkeeping, and post-loop checks.

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
