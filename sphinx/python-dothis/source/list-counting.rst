Most frequent item in list
--------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``max`` with ``set`` to find the most frequent item in a list.

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

    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    num = max(set(nums), key=nums.count)
