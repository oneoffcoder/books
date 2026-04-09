New vs old classes
------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3, every class is already a "new-style" class. You do not need to inherit from ``object`` explicitly.

Leaving out ``object`` removes a historical compatibility artifact that no longer carries meaning in modern Python. Trimming those leftovers makes examples shorter and signals that the code is written for current Python, not for Python 2.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    class Car(object):
        def __init__(self, make, model):
            self.make = make
            self.model = model

Do this
^^^^^^^

.. code:: python

    class Car:
        def __init__(self, make, model):
            self.make = make
            self.model = model
