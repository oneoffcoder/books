Collection initialization
-------------------------

.. highlight:: python
   :linenothreshold: 1

When initializing empty Python collections such as lists and dictionaries, favor using the corresponding literal delimiters instead of the corresponding functions.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = list() # initialize list
    data = dict()  # initialize dictionary

Do this
^^^^^^^

.. code:: python

    names = [] # initialize list
    data = {}  # initialize dictionary


Using the literal delimiters ``[]`` and ``{}`` is faster and more Pythonic than using ``list()`` and ``dictionary()``. The former approach is faster since the bytecode generated does not try to find the names of the function. You should inspect the bytecode generated.

The bytecode generated for :code:`[]` can be generated as follows.

.. code:: python

    from dis import dis

    dis('[]')


And the bytecode will look as follows. Notice there are only 2 lines of bytecode.

.. code:: text

    1           0 BUILD_LIST               0
                2 RETURN_VALUE

The bytecode generated for :code:`list()` can be generated as follows.

.. code:: python

    from dis import dis

    dis('list()')

And the bytecode will look as follows. Notice there are 3 lines of bytecode.

.. code:: text

    1           0 LOAD_NAME                0 (list)
                2 CALL_FUNCTION            0
                4 RETURN_VALUE

Here's the bytecode for :code:`{}`.

.. code:: text

    1           0 BUILD_MAP                0
                2 RETURN_VALUE

Here's the bytecode for :code:`dict()`.

.. code:: text

    1           0 LOAD_NAME                0 (dict)
                2 CALL_FUNCTION            0
                4 RETURN_VALUE