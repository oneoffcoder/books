Looping over a range of numbers
-------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid creating a list just to loop over a sequence of numbers. Use ``range`` instead because it is more concise and more memory-efficient.

``range`` describes a numeric sequence without allocating all of its values up front. That is the normal tool for count-controlled loops, so using it also matches reader expectations.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    for i in [0, 1, 2, 3, 4, 5]:
        print(i ** 2)

Do this
^^^^^^^

.. code:: python

    for i in range(6):
        print(i ** 2)
