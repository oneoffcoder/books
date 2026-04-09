Use is None for None checks
---------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``is None`` and ``is not None`` for ``None`` checks.

``None`` is a singleton, so identity is the right concept here, not equality. Using ``is`` also avoids surprising behavior from user-defined ``__eq__`` methods that can make ``== None`` behave in unexpected ways.

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
