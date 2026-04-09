Reading a file
--------------

.. highlight:: python
   :linenothreshold: 1

Use a context manager to handle file resources safely.

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
