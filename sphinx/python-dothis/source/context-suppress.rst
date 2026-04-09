Use contextlib.suppress for narrow ignored exceptions
-----------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``contextlib.suppress`` when a specific exception is expected and can be ignored cleanly.

A narrow suppress block documents that the exception is intentionally non-fatal in this specific operation. It is much safer than a broad ``try``/``except`` because the ignored surface area stays small and visible.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    try:
        cache.pop('expired')
    except KeyError:
        pass

Do this
^^^^^^^

.. code:: python

    from contextlib import suppress

    with suppress(KeyError):
        cache.pop('expired')
