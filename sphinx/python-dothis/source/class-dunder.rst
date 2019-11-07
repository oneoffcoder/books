Classes and dunders (double underscores)
----------------------------------------

.. highlight:: python
   :linenothreshold: 1

Exploit dunders when doing object-oriented programming in Python. In particular, override the __str__ dunder to enable a printer friendly representation of the object.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    class Student():
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
            
    student = Student('John', 'Doe')

    print(student)

Do this
^^^^^^^

.. code:: python

    class Student():
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
            
        def __str__(self):
            return f'{self.first_name} {self.last_name}'
            
    student = Student('John', 'Doe')

    print(student)
