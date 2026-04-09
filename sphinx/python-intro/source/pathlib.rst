Pathlib
=======

.. highlight:: python

``pathlib`` is the modern standard-library way to work with filesystem paths. It is usually clearer than building paths by hand with strings or older ``os.path`` helper functions.

Creating paths
--------------

Use ``Path`` objects to represent filesystem locations.

.. literalinclude:: code/oneoffcoder/pathlib/createpaths.py
   :language: python
   :linenos:

The ``/`` operator joins path segments in a readable way.

Checking files and directories
------------------------------

``Path`` objects provide convenient methods for common filesystem checks.

.. literalinclude:: code/oneoffcoder/pathlib/checks.py
   :language: python
   :linenos:

Reading and writing text
------------------------

For simple tasks, ``Path`` has built-in helpers for reading and writing files.

.. literalinclude:: code/oneoffcoder/pathlib/readwrite.py
   :language: python
   :linenos:

Globbing
--------

``Path.glob()`` is useful when you want to find files matching a pattern.

.. literalinclude:: code/oneoffcoder/pathlib/globbing.py
   :language: python
   :linenos:

Why pathlib matters
-------------------

``pathlib`` keeps path operations object-oriented and consistent. It is easier to read than manual string concatenation, and it helps keep filesystem code portable across operating systems.
