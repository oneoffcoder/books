Classes
=======

.. highlight:: python

Basic
-----

.. literalinclude:: code/oneoffcoder/clazz/basicclass.py
   :language: python
   :linenos:
   :emphasize-lines: 1-5

Getters and setters
-------------------

.. literalinclude:: code/oneoffcoder/clazz/gettersetter.py
   :language: python
   :linenos:
   :emphasize-lines: 7-23

Private method
--------------

.. literalinclude:: code/oneoffcoder/clazz/privatemethod.py
   :language: python
   :linenos:
   :emphasize-lines: 7-8

Static method
-------------

.. literalinclude:: code/oneoffcoder/clazz/staticmethod.py
   :language: python
   :linenos:
   :emphasize-lines: 7-8

Method overriding dunders
-------------------------

.. literalinclude:: code/oneoffcoder/clazz/methodoverriding.py
   :language: python
   :linenos:
   :emphasize-lines: 7-11

Inheritance
-----------

Here, we have a base class ``Animal``. Noticed how the Animal class itself inherits from ``ABC`` (Abstract Base Class)?
We annotate the ``make_noise`` method ``@abstractmethod`` decorator. A class that inherits from ``ABC`` cannot be 
instantiated directly. We create two subclasses, ``Dog`` and ``Cat``, from Animal. These derived classes can be
instantiated, however, they must implement all methods annotated with ``@abstractmethod`` or a ``TypeError`` will be thrown.
The Animal class is also called a ``formal interface``.

.. literalinclude:: code/oneoffcoder/clazz/inheritance.py
   :language: python
   :linenos:

Informal Interface
------------------

An informal interface is defined like a class but has no internal state and method implementations are not provided.
Below, we have a circle calculator which computes the area and circumference of a circle given
the radius. We also show how to implement the informal interface. 

.. literalinclude:: code/oneoffcoder/clazz/informalinterface.py
   :language: python
   :linenos:

Mixin
-----

A mixin is like an abstract base class, but does not have state. It sits somewhere between an informal
interface and abstract base class. Philosophically, a mixin avoids problems with single and multiple
inheritance. Single inheritance can be taken to an extreme where long chains of inheritance can obfuscate
the intentions of methods and properties (fragmentation). Multiple inheritance is problematic when 
`diamond dependencies <https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem>`_ are created.

Below, we have an example class ``DivisionSolver`` that solves a division problem; the dividend (numerator)
and divisor (denominator) must be given. The ``DivFloatMixin`` returns the solution as a float. 
The ``DivQRMixin`` returns the solution with the quotient and remainder.

.. literalinclude:: code/oneoffcoder/clazz/mixin.py
   :language: python
   :linenos:

Python has a lot of mixins. Below, we use the ``Mapping`` mixin to model a person's mailing label.
Notice that the ``MailingLabel`` class behaves like a dictionary?

.. literalinclude:: code/oneoffcoder/clazz/mixinmapping.py
   :language: python
   :linenos: