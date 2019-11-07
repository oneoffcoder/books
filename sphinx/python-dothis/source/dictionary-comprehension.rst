Dictionary comprehension
------------------------

.. highlight:: python
   :linenothreshold: 1

Here, we want to create two dictionaries; index-to-word i2w and word-to-index w2i. In the discouraged approach, we create two dictionaries, use a for loop, and set the key-value pair with the help of enumerate; there are 5 lines of code. In the encouraged approach, using two lines of code, we can declare and instantiate the dictionaries with a for comprehension.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    words = ['i', 'like', 'to', 'eat', 'pizza', 'and', 'play', 'tennis']

    i2w = {}
    w2i = {}
    for i, word in enumerate(words):
        i2w[i] = word
        w2i[word] = i

Do this
^^^^^^^

.. code:: python

    words = ['i', 'like', 'to', 'eat', 'pizza', 'and', 'play', 'tennis']

    i2w = {i: word for i, word in enumerate(words)}
    w2i = {word: i for i, word in enumerate(words)}