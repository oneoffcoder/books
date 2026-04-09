JSON
====

.. highlight:: python

JSON is one of the most common ways to exchange structured data between programs, files, and web APIs. Python's ``json`` module lets you turn Python values into JSON text and parse JSON text back into Python values.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "Python dict / list" as py
   rectangle "json.dumps()" as dumps
   rectangle "JSON text" as text
   rectangle "json.loads()" as loads

   py --> dumps
   dumps --> text
   text --> loads
   loads --> py
   @enduml

Encoding JSON
-------------

Use ``json.dumps()`` to convert Python data into JSON text.

.. literalinclude:: code/oneoffcoder/json/encode.py
   :language: python
   :linenos:

Decoding JSON
-------------

Use ``json.loads()`` to parse JSON text into Python values.

.. literalinclude:: code/oneoffcoder/json/decode.py
   :language: python
   :linenos:

Pretty printing
---------------

When you want JSON output to be easy for humans to read, use indentation and key sorting.

.. literalinclude:: code/oneoffcoder/json/pretty.py
   :language: python
   :linenos:

Exercise
--------

Create a list of three books as dictionaries and convert it to JSON text. Then parse the JSON text back into Python data and print the title of each book.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "book dictionaries" as books
   rectangle "JSON text" as json
   rectangle "parsed books" as parsed

   books --> json
   json --> parsed
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   import json

   books = [
       {'title': 'Dune', 'author': 'Frank Herbert'},
       {'title': 'Foundation', 'author': 'Isaac Asimov'},
       {'title': 'Neuromancer', 'author': 'William Gibson'},
   ]

   raw = json.dumps(books)
   parsed = json.loads(raw)

   for book in parsed:
       print(book['title'])
