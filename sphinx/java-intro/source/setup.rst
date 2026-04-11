Getting Started
===============

This book is built around small Java programs that can be read in the browser
and run from a local development environment. The core examples target
``JDK 25``, the latest long-term support release, so the syntax stays current
without depending on preview language features.

Version baseline
----------------

Use JDK 25 for the main book examples. JDK 26 is the latest feature release,
but JDK 25 is the better default for an introductory book because it is the
current LTS release.

The main example project is in ``source/code`` and is configured with Maven.
Its ``pom.xml`` sets the compiler release to JDK 25 and does not enable preview
features.

.. literalinclude:: code/pom.xml
   :language: xml
   :lines: 11-24
   :dedent: 2

Preview features are covered separately in the JDK 26 notes. Keep preview code
out of the main examples unless the chapter explicitly says otherwise.

Running compact source files
----------------------------

JDK 25 can run a small Java file directly.

.. code-block:: bash

   java hello.java

This is the easiest way to try the first chapter. It does not require a Maven
project, a package declaration, or a separate compilation step.

Running with Docker
-------------------

The Docker image from the preface starts Jupyter Lab on port ``8888``.

.. code-block:: bash

   docker run -it \
     -p 8888:8888 \
     oneoffcoder/book-java-intro

Open ``http://localhost:8888`` after the container is running. If the published
image lags behind the book's JDK 25 baseline, use a local JDK 25 installation
for the newer language examples.

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
   java -cp target/classes com.oneoffcoder.java.intro.HelloWorld

Examples that depend on external libraries, such as OpenCSV, are easiest to run
from Maven, Jupyter, or an IDE that understands the ``pom.xml`` file.

Reading examples in this book
-----------------------------

Most chapters show only the lines that matter for the topic being discussed.
The complete source files are under ``source/code/src/main/java``. For example,
the first class-based program appears in the book as a short listing, but the
full file is available at ``source/code/src/main/java/com/oneoffcoder/java/intro``.

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/intro/HelloWorld.java
   :language: java
   :linenos:

The package name at the top of a file must match its directory path under
``src/main/java``. That relationship becomes important as programs grow beyond
a single file.
