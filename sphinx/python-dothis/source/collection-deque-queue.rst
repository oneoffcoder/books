Use deque for queue operations
------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``collections.deque`` instead of a list when you need efficient queue operations from the left side.

Lists are optimized for appending and popping at the end, not at the front. ``deque`` makes the queue behavior explicit and keeps performance predictable as the queue grows.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    queue = ['a', 'b', 'c']
    item = queue.pop(0)

Do this
^^^^^^^

.. code:: python

    from collections import deque

    queue = deque(['a', 'b', 'c'])
    item = queue.popleft()
