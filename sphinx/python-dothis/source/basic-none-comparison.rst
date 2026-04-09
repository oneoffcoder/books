Use is None for None checks
---------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``is None`` and ``is not None`` for ``None`` checks.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    if result == None:
        print('missing')

Do this
^^^^^^^

.. code:: python

    if result is None:
        print('missing')
