Use dataclass(slots=True) for simple records
--------------------------------------------

.. highlight:: python
   :linenothreshold: 1

For simple data containers, prefer ``@dataclass(slots=True)`` over writing repetitive boilerplate by hand.

This keeps the declaration compact while also preventing arbitrary attribute creation on instances. It is a good fit for lightweight records whose fields are known up front and whose main job is to hold data clearly.

.. note::

   Python 3.10+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'Point(x={self.x}, y={self.y})'

Do this
^^^^^^^

.. code:: python

    from dataclasses import dataclass

    @dataclass(slots=True)
    class Point:
        x: int
        y: int
