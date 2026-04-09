Use heapq for top-N selection
-----------------------------

.. highlight:: python
   :linenothreshold: 1

If you only need a few smallest or largest items, avoid sorting the entire collection.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    top_scores = sorted(scores, reverse=True)[:3]

Do this
^^^^^^^

.. code:: python

    from heapq import nlargest

    top_scores = nlargest(3, scores)
