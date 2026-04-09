Chained comparison operators
----------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid splitting simple chained comparisons with ``and`` when Python can express them directly.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    x = 10
    y = 15
    z = 20

    if x <= y and y <= z:
        print('hi')

Do this
^^^^^^^

.. code:: python

    if x <= y <= z:
        print('hi')
