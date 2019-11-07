Simultaneous state updates
--------------------------

.. highlight:: python
   :linenothreshold: 1

The key here is to make your code more concise and avoid nuisance variables. In the discouraged approach, you create temporary variables to avoid mutating x and y. In the encouraged approach, all mutations occur in one coherent line.

Don't do this
^^^^^^^^^^^^^

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
