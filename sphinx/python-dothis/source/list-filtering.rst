Filtering a list
----------------

.. highlight:: python
   :linenothreshold: 1

Use a comprehension to filter values instead of building the list with a loop.

Comprehensions keep the element transformation and filter condition together in one expression, which makes the resulting list easy to understand at a glance. They also avoid the visual overhead of a temporary list plus repeated ``append`` calls.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    nums = []
    for i in range(100):
        if i % 2 == 0:
            nums.append(i)

Do this
^^^^^^^

.. code:: python

    nums = [i for i in range(100) if i % 2 == 0]
