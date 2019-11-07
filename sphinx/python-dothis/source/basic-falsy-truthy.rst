Falsy and truthy
----------------

.. highlight:: python
   :linenothreshold: 1

It's enough to use the variable to test for falsy or truthy.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    is_male = True

    if is_male == True:
        print('is male is true')

Do this
^^^^^^^

.. code:: python

    is_male = True

    if is_male:
        print('is male is true')
