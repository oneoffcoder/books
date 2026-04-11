Packages, Maven, and Project Layout
===================================

Java programs usually live inside packages, and Maven gives those packages a
standard directory layout. This chapter explains the structure used by the code
samples in this book.

Source directories
------------------

The main example project follows this layout.

.. code-block:: text

   source/code
   |-- pom.xml
   |-- src
       |-- main
       |   |-- java
       |       |-- com
       |           |-- oneoffcoder
       |               |-- java
       |-- test
           |-- java

Production code goes under ``src/main/java``. Test code goes under
``src/test/java``. Maven compiles both, but it treats them differently:
application classes are packaged as the program, while test classes are used
only while running tests.

Packages
--------

A Java file declares its package at the top of the file.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/intro/HelloWorld.java
   :language: java
   :lines: 1

That package maps to the directory
``src/main/java/com/oneoffcoder/java/intro``. If the package and directory do
not agree, compilers and IDEs will usually report confusing errors.

Imports
-------

Classes in ``java.lang`` are imported automatically. Other classes are imported
explicitly.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/library/OptionalBasic.java
   :language: java
   :lines: 3

Imports tell the compiler which type a short class name refers to. Without this
import, the program would need the fully qualified name ``java.util.Optional``.

Maven project files
-------------------

The ``pom.xml`` file declares the project metadata, compiler settings, plugins,
and dependencies. The example project depends on OpenCSV for CSV examples and
JUnit for test examples.

.. literalinclude:: code/pom.xml
   :language: xml
   :lines: 36-49
   :dedent: 2

Maven downloads dependencies into a local cache and places them on the classpath
when it compiles or tests the project. That is why chapters can use external
libraries without manually downloading ``.jar`` files.

Common Maven commands
---------------------

Use these commands from ``source/code``.

.. code-block:: bash

   mvn compile   # compile src/main/java
   mvn test      # compile and run tests
   mvn clean     # remove target/

The compiled output goes into ``target/classes`` and test output goes into
``target/test-classes``. The ``target`` directory is generated and should not be
edited by hand.
