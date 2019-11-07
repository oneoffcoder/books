String interpolation
--------------------

.. highlight:: python
   :linenothreshold: 1

Note how we have to substitute name in twice? If we used variable names inside the substitution place holders, we only have to pass it in once. Also, note the use of f-string and Template.

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

    # variable substitution
    sentence = '{name} likes to eat {}. {name} likes to play {}.'.format(food, sport, name=name)

.. code:: python

    name = 'John'
    food = 'pizza'
    sport = 'tennis'

    # f-string
    sentence = f'{name} likes to eat {food}. {name} likes to play {sport}.'

.. code:: python

    from string import Template

    name = 'John'
    food = 'pizza'
    sport = 'tennis'

    # string template
    template = Template('$name likes to eat $food. $name likes to play $sport.')
    sentence = template.substitute(name=name, food=food, sport=sport)