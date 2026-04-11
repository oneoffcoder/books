Libraries
=========

The Java standard library is large. Prefer standard library APIs first, and add
third-party dependencies only when the standard library does not cover the
problem well.

Math
----

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/MathClazz.java
   :language: java
   :linenos:
   :lines: 6-10
   :dedent: 4

StringBuilder
-------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/StringBuilderClazz.java
   :language: java
   :linenos:
   :lines: 6-24
   :dedent: 4

HTTP
----

Use ``java.net.http.HttpClient`` for new HTTP code. JDK 26 adds HTTP/3 support
to this API, but ordinary beginner code still uses the same ``HttpClient``,
``HttpRequest``, and ``HttpResponse`` types.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/HttpPackage.java
   :language: java
   :linenos:
   :lines: 3-6

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/HttpPackage.java
   :language: java
   :linenos:
   :lines: 11-23
   :dedent: 4
   

CSV
---

Writing data to a CSV
^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OpenCsvWrite.java
   :language: java
   :linenos:
   :lines: 3-6

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OpenCsvWrite.java
   :language: java
   :linenos:
   :lines: 11-28
   :dedent: 4

Reading data from a CSV
^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OpenCsvRead.java
   :language: java
   :linenos:
   :lines: 3-6

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OpenCsvRead.java
   :language: java
   :linenos:
   :lines: 11-34
   :dedent: 4

Static imports
--------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/StaticImport.java
   :language: java
   :linenos:
   :lines: 3-4

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/StaticImport.java
   :language: java
   :linenos:
   :lines: 9-11
   :dedent: 4

String tokenization
-------------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/StringTokenization.java
   :language: java
   :linenos:
   :lines: 3

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/StringTokenization.java
   :language: java
   :linenos:
   :lines: 8-17
   :dedent: 4

Optional
--------

``Optional`` is most useful as a return type when a method may not have a
result. Avoid using it as a field type or method parameter in beginner code;
plain values and validation are usually clearer there.

Basic use of optional
^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OptionalBasic.java
   :language: java
   :linenos:
   :lines: 3

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OptionalBasic.java
   :language: java
   :linenos:
   :lines: 8-13
   :dedent: 4

Nullable optional
^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OptionalNullable.java
   :language: java
   :linenos:
   :lines: 3

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OptionalNullable.java
   :language: java
   :linenos:
   :lines: 8-13
   :dedent: 4

Date
----

``Date`` and ``Calendar`` are legacy APIs. They appear in older code, but new
code should usually use the ``java.time`` package covered in the next chapter.

Basic date
^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/DateBasic.java
   :language: java
   :linenos:
   :lines: 3

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/DateBasic.java
   :language: java
   :linenos:
   :lines: 8-10
   :dedent: 4

Basic calendar
^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/CalendarBasic.java
   :language: java
   :linenos:
   :lines: 3-6

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/CalendarBasic.java
   :language: java
   :linenos:
   :lines: 11-34
   :dedent: 4

Calendar creation
^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/CalendarCreation.java
   :language: java
   :linenos:
   :lines: 3-5

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/CalendarCreation.java
   :language: java
   :linenos:
   :lines: 10-13
   :dedent: 4

Calendar manipulation
^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/CalendarManipulation.java
   :language: java
   :linenos:
   :lines: 3-4

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/CalendarManipulation.java
   :language: java
   :linenos:
   :lines: 9-19
   :dedent: 4

Random number generation
------------------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/RandomNumberGeneration.java
   :language: java
   :linenos:
   :lines: 3

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/RandomNumberGeneration.java
   :language: java
   :linenos:
   :lines: 8-16
   :dedent: 4
