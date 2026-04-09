Ignoring unpacked values from a tuple
-------------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid creating an extra variable when unpacking tuples. Use ``_`` for a value you intend to ignore.

Using ``_`` signals to readers that the value exists but is intentionally irrelevant here. That makes the unpacking contract clear without inventing a meaningless variable name that suggests the value matters.

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
