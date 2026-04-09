Use deque for queue operations
------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``collections.deque`` instead of a list when you need efficient queue operations from the left side.

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
