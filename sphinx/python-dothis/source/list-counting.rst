Most frequent item in list
--------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``Counter`` when you need frequencies. It is clearer and scales better than repeatedly calling ``list.count``.

Repeated ``list.count`` scans the same data over and over, which hides both intent and cost. ``Counter`` says you are computing frequencies once and then querying them.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    d = {}
    for num in nums:
        if num not in d:
            d[num] = 0
        d[num] += 1

    num, freq = None, None
    for n, f in d.items():
        if freq is None or f > freq:
            num = n
            freq = f

Do this
^^^^^^^

.. code:: python

    from collections import Counter

    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    num, freq = Counter(nums).most_common(1)[0]
