String interpolation
--------------------

.. highlight:: python
   :linenothreshold: 1

Prefer f-strings for most string interpolation in modern Python. They are usually the clearest option.

F-strings keep the literal text and embedded values in one place with very little ceremony. That tends to be easier to scan than older formatting styles, especially once expressions or format specifiers appear.

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
