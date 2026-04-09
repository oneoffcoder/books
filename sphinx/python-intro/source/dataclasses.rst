Dataclasses
===========

.. highlight:: python

``dataclasses`` are a modern way to define classes that mostly store data. They reduce boilerplate for common tasks such as creating an ``__init__()`` method, a readable ``__repr__()``, and value-based equality checks.

Basic dataclass
---------------

Without a dataclass, a simple record type can require a lot of repetitive code.

With ``@dataclass``, Python generates that boilerplate for you.

.. literalinclude:: code/oneoffcoder/dataclasses/basic.py
   :language: python
   :linenos:

Default values
--------------

You can give dataclass fields default values just as you would with function arguments.

.. literalinclude:: code/oneoffcoder/dataclasses/defaults.py
   :language: python
   :linenos:

Mutable defaults
----------------

Be careful with mutable defaults such as lists and dictionaries. Just like function defaults, they should not be shared across instances accidentally. Use ``field(default_factory=...)`` instead.

.. literalinclude:: code/oneoffcoder/dataclasses/mutabledefault.py
   :language: python
   :linenos:

Frozen dataclasses
------------------

If you want instances to behave like immutable records, use ``frozen=True``.

.. literalinclude:: code/oneoffcoder/dataclasses/frozen.py
   :language: python
   :linenos:

Why dataclasses matter
----------------------

Dataclasses are especially useful when a class mainly represents structured data rather than complicated behavior. They keep examples short, make code easier to read, and encourage you to model data with named fields instead of anonymous dictionaries or tuples.
