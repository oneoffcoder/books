Ternary operator
----------------

.. highlight:: python
   :linenothreshold: 1

Python supports conditional expressions, which are often called the ternary operator.

A conditional expression keeps a small value choice close to the assignment or return that uses it. It works best for simple two-way decisions; once the branches become large or side-effectful, a normal ``if`` statement is usually easier to read.

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
