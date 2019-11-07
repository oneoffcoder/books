Unpacking sequences and tuples
--------------------------------------

.. highlight:: python
   :linenothreshold: 1

The key is to avoid long code that breaks up the coherent intention. In the discouraged approach, we receive a tuple, and store it in s and then for each element in s, use a different line to access the values. In the encouraged approach, the tuple is unpacked neatly into one line.

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