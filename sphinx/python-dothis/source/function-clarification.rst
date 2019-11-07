Clarify function calls with keyword arguments
---------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When passing in values/arguments to a method, try to associate the values with the argument names.

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