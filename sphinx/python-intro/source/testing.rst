Testing
=======

.. highlight:: python

Tests help you check that your code behaves the way you expect. Even small functions benefit from a few automated checks. The standard library includes ``unittest`` so you can start testing without extra dependencies.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "function under test" as fn
   rectangle "test case" as test
   rectangle "assertions" as assert
   rectangle "pass / fail" as result

   fn --> test
   test --> assert
   assert --> result
   @enduml

Simple assertions
-----------------

The simplest test checks that a function returns the value you expect.

.. literalinclude:: code/oneoffcoder/testing/simple_assertions.py
   :language: python
   :linenos:

Using unittest
--------------

``unittest`` gives you test classes, setup hooks, and richer assertions.

.. literalinclude:: code/oneoffcoder/testing/unittest_example.py
   :language: python
   :linenos:

Why testing matters
-------------------

Tests make refactoring safer and catch regressions early. They also serve as executable examples of how a function is supposed to behave.

Exercise
--------

Write tests for a function named ``is_even``. Check at least one even number, one odd number, and zero.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "is_even(2)" as even
   rectangle "is_even(3)" as odd
   rectangle "is_even(0)" as zero
   rectangle "expected True / False" as expected

   even --> expected
   odd --> expected
   zero --> expected
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   def is_even(n):
       return n % 2 == 0

   assert is_even(2) is True
   assert is_even(3) is False
   assert is_even(0) is True
