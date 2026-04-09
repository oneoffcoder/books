TOML Configuration
==================

.. highlight:: python

Python 3.11 added ``tomllib`` to the standard library. TOML is a readable configuration format, and it is a good fit for settings files.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "config.toml" as toml
   rectangle "tomllib.load()" as load
   rectangle "Python dict" as data

   toml --> load
   load --> data
   @enduml

Reading TOML
------------

Use ``tomllib.load()`` to read TOML data from a file opened in binary mode.

.. literalinclude:: code/oneoffcoder/tomllib/read_toml.py
   :language: python
   :linenos:

Nested settings
---------------

TOML maps naturally to nested dictionaries.

.. literalinclude:: code/oneoffcoder/tomllib/nested_toml.py
   :language: python
   :linenos:

Exercise
--------

Create a ``settings.toml`` file for a small web app with an app name, port number, and debug flag. Load it with ``tomllib`` and print each setting.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "settings.toml" as settings
   rectangle "parsed settings" as parsed
   rectangle "printed config" as output

   settings --> parsed
   parsed --> output
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   import tomllib

   with open('settings.toml', 'rb') as f:
       settings = tomllib.load(f)

   print(settings['app']['name'])
   print(settings['app']['port'])
   print(settings['app']['debug'])
