Use InterpreterPoolExecutor for isolated parallel workers
---------------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.14 and later, consider ``InterpreterPoolExecutor`` when you want isolated workers without jumping straight to process management.

.. note::

   Python 3.14+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(str.upper, ['a', 'b', 'c']))

Do this
^^^^^^^

.. code:: python

    from concurrent.futures import InterpreterPoolExecutor

    with InterpreterPoolExecutor() as executor:
        results = list(executor.map(str.upper, ['a', 'b', 'c']))
