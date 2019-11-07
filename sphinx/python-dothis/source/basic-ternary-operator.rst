Ternary operator
----------------

.. highlight:: python
   :linenothreshold: 1

There is no official ternary operator in Python, but we may use the if/else statement as follows to mimic the ternary operator.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    is_male = True

    if is_male:
        gender = 'male'
    else:
        gender = 'female'

Do this
^^^^^^^

.. code:: python

    is_male = True
    
    gender = 'male' if is_male else 'female'
