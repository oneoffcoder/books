Mini Projects
=============

The chapters in this book mostly teach one concept at a time. Mini-projects are where you combine several ideas into a single usable program.

.. graphviz::

   digraph projects {
     rankdir=LR;
     node [shape=box, style="rounded"];
     input [label="input"];
     logic [label="logic"];
     files [label="files / config"];
     output [label="output"];
     input -> logic -> output;
     files -> logic;
   }

Project 1: Personal Expense Tracker
-----------------------------------

Build a command-line program that:

- reads expenses from a CSV file
- groups them by category
- prints totals and the largest category
- optionally writes a JSON summary file

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "expenses.csv" as csv
   rectangle "parse rows" as parse
   rectangle "group by category" as group
   rectangle "summary.json" as json
   rectangle "report to terminal" as report

   csv --> parse
   parse --> group
   group --> json
   group --> report
   @enduml

Project 2: File Organizer
-------------------------

Build a script that scans a folder and sorts files into subfolders such as ``images``, ``notes``, and ``data`` based on file extension.

.. uml::

   @startuml
   skinparam shadowing false
   folder "source folder" as src
   folder images
   folder notes
   folder data

   src --> images : .png .jpg
   src --> notes : .txt .md
   src --> data : .csv .json
   @enduml

Project 3: Quiz Game
--------------------

Build a small terminal quiz that:

- loads questions from JSON
- shuffles the question order
- tracks correct answers
- prints the final score

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "questions.json" as questions
   rectangle "shuffle order" as shuffle
   rectangle "ask questions" as ask
   rectangle "score" as score

   questions --> shuffle
   shuffle --> ask
   ask --> score
   @enduml

One complete solution
---------------------

As a concrete example, here is a small solution for the quiz-game project shape.

.. literalinclude:: code/oneoffcoder/miniprojects/quiz_game.py
   :language: python
   :linenos:
