Unpacking sequences and tuples
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid stretching simple unpacking across multiple lines. In the first approach, a tuple is stored and then indexed repeatedly. In the second, the tuple is unpacked directly in one line.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    def get_student():
        return 'john', 'doe', 88

    s = get_student()

    first_name = s[0]
    last_name = s[1]
    score = s[2]

    print(first_name, last_name, score)

Do this
^^^^^^^

.. code:: python

    def get_student():
        return 'john', 'doe', 88

    first_name, last_name, score = get_student()

    print(first_name, last_name, score)
