Use StrEnum for string enums
----------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``StrEnum`` instead of loose string constants when the values are still meant to behave like strings.

That keeps the benefits of an enum type without losing the ergonomics of string values at boundaries such as JSON, logs, and config files. It also reduces typo-prone comparisons against free-floating literals.

.. note::

   Python 3.11+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'

Do this
^^^^^^^

.. code:: python

    from enum import StrEnum

    class Status(StrEnum):
        DRAFT = 'draft'
        PUBLISHED = 'published'
