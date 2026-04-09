Use enumerate(start=...) for numbered loops
-------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``enumerate(..., start=1)`` instead of adding offsets inside the loop body.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    for i, name in enumerate(names):
        print(i + 1, name)

Do this
^^^^^^^

.. code:: python

    for i, name in enumerate(names, start=1):
        print(i, name)
