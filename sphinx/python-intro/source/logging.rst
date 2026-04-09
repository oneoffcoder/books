Logging
=======

.. highlight:: python

The ``logging`` module is the standard-library way to record what a program is doing. It is better than scattering ``print()`` calls through larger programs because it has levels, formatting, and better control.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "program code" as code
   rectangle "logger" as logger
   rectangle "levels\nDEBUG INFO WARNING ERROR" as levels
   rectangle "console or file" as output

   code --> logger
   logger --> levels
   levels --> output
   @enduml

Basic logging
-------------

Set up a basic logger and emit messages at several levels.

.. literalinclude:: code/oneoffcoder/logging/basic_logging.py
   :language: python
   :linenos:

Logging to a file
-----------------

You can write log output to a file instead of the console.

.. literalinclude:: code/oneoffcoder/logging/file_logging.py
   :language: python
   :linenos:

Why logging matters
-------------------

Logging is especially helpful when a script grows into a real application. It tells you what happened, when it happened, and where something failed.

Exercise
--------

Create a script that processes a list of usernames. Log an ``INFO`` message for each valid username and a ``WARNING`` message for any empty username.

.. uml::

   @startuml
   skinparam shadowing false
   start
   :Read username;
   if (empty?) then (yes)
     :log WARNING;
   else (no)
     :log INFO;
   endif
   repeat :next username;
   stop
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   import logging

   logging.basicConfig(level=logging.INFO)

   for username in ['ava', '', 'mia']:
       if not username:
           logging.warning('empty username encountered')
       else:
           logging.info('processing %s', username)
