String debug
------------

.. highlight:: python
   :linenothreshold: 1

When debugging with f-strings, use the built-in debug format to be more concise.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    x = 35
    y = 88

    print(f'x = {x}, y = {y}')
    print(f'x * y = {x * y}')

Do this
^^^^^^^

.. code:: python

    x = 35
    y = 88

    print(f'{x = }, {y = }')
    print(f'{x * y = }')
