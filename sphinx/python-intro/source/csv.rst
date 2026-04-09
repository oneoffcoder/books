CSV
===

.. highlight:: python

Comma-separated values, or CSV, is a simple text format for tabular data. Python's ``csv`` module helps you read and write rows safely without manually splitting strings.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "rows of data" as rows
   rectangle "csv.writer" as writer
   rectangle "CSV file" as file
   rectangle "csv.reader" as reader

   rows --> writer
   writer --> file
   file --> reader
   reader --> rows
   @enduml

Writing CSV
-----------

Use ``csv.writer`` when you want to write rows to a CSV file.

.. literalinclude:: code/oneoffcoder/csv/write_csv.py
   :language: python
   :linenos:

Reading CSV
-----------

Use ``csv.reader`` to read rows back from a CSV file.

.. literalinclude:: code/oneoffcoder/csv/read_csv.py
   :language: python
   :linenos:

Dictionary rows
---------------

When your data has named columns, ``DictReader`` and ``DictWriter`` are often easier to understand.

.. literalinclude:: code/oneoffcoder/csv/dict_rows.py
   :language: python
   :linenos:

Exercise
--------

Write a CSV file for student scores with the columns ``name`` and ``score``. Then read the file back and print only the students whose score is at least 90.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "student rows" as rows
   rectangle "scores.csv" as csv
   rectangle "filtered high scorers" as high

   rows --> csv
   csv --> high
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   import csv

   rows = [
       {'name': 'Ava', 'score': 95},
       {'name': 'Noah', 'score': 88},
       {'name': 'Mia', 'score': 91},
   ]

   with open('scores.csv', 'w', newline='') as f:
       writer = csv.DictWriter(f, fieldnames=['name', 'score'])
       writer.writeheader()
       writer.writerows(rows)

   with open('scores.csv', newline='') as f:
       reader = csv.DictReader(f)
       for row in reader:
           if int(row['score']) >= 90:
               print(row['name'])
