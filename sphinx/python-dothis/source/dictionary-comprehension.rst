Dictionary comprehension
------------------------

.. highlight:: python
   :linenothreshold: 1

Here, we want to create two dictionaries: index-to-word ``i2w`` and word-to-index ``w2i``. In the first approach, we build both with a loop. In the second, we use dictionary comprehensions to express the intent more directly.

A comprehension makes it obvious that the result is derived mechanically from another iterable without incremental mutation. That is usually easier to scan because the mapping logic sits next to the dictionary being constructed.

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
