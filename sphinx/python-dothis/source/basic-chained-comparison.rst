Chained comparison operators
----------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid splitting simple chained comparisons with ``and`` when Python can express them directly.

The chained form matches the mathematical idea directly and avoids repeating the middle operand. That reduces visual noise and makes boundary checks easier to audit during review.

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
