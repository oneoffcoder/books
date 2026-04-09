Don't repeat yourself (DRY)
---------------------------

.. highlight:: python
   :linenothreshold: 1

It is easier to write ``'-' * 15`` to produce 15 consecutive dashes than to type them out manually.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    print('---------------')

Do this
^^^^^^^

.. code:: python

    print('-'*15)
