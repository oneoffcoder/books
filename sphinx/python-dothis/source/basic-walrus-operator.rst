Use the walrus operator to avoid repeated work in conditions
------------------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When a condition also needs the computed value, ``:=`` can be clearer than computing the same result twice.

The walrus operator is most helpful when a condition naturally produces a value you need immediately afterward. Used this way, it removes duplicated calls and keeps the read-test-use flow together, but it should stay local and simple rather than turning a condition into a dense expression.

.. note::

   Python 3.8+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    line = input_stream.readline()
    while line != '':
        print(line.strip())
        line = input_stream.readline()

Do this
^^^^^^^

.. code:: python

    while (line := input_stream.readline()) != '':
        print(line.strip())
