Hello, World!
=============

.. highlight:: java

.. role:: java(code)
    :language: java

.. role:: python(code)
    :language: python

Learning any programming language starts with the customary ``Hello, world!``
example. Modern Java lets you begin with a very small source file and then grow
the program into the classic class-based form when you are ready.

Compact source file
-------------------

For a first program on JDK 25 or newer, place this code in ``hello.java``.

.. code-block:: java

   void main() {
     IO.println("Hello, world!");
   }

Run it directly with the Java launcher.

.. code-block:: bash

   java hello.java

This form is called a compact source file. It keeps the first example focused
on statements, method calls, strings, and output. ``IO`` is a small console I/O
class in ``java.lang``, so it is available without an import.

Growing the program
-------------------

The same program can grow into an explicit class while keeping an instance
``main`` method.

.. code-block:: java

   class HelloWorld {
     void main() {
       IO.println("Hello, world!");
     }
   }

This is a useful bridge: students can see that methods live inside classes
without learning every modifier on the first page.

Classic main method
-------------------

Large Java programs still commonly use the classic static entry point shown
below. The example project uses this form because Maven, packages, tests, and
IDEs all handle it consistently.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/intro/HelloWorld.java
   :language: java
   :linenos:
   :lines: 3-9

The rest of the book uses complete class-based examples. When a chapter shows
only the body of ``main``, remember that the code still lives inside a class in
the full source file.
