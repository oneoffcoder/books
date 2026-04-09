Hello, World!
==============

.. highlight:: python

When you start to learn a programming language, the first program you write is typically one that prints ``Hello, world!`` to the terminal (or console). Below is the simplest Python statement that does exactly that.

.. uml::

   @startuml
   skinparam shadowing false

   rectangle "print('Hello, world!')" as statement
   rectangle "print" as function
   rectangle "'Hello, world!'" as argument
   rectangle "terminal output" as output

   statement --> function : calls
   statement --> argument : passes
   function --> output : writes text
   @enduml

.. literalinclude:: code/oneoffcoder/intro/helloworld.py
   :language: python
   :linenos:

Notice that this program is seemingly trivial, but a lot is going on. First, the ``print()`` command is actually a ``function``. The word ``print`` is the name of the function, and the opening and closing parentheses indicate that we are calling (or invoking) a function. Inside the parentheses, we have a string literal, ``'Hello, world!'``. All string literals are enclosed by either a pair of single or double quotes. In this example, it is said that we are passing a string literal to the print function; the string literal is called a ``parameter`` of or ``argument`` to the print function.

That is already a fair amount of background for such a small program. Even so, it shows one of Python's strengths early: simple tasks can often be expressed very directly. We have already touched on functions, arguments, and string literals while doing one of the simplest things possible in programming.

.. note::
   When I specify string literals, do I use single or double quotes?

   Single and double quotes may be used interchangeably to specify string literals in Python. When specifying string literals, be consistent; either always use single or double quotes, as best as you can, throughout your code.

Exercises
---------

Print your name
^^^^^^^^^^^^^^^
Try printing your name to the terminal.

Solution

.. code-block:: python
   :linenos:

   print('John Doe')
   print('Jane Smith')

Print a complete sentence
^^^^^^^^^^^^^^^^^^^^^^^^^
Try printing a complete sentence to the terminal.

Solution

.. code-block:: python
   :linenos:

   print('I am feeling fine today.')
   print('Today is very cold.')
   print('In fall, we fall back in time, in spring, we spring forward in time.')
