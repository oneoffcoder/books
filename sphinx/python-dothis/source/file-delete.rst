Deleting a file
---------------

.. highlight:: python
   :linenothreshold: 1

The key here is to avoid the try/except code and favor a context manager approach.

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

    from contextlib import suppress

    with suppress(OSError):
        os.remove('test.tmp')
