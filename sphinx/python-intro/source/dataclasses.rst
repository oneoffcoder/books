Dataclasses
===========

.. highlight:: python

``dataclasses`` are a modern way to define classes that mostly store data. They reduce boilerplate for common tasks such as creating an ``__init__()`` method, a readable ``__repr__()``, and value-based equality checks.

.. uml::

   @startuml
   skinparam classAttributeIconSize 0
   skinparam shadowing false

   class Student {
     name : str
     grade : int
   }

   note right of Student
     @dataclass can generate:
     - __init__()
     - __repr__()
     - __eq__()
   end note
   @enduml

Basic dataclass
---------------

Without a dataclass, a simple record type can require a lot of repetitive code.

With ``@dataclass``, Python generates that boilerplate for you.

.. literalinclude:: code/oneoffcoder/dataclasses/basic.py
   :language: python
   :linenos:

Default values
--------------

You can give dataclass fields default values just as you would with function arguments.

.. literalinclude:: code/oneoffcoder/dataclasses/defaults.py
   :language: python
   :linenos:

Mutable defaults
----------------

Be careful with mutable defaults such as lists and dictionaries. Just like function defaults, they should not be shared across instances accidentally. Use ``field(default_factory=...)`` instead.

.. literalinclude:: code/oneoffcoder/dataclasses/mutabledefault.py
   :language: python
   :linenos:

Frozen dataclasses
------------------

If you want instances to behave like immutable records, use ``frozen=True``.

.. literalinclude:: code/oneoffcoder/dataclasses/frozen.py
   :language: python
   :linenos:

Why dataclasses matter
----------------------

Dataclasses are especially useful when a class mainly represents structured data rather than complicated behavior. They keep examples short, make code easier to read, and encourage you to model data with named fields instead of anonymous dictionaries or tuples.

Exercise
--------

Model a small library system with dataclasses. Create a ``Book`` dataclass with ``title``, ``author``, ``year``, and ``tags``. Then:

- give ``tags`` a safe default with ``field(default_factory=list)``
- create at least three books
- compare two books for equality
- print the books so you can see the generated ``__repr__()``

.. uml::

   @startuml
   skinparam shadowing false
   skinparam classAttributeIconSize 0

   class Book <<dataclass>> {
     title: str
     author: str
     year: int
     tags: list[str]
   }
   @enduml
