Use any and all for boolean scans
---------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``any()`` and ``all()`` instead of managing boolean flags by hand.

These builtins move the scan logic into a well-known idiom and keep the loop body out of the way. They short-circuit naturally, so they stop as soon as the answer is known, and they read like the question the code is asking.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    has_negative = False
    for value in values:
        if value < 0:
            has_negative = True
            break

Do this
^^^^^^^

.. code:: python

    has_negative = any(value < 0 for value in values)
