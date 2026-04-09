Use the type statement for type aliases
---------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.12 and later, prefer the ``type`` statement for type aliases. It is clearer than assigning a type expression to a normal variable.

The dedicated syntax removes ambiguity between a type alias and an ordinary runtime assignment. That helps both readers and tooling distinguish definition-time type vocabulary from ordinary variables.

.. note::

   Python 3.12+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    from typing import TypeAlias

    UserId: TypeAlias = int
    ScoresByUser: TypeAlias = dict[UserId, list[int]]

Do this
^^^^^^^

.. code:: python

    type UserId = int
    type ScoresByUser = dict[UserId, list[int]]
