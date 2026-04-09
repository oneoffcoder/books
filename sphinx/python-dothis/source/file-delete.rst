Deleting a file
---------------

.. highlight:: python
   :linenothreshold: 1

If missing files are acceptable, ``contextlib.suppress`` keeps the intent clear.

Deleting a file is often best-effort cleanup, so treating a missing file as noise can be reasonable. The goal is to make that choice explicit without broadening the exception handling more than necessary.

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
