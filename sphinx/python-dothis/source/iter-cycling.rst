Cycling through a list
----------------------

.. highlight:: python
   :linenothreshold: 1

Here's how to cycle through a list of elements an arbitrary number of times.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    colors = ['red', 'green', 'blue']

    color_sequence = []
    index = 0

    for i in range(10):
        color_sequence.append(colors[index])
        index += 1
        if index == 3:
            index = 0

Do this
^^^^^^^

.. code:: python

    from itertools import cycle

    colors = ['red', 'green', 'blue']

    color_cycle = cycle(colors)
    color_sequence = (next(color_cycle) for _ in range(10))