Use concurrent.interpreters instead of custom wrappers
------------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.14 and later, use ``concurrent.interpreters`` rather than building your own thin wrapper around low-level subinterpreter management.

.. note::

   Python 3.14+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    # custom wrapper around private or low-level interpreter management
    worker = start_subinterpreter()
    worker.run('print("hello")')

Do this
^^^^^^^

.. code:: python

    from concurrent import interpreters

    interp = interpreters.create()
    interp.exec('print("hello")')
