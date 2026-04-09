Clarify function calls with keyword arguments
---------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When passing values to a function, prefer keyword arguments when they make the call clearer.

Keyword arguments turn positional knowledge into explicit names at the call site, which is especially helpful when several parameters share the same broad type. They also make later refactors safer because reviewers can see which argument is intended to mean what.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    def format_information(first_name, last_name, age):
        return '{} {} is {} years old'.format(first_name, last_name, age)

    format_information('John', 'Doe', 28)

Do this
^^^^^^^

.. code:: python

    def format_information(first_name, last_name, age):
        return '{} {} is {} years old'.format(first_name, last_name, age)

    format_information(first_name='John', last_name='Doe', age=28)

.. code:: python

    def format_information(first_name, last_name, age):
        return '{} {} is {} years old'.format(first_name, last_name, age)

    format_information(**{
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 28
    })
