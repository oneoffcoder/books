String interpolation
--------------------

.. highlight:: python
   :linenothreshold: 1

Prefer f-strings for most string interpolation in modern Python. They are usually the clearest option.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    name = 'John'
    food = 'pizza'
    sport = 'tennis'

    sentence = '{} likes to eat {}. {} likes to play {}.'.format(name, food, name, sport)

Do this
^^^^^^^

.. code:: python

    name = 'John'
    food = 'pizza'
    sport = 'tennis'

    sentence = f'{name} likes to eat {food}. {name} likes to play {sport}.'
