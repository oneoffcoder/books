Lambdas
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

If you have one-liner functions, avoid using function declaration with def. Instead, use lambda.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    def add_one(x):
        return x + 1

    add_one(3)

Do this
^^^^^^^

.. code:: python

    add_one = lambda x: x + 1

    add_one(3)
