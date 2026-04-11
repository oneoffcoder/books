Debugging and Logging
=====================

Every Java programmer spends time reading compiler errors, stack traces, and
logs. These tools are part of the programming workflow, not signs that
something unusual happened.

Compiler errors
---------------

Compiler errors happen before the program runs. They usually point to syntax
problems, missing imports, type mismatches, or package layout problems.

.. code-block:: text

   error: cannot find symbol
     Optional<String> name = Optional.of("John");
     ^
   symbol:   class Optional

In this case the code probably needs an import.

.. code-block:: java

   import java.util.Optional;

Runtime exceptions
------------------

Runtime exceptions happen while the program is running. The stack trace shows
the exception type, the message, and the path through the code.

.. code-block:: text

   Exception in thread "main" java.lang.ArithmeticException: / by zero
       at com.oneoffcoder.java.exception.DivideByZero.main(DivideByZero.java:8)

Start with the first line that points to your code. In this example, the useful
location is ``DivideByZero.java:8``.

Printing values
---------------

The quickest debugging tool is often a temporary print statement.

.. code-block:: java

   int total = price * quantity;
   System.out.println("total = " + total);

Print statements are useful while exploring, but they should not become the
main way a production program reports status.

Assertions
----------

Assertions document assumptions that should always be true while debugging.

.. code-block:: java

   int age = 23;
   assert age >= 0 : "age must be non-negative";

Assertions are disabled by default. Enable them with ``-ea`` when running the
program.

.. code-block:: bash

   java -ea com.oneoffcoder.java.SomeProgram

Basic logging
-------------

Java includes ``java.util.logging`` for simple logs.

.. code-block:: java

   import java.util.logging.Logger;

   public class LoggingDemo {
     private static final Logger LOGGER =
         Logger.getLogger(LoggingDemo.class.getName());

     public static void main(String[] args) {
       LOGGER.info("program started");
     }
   }

Logs are better than print statements when a program runs for a long time,
serves users, or needs different levels of detail in development and production.
