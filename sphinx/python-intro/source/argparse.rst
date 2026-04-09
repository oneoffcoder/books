Command-Line Arguments
======================

.. highlight:: python

The ``argparse`` module helps you build command-line programs that accept flags and parameters. It is the standard-library way to turn a script into a proper CLI tool.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "terminal command" as command
   rectangle "ArgumentParser" as parser
   rectangle "parsed args" as args
   rectangle "program logic" as logic

   command --> parser
   parser --> args
   args --> logic
   @enduml

Basic arguments
---------------

Create a parser, declare the arguments you expect, and then read them from ``args``.

.. literalinclude:: code/oneoffcoder/argparse/basic_args.py
   :language: python
   :linenos:

Flags
-----

Boolean flags are a good fit for optional behavior such as ``--verbose``.

.. literalinclude:: code/oneoffcoder/argparse/flags.py
   :language: python
   :linenos:

Choices
-------

You can restrict an argument to a small set of valid values.

.. literalinclude:: code/oneoffcoder/argparse/choices.py
   :language: python
   :linenos:

Exercise
--------

Write a command-line temperature converter that accepts a numeric value and a mode of either ``c-to-f`` or ``f-to-c``. Print the converted result.

.. uml::

   @startuml
   skinparam shadowing false
   start
   :Read value and mode;
   if (c-to-f?) then (yes)
     :convert to Fahrenheit;
   else (no)
     :convert to Celsius;
   endif
   :print result;
   stop
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   import argparse

   parser = argparse.ArgumentParser()
   parser.add_argument('value', type=float)
   parser.add_argument('mode', choices=['c-to-f', 'f-to-c'])
   args = parser.parse_args()

   if args.mode == 'c-to-f':
       result = args.value * 9 / 5 + 32
   else:
       result = (args.value - 32) * 5 / 9

   print(result)
