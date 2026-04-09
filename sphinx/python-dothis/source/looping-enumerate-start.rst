Use enumerate(start=...) for numbered loops
-------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``enumerate(..., start=1)`` instead of adding offsets inside the loop body.

Putting the starting offset in the iterator setup is easier to spot than adding ``1`` or another offset in several places inside the loop. It keeps numbering policy out of the loop body.

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
