Set comprehension
-----------------

.. highlight:: python
   :linenothreshold: 1

Set comprehensions are a concise way to build sets from iterables.

Like other comprehension forms, it puts the result shape front and center while leaving Python to manage the accumulation details. That makes it especially readable when uniqueness is part of the goal.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    words = ['i', 'like', 'to', 'eat', 'pizza', 'and', 'play', 'tennis']

    vocab = set()

    for word in words:
        vocab.add(word)

Do this
^^^^^^^

.. code:: python

    words = ['i', 'like', 'to', 'eat', 'pizza', 'and', 'play', 'tennis']

    vocab = {word for word in words}
