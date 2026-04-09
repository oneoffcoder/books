Ignoring unpacked values from a tuple
-------------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid creating an extra variable when unpacking tuples. Use ``_`` for a value you intend to ignore.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    def get_info():
        return 'John', 'Doe', 28

    fname, lname, tmp = get_info()

    print(fname, lname)

Do this
^^^^^^^

.. code:: python

    def get_info():
        return 'John', 'Doe', 28

    fname, lname, _ = get_info()

    print(fname, lname)
