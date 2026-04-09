Python 3.13 Notes
=================

This edition of the book targets Python 3.13. Most of the language and standard-library features used here also work in Python 3.11 and 3.12, but the recommendation is to learn and practice with Python 3.13 so your environment matches the examples and the current standard library.

.. graphviz::

   digraph py313 {
     rankdir=LR;
     node [shape=box, style="rounded"];
     edition [label="Python 3.13 edition"];
     syntax [label="modern syntax\nmatch, type hints, dataclasses"];
     stdlib [label="modern stdlib\npathlib, zoneinfo, tomllib"];
     tooling [label="modern tooling\nlogging, argparse, unittest"];
     edition -> syntax;
     edition -> stdlib;
     edition -> tooling;
   }

What this means in practice
---------------------------

- use Python 3 style classes, exceptions, and string formatting
- prefer modern standard-library modules such as ``pathlib`` over older string-based patterns
- use current typing syntax such as ``list[str]`` instead of older ``List[str]`` when appropriate
- treat ``tomllib`` as built in, since it is available in Python 3.13

What this book does not cover
-----------------------------

This is still an introduction. It does not try to cover every advanced runtime feature or deep implementation detail in Python 3.13. The goal is to give you a clean, modern base so you can read and write real Python confidently.
