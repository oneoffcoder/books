Use heapq for top-N selection
-----------------------------

.. highlight:: python
   :linenothreshold: 1

If you only need a few smallest or largest items, avoid sorting the entire collection.

Partial selection algorithms matter when the collection is large and you only care about a small slice of it. ``heapq`` expresses that intent directly and avoids paying the readability and runtime cost of a full sort when you do not need one.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    top_scores = sorted(scores, reverse=True)[:3]

Do this
^^^^^^^

.. code:: python

    from heapq import nlargest

    top_scores = nlargest(3, scores)
