Ignoring unpacked values from a tuple
-------------------------------------

.. highlight:: python
   :linenothreshold: 1

Try not to create that extra variable declaration when unpacking tuples. Use the underscore `_` to ignore declaring a variable when unpacking a tuple.

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
