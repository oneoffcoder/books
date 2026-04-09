Typing
======

.. highlight:: python

Type hints let you describe the kind of values a function expects and returns. Python stays dynamically typed, but type hints make code easier to read and help static analysis tools catch mistakes.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "Function signature\nadd(a: int, b: int) -> int" as sig
   rectangle "Reader" as reader
   rectangle "Type checker / editor" as tool

   sig --> reader
   sig --> tool
   @enduml

Basic type hints
----------------

Here is a function with parameter and return annotations.

.. literalinclude:: code/oneoffcoder/typing/basic.py
   :language: python
   :linenos:

Collection types
----------------

You can also annotate lists, dictionaries, and other container types.

.. literalinclude:: code/oneoffcoder/typing/collections.py
   :language: python
   :linenos:

Optional values
---------------

When a value may be missing, ``None`` is commonly part of the type.

.. literalinclude:: code/oneoffcoder/typing/optionalvalue.py
   :language: python
   :linenos:

Typed aliases
-------------

Type aliases can make repeated type signatures easier to understand.

.. literalinclude:: code/oneoffcoder/typing/typealias.py
   :language: python
   :linenos:

Why type hints help
-------------------

Type hints are useful documentation. They show readers what shape of data the code expects, and they work well with tools such as type checkers, editors, and code review. They are most helpful when they clarify interfaces, not when they repeat the obvious everywhere.

Exercise
--------

Annotate a small student-report module. Write:

- a type alias for ``dict[str, list[int]]`` to represent student grades
- a function that returns the average for one student
- a function that returns the top student name or ``None`` if there is no data

Use type hints on all parameters and return values.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "StudentGrades\nalias" as alias
   rectangle "get_average(name) -> float" as avg
   rectangle "get_top_student(...) -> str | None" as top

   alias --> avg
   alias --> top
   @enduml
