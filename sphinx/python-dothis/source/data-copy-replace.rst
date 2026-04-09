Use copy.replace for shallow field updates
------------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.13 and later, use ``copy.replace()`` when you want a copy of an object with a few fields changed.

.. note::

   Python 3.13+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    from dataclasses import dataclass, replace

    @dataclass(frozen=True)
    class User:
        name: str
        active: bool

    user = User('alice', False)
    updated = replace(user, active=True)

Do this
^^^^^^^

.. code:: python

    from copy import replace
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class User:
        name: str
        active: bool

    user = User('alice', False)
    updated = replace(user, active=True)
