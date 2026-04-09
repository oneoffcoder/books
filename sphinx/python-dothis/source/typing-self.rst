Use Self for fluent instance return types
-----------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``Self`` when a method returns an instance of its own class.

.. note::

   Python 3.11+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    class Query:
        def filter(self, expr: str) -> 'Query':
            return self

Do this
^^^^^^^

.. code:: python

    from typing import Self

    class Query:
        def filter(self, expr: str) -> Self:
            return self
