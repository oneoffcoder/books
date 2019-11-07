Reading a file
--------------

.. highlight:: python
   :linenothreshold: 1

The key here is to use a context manager to manage resources.

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
