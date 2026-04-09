Classes and dunders (double underscores)
----------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use dunder methods when they improve how objects behave. In particular, override ``__str__`` to provide a printer-friendly representation of an object.

Special methods let your objects participate in Python's built-in protocols instead of requiring callers to remember custom helper methods. That usually produces code that feels more native at the call site and concentrates representation logic inside the type that owns it.

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
