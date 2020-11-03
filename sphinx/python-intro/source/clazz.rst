Classes
=======

Classes are the way to model your code after real-world objects. Classes define two things about objects: their properties and actions. Properties are simply traits, characteristics or attributes of an object. Actions are what the object can do. As such, properties are variables attached to a class and actions are functions attached to a class. When you start defining an object with a class (or start writing a class definition), always keep in mind the properties and actions that are important to that object and make a sketch or outline. Let's do some examples.

If you are trying to model a person, what are some properties of a person and what can a person do? A person has a first and last name, as well as an age. A person can also eat, sleep or talk.

* Person
   - properties
      * first name
      * last name
      * age
   - actions
      * eat
      * sleep
      * talk

If you are trying to model a square, what are some properties and actions of a square? A square has a side and can compute its own area and perimeter.

* Triangle
   - properties
      * side
   - actions
      * compute area
      * compute perimeter

What about modeling a car? A car has a make, model, year, doors and gas efficiency rating. A car can start up, speed up, slow down or stop. 

* Car
   - properties
      * make
      * model
      * year
      * number of doors
      * miles per gallon
   - actions
      * start up
      * speed 
      * slow
      * stop

.. highlight:: python

Basic
-----

The best way to understand how to define an object is by looking at the **simplest** example possible. Below, we are trying to model a car. Only the properties of a car are defined (make, model and year), and no actions are being modeled yet. You will notice that a class definition starts with the keyword ``class`` followed by the name (upper-cased). When we create an ``instance`` of a car, we need to 

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