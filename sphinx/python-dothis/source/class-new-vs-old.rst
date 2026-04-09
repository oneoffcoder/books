New vs old classes
------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3, every class is already a "new-style" class. You do not need to inherit from ``object`` explicitly.

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
