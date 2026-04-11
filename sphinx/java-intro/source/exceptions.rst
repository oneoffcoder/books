Exceptions
==========

Divide by zero example
----------------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/exception/DivideByZero.java
   :language: java
   :linenos:
   :lines: 6-8
   :dedent: 4

try-catch
---------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/exception/TryCatch.java
   :language: java
   :linenos:
   :lines: 6-14
   :dedent: 4
   :emphasize-lines: 4,7

throw
-----

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/exception/ThrowException.java
   :language: java
   :linenos:
   :lines: 6-14
   :dedent: 4
   :emphasize-lines: 8


try-catch-finally
-----------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/exception/TryCatchFinally.java
   :language: java
   :linenos:
   :lines: 6-18
   :dedent: 4
   :emphasize-lines: 9


try-catch with resources
------------------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/exception/TryCatchFinallyResource.java
   :language: java
   :linenos:
   :lines: 3-9

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/exception/TryCatchFinallyResource.java
   :language: java
   :linenos:
   :lines: 14-53
   :dedent: 4
   :emphasize-lines: 1-6,25-28

try-with-resources with an existing variable
--------------------------------------------

If a resource variable is final or effectively final, put the variable name in
the ``try`` header. You do not need to redeclare it inside the resource list.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/exception/TryWithExistingResource.java
   :language: java
   :linenos:
   :lines: 9-14
   :dedent: 2
   :emphasize-lines: 4
