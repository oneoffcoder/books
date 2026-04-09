Ternary operator
----------------

.. highlight:: python
   :linenothreshold: 1

Python supports conditional expressions, which are often called the ternary operator.

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
