Input/Output (IO)
=================

Modern Java code should usually start with ``Path`` and ``Files`` from
``java.nio.file``. Older ``File`` and stream classes are still useful, but
``Path`` and ``Files`` cover many common tasks with less ceremony.

Path and Files
--------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/PathFiles.java
   :language: java
   :linenos:
   :lines: 3-5

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/PathFiles.java
   :language: java
   :linenos:
   :lines: 9-16
   :dedent: 2
   :emphasize-lines: 1,5-6

Writing to a file
-----------------

The next example uses older writer classes. This style is still common in
existing code and remains useful when you need detailed control over buffering
or streaming.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/WritingFile.java
   :language: java
   :linenos:
   :lines: 3-7

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/WritingFile.java
   :language: java
   :linenos:
   :lines: 12-19
   :dedent: 4
   :emphasize-lines: 3

Reading from a file
-------------------

Reading one line at a time
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/ReadingFile.java
   :language: java
   :linenos:
   :lines: 3-5

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/ReadingFile.java
   :language: java
   :linenos:
   :lines: 10-15
   :dedent: 4
   :emphasize-lines: 1

Reading all lines 
^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/ReadingFileAllLines.java
   :language: java
   :linenos:
   :lines: 3-4

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/ReadingFileAllLines.java
   :language: java
   :linenos:
   :lines: 9-11
   :dedent: 4
   :emphasize-lines: 1

Reading whole file
^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/ReadingFileWholeText.java
   :language: java
   :linenos:
   :lines: 3-4

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/io/ReadingFileWholeText.java
   :language: java
   :linenos:
   :lines: 9-13
   :dedent: 4
   :emphasize-lines: 1-3
