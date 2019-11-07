Set comprehension
-----------------

.. highlight:: python
   :linenothreshold: 1

Set comprehension avoids for loops.

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
