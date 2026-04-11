Getting Started
===============

This book is built around small Java programs that can be read in the browser
and run from a local development environment. The examples use ordinary Java
source files under a Maven project layout, so the same commands work from a
terminal, an IDE, or the Docker image described in the preface.

Version used by the examples
----------------------------

The main example project is in ``source/code`` and is configured with Maven.
Its ``pom.xml`` sets the compiler release to Java 13 and enables preview
features.

.. literalinclude:: code/pom.xml
   :language: xml
   :lines: 11-26
   :dedent: 2

There is also a smaller project in ``source/java-14`` that demonstrates records,
stream additions, tuples, and Lombok. That project is configured separately and
uses Java 15 preview settings.

.. literalinclude:: java-14/pom.xml
   :language: xml
   :lines: 11-29
   :dedent: 2

When you are running examples locally, use the JDK version expected by the
project you are compiling. If you use a newer JDK, Maven may still compile many
examples, but preview features and old preview syntax can require adjustment.

Running with Docker
-------------------

The simplest path is to use the Docker image from the preface.

.. code-block:: bash

   docker run -it \
     -p 8888:8888 \
     oneoffcoder/book-java-intro

The container starts Jupyter Lab on port ``8888``. Open
``http://localhost:8888`` after the container is running.

Running with Maven
------------------

From the main project directory, compile and test the Java examples with Maven.

.. code-block:: bash

   cd source/code
   mvn test

To run one class directly, compile first and then invoke the fully qualified
class name.

.. code-block:: bash

   cd source/code
   mvn test
   java --enable-preview \
     -cp target/classes:target/dependency/* \
     com.oneoffcoder.java.intro.HelloWorld

On Windows, use ``;`` instead of ``:`` between classpath entries.

Reading examples in this book
-----------------------------

Most chapters show only the lines that matter for the topic being discussed.
The complete source files are under ``source/code/src/main/java``. For example,
the first program appears in the book as a short listing, but the full file is
available at ``source/code/src/main/java/com/oneoffcoder/java/intro``.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/intro/HelloWorld.java
   :language: java
   :linenos:

The package name at the top of a file must match its directory path under
``src/main/java``. That relationship becomes important as programs grow beyond
a single file.
