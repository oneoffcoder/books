Optional Tools
==============

Some libraries reduce boilerplate or provide convenience types, but they are
not part of the Java language. Treat them as optional tools after you understand
the core Java feature they resemble.

Lombok
------

Lombok generates code at compile time from annotations. It can reduce repetitive
model-class code, but it also adds an annotation processor to the build and
requires IDE support.

On current JDKs, configure the annotation processor explicitly instead of
depending on compiler classpath scanning.

.. literalinclude:: java-14/pom.xml
   :language: xml
   :linenos:
   :lines: 11-33
   :dedent: 2

.. literalinclude:: java-14/src/main/java/com/oneoffcoder/java/lombok/Lombok00.java
   :language: java
   :linenos:
   :lines: 30-45
   :dedent: 2

Before using Lombok for simple data classes, compare the same design with a
record. Records are standard Java and are usually the better default for
immutable data carriers.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/RecordData.java
   :language: java
   :linenos:
   :lines: 5-14
   :dedent: 2

Lombok still has uses in some teams and frameworks, especially when JavaBeans
accessors, builders, or mutable models are required. Keep it out of beginner
examples unless the lesson is specifically about build tools or annotation
processing.

Tuples
------

Java does not have built-in tuple types. The ``javatuples`` library provides
tuple classes such as ``Pair``, ``Triplet``, and ``Quintet``.

.. literalinclude:: java-14/src/main/java/com/oneoffcoder/java/tuple/Tuple01.java
   :language: java
   :linenos:
   :lines: 13-27
   :dedent: 4

Tuple values are accessed by position.

.. literalinclude:: java-14/src/main/java/com/oneoffcoder/java/tuple/Tuple02.java
   :language: java
   :linenos:
   :lines: 10-15
   :dedent: 4

Use tuples sparingly. A named record is usually clearer because each field has
a name and the type documents the domain concept.

.. code-block:: java

   record FullName(String firstName, String lastName) {}

The tuple examples remain useful as a side note, but records and small classes
are the idiomatic path for most Java code.
