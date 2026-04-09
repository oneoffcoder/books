Use contextlib.suppress for narrow ignored exceptions
-----------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``contextlib.suppress`` when a specific exception is expected and can be ignored cleanly.

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
