New vs old classes
------------------

.. highlight:: python
   :linenothreshold: 1

When declaring a class, always inherit from `object` as there are additional, optimized properties and behaviors that your class will inherit (e.g. |slots_link|).

.. |slots_link| raw:: html

    <a href="https://docs.python.org/3.7/reference/datamodel.html#slots" target="_blank">__slots__</a>
    
Don't do this
^^^^^^^^^^^^^

.. code:: python

    class Car():
        def __init_(self, make, model):
            self.make = make
            self.model = model

Do this
^^^^^^^

.. code:: python

    class Car(object):
        def __init_(self, make, model):
            self.make = make
            self.model = model
