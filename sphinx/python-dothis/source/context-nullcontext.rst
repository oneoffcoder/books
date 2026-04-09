Use nullcontext for optional context managers
---------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``nullcontext()`` when a value is sometimes managed by a context manager and sometimes already available.

This keeps the control flow uniform: the code can always use ``with`` even when one branch does not need resource management. That usually reads better than splitting the main logic across two branches just to handle setup differently.

.. note::

   Python 3.7+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    if filename is None:
        data = stream.read()
    else:
        with open(filename) as stream:
            data = stream.read()

Do this
^^^^^^^

.. code:: python

    from contextlib import nullcontext

    cm = open(filename) if filename is not None else nullcontext(stream)
    with cm as fh:
        data = fh.read()
