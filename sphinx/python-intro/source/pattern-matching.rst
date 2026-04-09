Structural Pattern Matching
===========================

.. highlight:: python

Structural pattern matching lets you branch on both the kind of value you received and the structure of that value. It is often clearer than a long chain of ``if`` and ``elif`` checks when the code is dispatching on shapes of data.

.. uml::

   @startuml
   start
   :Receive input value;
   if (case 1 matches?) then (yes)
     :Run case 1 block;
   elseif (case 2 matches?) then (yes)
     :Run case 2 block;
   else
     :Run default case _;
   endif
   stop
   @enduml

Basic matching
--------------

The ``match`` statement compares one value against a sequence of ``case`` patterns.

.. literalinclude:: code/oneoffcoder/pattern_matching/basic_match.py
   :language: python
   :linenos:

Matching structured data
------------------------

Pattern matching becomes more useful when the input is structured data such as dictionaries.

.. literalinclude:: code/oneoffcoder/pattern_matching/dict_match.py
   :language: python
   :linenos:

Matching with guards
--------------------

Sometimes the structure matches, but you also need an extra condition. In that case, you can use a guard with ``if``.

.. literalinclude:: code/oneoffcoder/pattern_matching/guard_match.py
   :language: python
   :linenos:

Why this matters
----------------

Pattern matching is useful when you are decoding commands, events, messages, or other structured inputs. It keeps the branching logic compact and makes each case read like a description of the shape you expect.

Exercise
--------

Build a tiny chat command router using ``match``. Support commands such as:

- ``{'type': 'join', 'room': 'python'}``
- ``{'type': 'message', 'room': 'python', 'text': 'hello'}``
- ``{'type': 'leave', 'room': 'python'}``

Print a different message for each command shape, and use a guard to reject empty messages.

.. uml::

   @startuml
   skinparam shadowing false
   start
   :Receive command dict;
   if (join?) then (yes)
     :announce room join;
   elseif (message and text?) then (yes)
     :print chat message;
   elseif (leave?) then (yes)
     :announce room leave;
   else
     :report unknown command;
   endif
   stop
   @enduml
