Simultaneous state updates
--------------------------

.. highlight:: python
   :linenothreshold: 1

This pattern makes code more concise and avoids nuisance variables. In the first approach, temporary variables are used to stage updates. In the second, the related updates happen together in one assignment.

Bundling related assignments can also avoid transient intermediate states that do not really exist in the intended logic. It is a good fit when several names are being updated as one conceptual step.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    x, y = 1, 2
    temp = x
    x = y
    y = temp


.. code:: python

    def update_x(x):
        return x + 1

    def update_y(y):
        return y + 1

    x = 3
    y = 4
    dx = 4
    dy = 5

    tmp_x = x + dx
    tmp_y = y + dy
    tmp_dx = update_x(x)
    tmp_dy = update_y(y)

    x = tmp_x
    y = tmp_y
    dx = tmp_dx
    dy = tmp_dy

    print(x, y, dx, dy)

Do this
^^^^^^^

.. code:: python

    x, y = 1, 2
    x, y = y, x

.. code:: python

    def update_x(x):
        return x + 1

    def update_y(y):
        return y + 1
        
    x = 3
    y = 4
    dx = 4
    dy = 5

    x, y, dx, dy = (x + dx, y + dy, update_x(x), update_y(y))

    print(x, y, dx, dy)
