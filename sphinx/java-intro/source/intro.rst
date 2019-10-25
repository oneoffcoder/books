Hello, World!
=============

.. highlight:: java

.. role:: java(code)
    :language: java

.. role:: python(code)
    :language: python

Learning any programming language starts with the customary ``Hello, world!`` example. The ``Hello, world!`` example demonstrates the simplest code one may write and involves printing the words ``Hello, world!`` to the console. The ``Hello, world!`` example in Java is not as easy to understand as ``Python`` because printing statements to the console typically involves writing a program. The code below is a full Java program (although it does not do much). You need to get used to this program structure as it will be used repeatedly throughout this book to demonstrate how to write Java code. 

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/intro/HelloWorld.java
   :language: java
   :linenos:

Let's break down this program.

The statement, :java:`package com.oneoffcoder.java.intro;`, declares which `package` this program belongs to. In Java, code is organized into `packages` and then packages are shipped as a part of a `library`; thus, a `library` has many `packages`. The package naming convention is to use `reversed internet domain name`. For example, if Google, Microsoft or Twitter released libraries dealing with the `HTTP` protocol, they will typically have package prefixes named something like the following.

- com.google.http
- com.microsoft.http
- com.twitter.http

Reading the package name from left to right should give coders a really good intuition into the intentions and capabilities of the library and sub-packages.

The code, :java:`public class HelloWorld`, declares a class. Here is where we might fail in learning Java since we are in a chicken-and-egg problem. To learn about classes, we need to learn about the basic Java syntax, but to learn basic Java syntax, we need to know about writing classes. For now, just understand that every Java program requires a class definition. In this case, the class definition is ``HelloWorld``.

Notice the curly braces ``{`` and ``}``? Java uses these curly braces to signal a unit of logical code. Typically, when showing code, we often omit code inside the curly braces for brevity, and instead write ``{ ... }``. Thus, :java:`public class HelloWorld { ... }`, is the class definition, inside of which we will define the program.

Let's move onto, :java:`public static void main(String[] args) { ... }`, which is the program's entry point. A program's entry point is where the program begins when the outside world tells it to start. But, wow and yuck, as again, this declaration of the program's entrypoint is another potential point of failure in learning Java since there are so many words written. For now, just understand that the signature of a Java program's entry point is always :java:`public static void main(String[] args) { ... }`. This entry point is a function or method, and all the code inside of it is what really does the work. 

Finally, we get to :java:`System.out.println("Hello, world!")`, which is the statement to print ``Hello, world!`` to the console. Again, this verbose statement may be daunting to understanding since there are so many words and dots ``.``. In ``Python``, printing ``Hello, world!`` in a program is as simple as :python:`print('Hello, world!')`. However, in Java, printing ``Hello, world!`` or any string to the console is typically :java:`System.out.println("something")`. 

There you have it, the not-so-simple ``Hello, world!`` example in Java.
