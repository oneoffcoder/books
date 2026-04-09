Enumerations
============

.. highlight:: python

An ``enum`` is a type whose values come from a fixed set of named choices. Enums are useful when a value should be one of a small number of valid options, such as status codes, directions, or roles.

.. uml::

   @startuml
   skinparam classAttributeIconSize 0
   skinparam shadowing false

   enum Status {
     DRAFT
     PUBLISHED
     ARCHIVED
   }
   @enduml

Basic enum
----------

Without an enum, it is easy to scatter string constants throughout a program.

.. code-block:: python
   :linenos:

   STATUS_DRAFT = 'draft'
   STATUS_PUBLISHED = 'published'
   STATUS_ARCHIVED = 'archived'

With ``Enum``, the valid choices live in one clear type.

.. literalinclude:: code/oneoffcoder/enum/basic.py
   :language: python
   :linenos:

Why enums help
--------------

Enums make the set of valid states explicit. That improves readability and reduces bugs caused by typos in plain strings or magic numbers.

Using StrEnum
-------------

In modern Python, ``StrEnum`` is often a better fit when the enum values should still behave like strings at boundaries such as JSON or configuration files.

.. literalinclude:: code/oneoffcoder/enum/strenum.py
   :language: python
   :linenos:

Looping over enum values
------------------------

Enums are iterable, which makes them easy to display in menus or validate user-facing choices.

.. literalinclude:: code/oneoffcoder/enum/iterate.py
   :language: python
   :linenos:

When to use enums
-----------------

Use enums when the set of choices is stable and meaningful. If you simply need arbitrary user-provided strings, a normal string is still the right tool.

Exercise
--------

Create an enum named ``TicketStatus`` for a bug tracker with the values ``OPEN``, ``IN_PROGRESS``, ``BLOCKED``, and ``DONE``. Then:

- create a list of fake tickets using those values
- count how many tickets are in each status
- print a friendly menu by looping over the enum

.. uml::

   @startuml
   skinparam shadowing false
   enum TicketStatus {
     OPEN
     IN_PROGRESS
     BLOCKED
     DONE
   }
   @enduml
