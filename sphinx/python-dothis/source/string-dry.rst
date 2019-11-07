Don't repeat yourself (DRY)
---------------------------

.. highlight:: python
   :linenothreshold: 1

It's easier to do `'-'*15` to produce 15 consecutive dashes, than to type them all out.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    print('---------------')

Do this
^^^^^^^

.. code:: python

    print('-'*15)
