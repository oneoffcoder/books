Use default_factory for mutable dataclass defaults
--------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``default_factory`` for mutable dataclass fields instead of sharing one default object across instances.

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
