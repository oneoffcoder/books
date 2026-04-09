Falsy and truthy
----------------

.. highlight:: python
   :linenothreshold: 1

It's enough to use the variable to test for falsy or truthy.

Explicit comparisons like ``== True`` and ``== False`` add noise and can obscure what counts as an empty or missing value. A direct truthiness check is the idiomatic default, though explicit comparisons are still useful when you truly need the boolean value ``True`` or ``False`` and not just a truthy object.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    is_male = True

    if is_male == True:
        print('is male is true')

Do this
^^^^^^^

.. code:: python

    is_male = True

    if is_male:
        print('is male is true')
