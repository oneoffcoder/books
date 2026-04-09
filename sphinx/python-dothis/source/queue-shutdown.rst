Use Queue.shutdown instead of sentinel values
---------------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.13 and later, prefer ``Queue.shutdown()`` over inventing sentinel values to stop worker threads.

.. note::

   Python 3.13+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import queue

    q = queue.Queue()

    q.put(task_1)
    q.put(None)

    item = q.get()
    if item is None:
        return

Do this
^^^^^^^

.. code:: python

    import queue

    q = queue.Queue()

    q.put(task_1)
    q.shutdown()
