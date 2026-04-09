Deleting a file
---------------

.. highlight:: python
   :linenothreshold: 1

If missing files are acceptable, ``contextlib.suppress`` keeps the intent clear.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import os

    try:
        os.remove('test.tmp')
    except OSError:
        pass

Do this
^^^^^^^

.. code:: python

    import os
    from contextlib import suppress

    with suppress(OSError):
        os.remove('test.tmp')
