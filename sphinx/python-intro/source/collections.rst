Collections Gems
================

.. highlight:: python

The ``collections`` module contains several standard-library data structures that solve common problems cleanly. Three especially useful ones are ``Counter``, ``defaultdict``, and ``deque``.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "Counter\ncount frequencies" as counter
   rectangle "defaultdict\nauto-create defaults" as defaultdict
   rectangle "deque\nfast queue operations" as deque
   @enduml

Counter
-------

``Counter`` is useful when you want to count how often values appear.

.. literalinclude:: code/oneoffcoder/collections/counter.py
   :language: python
   :linenos:

defaultdict
-----------

``defaultdict`` helps when missing keys should automatically start with a sensible default value.

.. literalinclude:: code/oneoffcoder/collections/defaultdict.py
   :language: python
   :linenos:

With a normal dictionary, you would need to check whether the key exists before appending to the list.

deque
-----

``deque`` is a double-ended queue. It is a better fit than a list when you need to add or remove items efficiently from both ends.

.. literalinclude:: code/oneoffcoder/collections/deque.py
   :language: python
   :linenos:

Why these matter
----------------

These types are worth learning early because they express intent directly. ``Counter`` means frequency counting, ``defaultdict`` means default values on first access, and ``deque`` means queue-like behavior. Using the right data structure usually makes the code shorter and easier to understand.

Exercise
--------

Build a tiny checkout analytics script for a coffee shop. You are given a list of drink orders, where each order is a tuple of ``(customer_name, drink_name)``. Use:

- ``Counter`` to find the three most common drinks
- ``defaultdict(list)`` to group drinks by customer
- ``deque`` to model a line of waiting orders and process them from the left

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "orders list" as orders
   rectangle "Counter\npopular drinks" as counter
   rectangle "defaultdict\ncustomer -> drinks" as grouped
   rectangle "deque\nwaiting line" as queue

   orders --> counter
   orders --> grouped
   orders --> queue
   @enduml

.. code-block:: python
   :linenos:

   orders = [
       ('Ava', 'latte'),
       ('Noah', 'tea'),
       ('Ava', 'espresso'),
       ('Mia', 'latte'),
       ('Noah', 'latte'),
       ('Luca', 'tea'),
       ('Ava', 'latte'),
   ]
