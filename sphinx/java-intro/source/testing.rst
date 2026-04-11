Testing
========

Running a ``main`` method is useful while learning syntax, but tests are better
when you want repeatable checks. A test states what the code should do and lets
Maven run that check every time the project changes.

Running tests
-------------

The example project uses JUnit. Run the test suite from ``source/code``.

.. code-block:: bash

   mvn test

Maven compiles the application code, compiles the test code, and then runs any
test classes it discovers under ``src/test/java``.

The existing test harness
-------------------------

The project includes a broad test that finds example classes and invokes their
``main`` methods. A few examples intentionally throw exceptions, so the harness
ignores those classes.

.. literalinclude:: code/src/test/java/com/oneoffcoder/java/TestAll.java
   :language: java
   :linenos:
   :lines: 81-85
   :dedent: 4

Each discovered class is wrapped in a ``Callable`` and executed by an executor.

.. literalinclude:: code/src/test/java/com/oneoffcoder/java/TestAll.java
   :language: java
   :linenos:
   :lines: 84-95
   :dedent: 4

The final loop fails the JUnit test if any example failed unexpectedly.

.. literalinclude:: code/src/test/java/com/oneoffcoder/java/TestAll.java
   :language: java
   :linenos:
   :lines: 105-109
   :dedent: 4

A small unit test
-----------------

Most production tests are narrower than the example harness. They call one
method and compare the actual result to the expected result.

.. code-block:: java

   package com.oneoffcoder.java;

   import org.junit.Assert;
   import org.junit.Test;

   public class ArithmeticTest {

     @Test
     public void addsTwoNumbers() {
       int result = 2 + 3;
       Assert.assertEquals(5, result);
     }
   }

Good tests usually follow the same pattern: arrange the input, act by calling
the code under test, and assert the result.

Testing exceptions
------------------

Some code should throw an exception for invalid input. JUnit can make that
expectation explicit.

.. code-block:: java

   @Test(expected = ArithmeticException.class)
   public void divisionByZeroFails() {
     int result = 10 / 0;
   }

That test passes only when ``ArithmeticException`` is thrown.
