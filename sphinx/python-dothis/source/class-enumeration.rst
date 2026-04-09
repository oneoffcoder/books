Enumerations
------------

.. highlight:: python
   :linenothreshold: 1

If you are working with enumerations, use the ``enum`` module. In the example below, students may be part-time, half-time, or full-time. If you declare these states as plain variables, they can be overwritten and provide little context. ``IntEnum`` makes the intent explicit and keeps the values grouped under a meaningful type.

Enums give invalid states fewer places to hide and make call sites easier to read than raw integers or strings. They also centralize the valid choices, which helps both tooling and future maintenance.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    PART_TIME = 1
    HALF_TIME = 2
    FULL_TIME = 3

Do this
^^^^^^^

.. code:: python

    from enum import IntEnum

    class StudentType(IntEnum):
        PART_TIME = 1
        HALF_TIME = 2
        FULL_TIME = 3
