Randomness
==========

.. highlight:: python

The ``random`` module is useful for games, simple simulations, sampling, and shuffling. It gives you common tools for making non-deterministic choices.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "random()" as random_value
   rectangle "randint()" as randint
   rectangle "choice()" as choice
   rectangle "shuffle()" as shuffle
   rectangle "sample()" as sample
   @enduml

Random numbers
--------------

Use ``randint()`` when you want a random integer in a closed range.

.. literalinclude:: code/oneoffcoder/random/random_numbers.py
   :language: python
   :linenos:

Picking values
--------------

Use ``choice()`` for a single random element and ``sample()`` for multiple unique values.

.. literalinclude:: code/oneoffcoder/random/pick_values.py
   :language: python
   :linenos:

Shuffling data
--------------

Use ``shuffle()`` when you want to rearrange a list in place.

.. literalinclude:: code/oneoffcoder/random/shuffle_cards.py
   :language: python
   :linenos:

Exercise
--------

Simulate rolling two dice 1,000 times. Count how often each total from 2 through 12 appears.

.. uml::

   @startuml
   skinparam shadowing false
   start
   :Roll die 1;
   :Roll die 2;
   :Add total;
   :Count result;
   repeat :repeat 1000 times;
   stop
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   from collections import Counter
   from random import randint

   counts = Counter()
   for _ in range(1000):
       total = randint(1, 6) + randint(1, 6)
       counts[total] += 1

   print(counts)
