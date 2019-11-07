Enumerations
------------

.. highlight:: python
   :linenothreshold: 1

If you are working with enumerations, use the enum package. In the example below, we have students who may be part, half or full time. If we simply declared these states with normal variables, they may be overwritten and there will be no context. On the other hand, if we use IntEnum, once declared, these states are immutable and provide context.

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
