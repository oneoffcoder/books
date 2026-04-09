Use default_factory for mutable dataclass defaults
--------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``default_factory`` for mutable dataclass fields instead of sharing one default object across instances.

Mutable defaults are shared at class definition time, which means one instance can accidentally affect another. ``default_factory`` makes the per-instance allocation explicit and prevents one of the most common dataclass footguns.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    from dataclasses import dataclass

    @dataclass
    class Report:
        tags: list[str] = []

Do this
^^^^^^^

.. code:: python

    from dataclasses import dataclass, field

    @dataclass
    class Report:
        tags: list[str] = field(default_factory=list)
