Reading a file
--------------

.. highlight:: python
   :linenothreshold: 1

Use a context manager to handle file resources safely.

The ``with`` block ties acquisition and release together so the lifetime of the file handle is obvious from indentation alone. That improves correctness first, and it also makes the code easier to modify later without forgetting cleanup.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    f = open('README.md')
    try:
        data = f.read()
        print(len(data))
    finally:
        f.close()

Do this
^^^^^^^

.. code:: python

    with open('README.md') as f:
        data = f.read()
        print(len(data))
