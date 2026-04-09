Don't repeat yourself (DRY)
---------------------------

.. highlight:: python
   :linenothreshold: 1

It is easier to write ``'-' * 15`` to produce 15 consecutive dashes than to type them out manually.

Small string-building idioms like this matter because they prevent hard-coded visual artifacts from scattering through the code. They also make the intent parameterizable if the width later needs to change.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    print('---------------')

Do this
^^^^^^^

.. code:: python

    print('-'*15)
