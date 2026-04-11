Modern Java Idioms
==================

Modern Java is still Java: classes, methods, packages, and static typing are
the foundation. The difference is that many common patterns now have clearer
language support. This chapter focuses on stable features available in the
JDK 25 LTS baseline.

Records for data
----------------

Use records for small immutable data carriers. A record declares its state in
the header and Java generates the constructor, accessors, ``equals()``,
``hashCode()``, and ``toString()``.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/RecordData.java
   :language: java
   :linenos:
   :lines: 5-14
   :dedent: 2

Records can have normal methods when the data has behavior closely tied to it.
Callers use accessor methods named after the components.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/RecordData.java
   :language: java
   :linenos:
   :lines: 16-22
   :dedent: 2

Use a class instead of a record when identity, mutation, inheritance, or a long
lifecycle is central to the object.

Sealed hierarchies
------------------

Use sealed types when a hierarchy has a known set of implementations. This is
common for domain alternatives such as commands, events, messages, or result
types.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/PatternMatching.java
   :language: java
   :linenos:
   :lines: 5-9
   :dedent: 2

The compiler can use the sealed hierarchy to check whether a ``switch`` handles
every possible subtype.

Pattern matching
----------------

Pattern matching removes the old "check, cast, assign" ceremony around
``instanceof``.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/PatternMatching.java
   :language: java
   :linenos:
   :lines: 22-28
   :dedent: 2

Pattern matching for ``switch`` and record patterns work well with sealed
hierarchies. The ``switch`` below handles every permitted ``Media`` subtype and
decomposes records directly in the case labels.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/PatternMatching.java
   :language: java
   :linenos:
   :lines: 11-20
   :dedent: 2

This style is usually clearer than a chain of ``if`` statements when the input
can be one of several known shapes.

Module imports
--------------

JDK 25 supports module import declarations. They import the public API exported
by a module and are useful in small programs, examples, and exploratory code.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/ModuleImportDemo.java
   :language: java
   :linenos:
   :lines: 3-16

Explicit imports are still better in many production files because they show
exactly which external names the file uses. Module imports are strongest when
they lower beginner friction or make short examples easier to read.

Flexible constructor bodies
---------------------------

JDK 25 lets a constructor do validation and simple preparation before calling
``super(...)``. This keeps invalid values out of the parent constructor.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/modern/FlexibleConstructorBodies.java
   :language: java
   :linenos:
   :lines: 19-27
   :dedent: 2
   :emphasize-lines: 3-6

The code before ``super(...)`` is still restricted. It cannot read from the
partly constructed object through ``this``.

Unnamed variables and patterns
------------------------------

Use ``_`` when a variable or pattern component is intentionally unused.

.. code-block:: java

   try {
     int value = Integer.parseInt(text);
     System.out.println(value);
   } catch (NumberFormatException _) {
     System.out.println("not a number");
   }

This avoids fake names such as ``ignored`` or ``unused``. It also tells the
reader and compiler that the value is deliberately not used.

Compact source files
--------------------

For small programs, scripts, and first lessons, compact source files avoid the
full class wrapper.

.. code-block:: java

   void main() {
     IO.println("Hello, world!");
   }

Use compact source files at the beginning of the learning path. Move to normal
class-based files when you need packages, tests, multiple classes, or ordinary
project structure.
