Control Statements
==================

if-else
-------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/control/IfElse.java
   :language: java
   :linenos:
   :lines: 6-13
   :dedent: 4
   :emphasize-lines: 4-8

if-elseif-else
--------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/control/IfElseIfElse.java
   :language: java
   :linenos:
   :lines: 6-14
   :dedent: 4
   :emphasize-lines: 5

Nested if-else
--------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/control/IfElseNested.java
   :language: java
   :linenos:
   :lines: 6-18
   :dedent: 4
   :emphasize-lines: 8-12

switch
------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/control/SwitchBasic.java
   :language: java
   :linenos:
   :lines: 6-22
   :dedent: 4
   :emphasize-lines: 3-17

Nested switch
-------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/control/SwitchNested.java
   :language: java
   :linenos:
   :lines: 6-26
   :dedent: 4
   :emphasize-lines: 6-12,14-20

Arrow syntax for switch
-----------------------

Modern ``switch`` statements can use arrow labels. This avoids accidental
fall-through between cases.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/control/SwitchNew.java
   :language: java
   :linenos:
   :lines: 6-14
   :dedent: 4
   :emphasize-lines: 3-9

Switch expressions
------------------

Modern ``switch`` can also produce a value. This works well when each branch
chooses one result and the rest of the method should keep moving. Use
``yield`` when a branch needs a block with more than one statement.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/control/SwitchExpression.java
   :language: java
   :linenos:
   :lines: 6-19
   :dedent: 4
   :emphasize-lines: 3-12

JDK 26 previews primitive patterns in ``switch``. Keep those examples in the
JDK 26 preview notes until the feature is final.
