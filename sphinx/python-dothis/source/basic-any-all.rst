Use any and all for boolean scans
---------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``any()`` and ``all()`` instead of managing boolean flags by hand.

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
