Code Documentation
==================

.. highlight:: python

Good code documentation explains what a function does, what inputs it expects, and what it returns. In Python, the most common place to document that information is in a ``docstring``: a string literal placed immediately below a module, class, or function definition.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "Function definition" as fn
   rectangle "Docstring\npurpose\nparameters\nreturns" as doc
   rectangle "Reader / help() / docs tool" as reader

   fn --> doc
   doc --> reader
   @enduml

Basic docstrings
----------------

A basic docstring should describe the purpose of the function in plain language.

.. literalinclude:: code/oneoffcoder/documentation/basicdocstring.py
   :language: python
   :linenos:

You can inspect a function's docstring with ``help()`` or by reading its ``__doc__`` attribute.

.. literalinclude:: code/oneoffcoder/documentation/readdocstring.py
   :language: python
   :linenos:

Documenting parameters and return values
----------------------------------------

As functions become more important, the docstring should explain the parameters and the return value clearly.

.. literalinclude:: code/oneoffcoder/documentation/parameterreturn.py
   :language: python
   :linenos:

Sphinx style
------------

One common documentation style is the Sphinx or reStructuredText style. It is especially useful when your project uses Sphinx to build documentation automatically.

.. literalinclude:: code/oneoffcoder/documentation/sphinxstyle.py
   :language: python
   :linenos:

Google style
------------

Another common style is the Google docstring style. It is easy to read in source files and is supported by many editors, linters, and documentation tools.

.. literalinclude:: code/oneoffcoder/documentation/googlestyle.py
   :language: python
   :linenos:

Which style should you use?
---------------------------

The most important rule is consistency. Pick one style for a project and use it throughout the codebase. If your team already uses Sphinx-generated API docs, Sphinx-style docstrings may fit naturally. If your team prefers simpler source-level readability, Google-style docstrings are a common choice.

What to document
----------------

Not every tiny function needs a long docstring. Focus on documenting functions whose purpose, inputs, outputs, side effects, or error cases might not be obvious from the code alone. Good documentation should clarify the code, not repeat it word for word.
