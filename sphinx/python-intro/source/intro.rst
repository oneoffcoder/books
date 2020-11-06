Hello, World!
==============

.. highlight:: python

When you start to learn a programming langugage, the first program you code is typically to print ``Hello, world!`` to the terminal (or console). Below is the simplest command you can code in Python to get ``Hello, world!`` to be printed.

.. literalinclude:: code/oneoffcoder/intro/helloworld.py
   :language: python
   :linenos:

Notice that this program is seemingly trivial, but a lot is going on. First, the ``print()`` command is actually a ``function``. The word ``print`` is the name of the function, and the opening and closing parentheses indicate that we are calling (or invoking) a function. Inside the parentheses, we have a string literal, ``'Hello, world!'``. All string literals are enclosed by either a pair of single or double quotes. In this example, it is said that we are passing a string literal to the print function; the string literal is called a ``parameter`` of or ``argument`` to the print function.

This background information a lot already just to understand how to print something. Compared to other languages (e.g. Java), however, printing something to the terminal is very easy in Python. Quickly, we have already gotten ahead of ourselves by talking about functions, parameters, arguments and string literals while doing one the simplest thing possible in coding with Python.

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